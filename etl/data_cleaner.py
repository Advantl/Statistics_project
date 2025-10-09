import pandas as pd


class DataCleaner:
    def __init__(self, data: pd.DataFrame):
        """
        Инициализация объекта для очистки данных.

        :param data: pandas DataFrame
        """
        self.data = data

    def drop_negative_values(self, columns=None):
        """
        Удаляет строки, где значения в указанных колонках меньше 0.

        :param columns: список колонок для проверки (по умолчанию проверяются 'dr_sdisc' и 'dr_kol')
        :return: DataFrame без строк с отрицательными значениями
        """
        if columns is None:
            columns = ['dr_sdisc', 'dr_kol']

        # Создаем логическую маску для строк с отрицательными значениями в указанных колонках
        mask = self.data[columns].lt(0).any(axis=1)

        # Удаляем строки с отрицательными значениями
        self.data = self.data[~mask]
        return self.data

    def drop_error_check_values(self, values_to_check=None):
        """
        Удаляет строки, где значения в колонке 'dr_nchk' принадлежат списку заданных значений.

        :param values_to_check: список значений для удаления (по умолчанию [21, 593, 2495])
        :return: DataFrame без строк с заданными значениями
        """
        if values_to_check is None:
            values_to_check = [21, 593, 2495]  # Заданные значения для удаления

        # Находим индексы строк, которые содержат эти значения
        error_check = self.data[self.data['dr_nchk'].isin(values_to_check)].index.tolist()

        # Удаляем строки по найденным индексам
        self.data = self.data.drop(error_check)
        return self.data

    def get_data(self):
        """Возвращает текущий DataFrame"""
        return self.data
