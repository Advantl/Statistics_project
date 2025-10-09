# db_connection.py

import configparser
from sqlalchemy import create_engine
import pandas as pd

class PostgresConnection:
    def __init__(self, config_file='config_rfm.ini'):
        """
        Инициализация подключения к PostgreSQL
        :param config_file: путь к конфигурационному файлу
        """
        self.config_file = config_file
        self.db_params = self._load_config()
        self.connection_string = self._build_connection_string()
        self.engine = self._create_engine()

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

    def execute_query(self, query):
        """Выполняем SQL-запрос и возвращаем результат в виде DataFrame"""
        with self.engine.connect() as connection:
            result = pd.read_sql(query, connection)
        return result
