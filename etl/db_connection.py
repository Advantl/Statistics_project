# db_connection.py

import configparser
from sqlalchemy import create_engine
import pandas as pd
import os
from config_loader import load_config


class PostgresConnection:
    def __init__(self, config_file='config_rfm.ini'):
        params = load_config(config_file)
        self.connection_string = (
            f"postgresql://{params['user']}:{params['password']}@"
            f"{params['host']}:{params['port']}/{params['database']}"
        )
        self.engine = create_engine(self.connection_string)

    def _load_config(self):
        """Загружаем параметры подключения из конфигурационного файла"""
        config = configparser.ConfigParser()
        config.read(self.config_file)
        return config['postgresql']

    def _build_connection_string(self):
        """Формируем строку подключения"""
        return f"postgresql://{self.db_params['user']}:{self.db_params['password']}@" \
               f"{self.db_params['host']}:{self.db_params['port']}/{self.db_params['database']}"

    def _create_engine(self):
        """Создаем engine для подключения к базе данных"""
        return create_engine(self.connection_string)

    def execute_query(self, query, cache_path=None):
        """
        Выполняет SQL-запрос с опциональным кэшированием.
        Если cache_path указан и файл существует — загружает результат из него.
        """
        if cache_path and os.path.exists(cache_path):
            print(f"Загрузка данных из кэша: {cache_path}")
            return pd.read_csv(cache_path)

        print("Выполнение SQL-запроса...")
        with self.engine.connect() as connection:
            result = pd.read_sql(query, connection)

        if cache_path:
            result.to_csv(cache_path, index=False)
            print(f"Результат сохранён в кэш: {cache_path}")

        return result