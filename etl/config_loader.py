import configparser
from pathlib import Path

def load_config(config_file='config_rfm.ini', section='postgresql'):
    """
    Загружает настройки из .ini файла.
    :param config_file: путь к конфигурационному файлу
    :param section: секция (по умолчанию 'postgresql')
    :return: dict с параметрами подключения
    """
    config_path = Path(config_file)
    if not config_path.exists():
        raise FileNotFoundError(f"Конфигурационный файл не найден: {config_path}")

    parser = configparser.ConfigParser()
    parser.read(config_path)

    if section not in parser:
        raise ValueError(f"Секция '{section}' не найдена в {config_file}")

    return dict(parser[section])
