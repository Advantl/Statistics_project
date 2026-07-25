# db_connection.py

import configparser
import psycopg
import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.engine import URL
from config_loader import load_config
from pathlib import Path
import logging
import time

logger = logging.getLogger(__name__)

class PostgresConnection:

    def __init__(self, config_file="config_rfm.ini"):
        params = load_config(config_file)

        self.url = URL.create(
            drivername="postgresql+psycopg",
            username=params["user"],
            password=params["password"],
            host=params["host"],
            port=params["port"],
            database=params["database"],
        )

        self.engine = create_engine(
            self.url,
            pool_pre_ping=True,
            future=True,
            pool_recycle=3600
        )

        self._check_connection()
        logger.info("Соединение с PostgreSQL успешно установлено.")

    def _check_connection(self):
        try:
            with self.engine.connect() as conn:
                conn.execute(text("SELECT 1"))
        except SQLAlchemyError as e:
            logger.error("Ошибка подключения к PostgreSQL: %s", e)
            raise ConnectionError(
                "Не удалось установить соединение с PostgreSQL."
            ) from e

    def execute_query(self, query, cache_path=None, force_refresh=False):
        """
        Выполняет SQL-запрос с опциональным кэшированием.
        Если cache_path указан и файл существует — загружает результат из него.
        """

        cache_file = Path(cache_path)
        cache_file.parent.mkdir(parents=True, exist_ok=True)

        if (cache_path and Path(cache_path).exists() and not force_refresh):
            logger.info("Используется кэш: %s", cache_path)
            return pd.read_parquet(cache_file)


        logger.info("Выполнение SQL-запроса...")
        start = time.perf_counter()
        with self.engine.connect() as connection:
            result = pd.read_sql(text(query), connection)
        elapsed = time.perf_counter() - start
        logger.info(
            "Запрос выполнен за %.2f сек. Получено %d строк.",
            elapsed,
            len(result),
        )

        if cache_path:
            result.to_parquet(cache_file)
            logger.info("Результат сохранён в %s", cache_path)

        return result

