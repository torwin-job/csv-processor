from dataclasses import dataclass, field
from typing import Any


@dataclass
class CSVRow:
    """
    Класс-обертка для строки CSV.
    Позволяет обращаться к данным как по ключу, так и через атрибуты.
    """

    data: dict[str, Any] = field(default_factory=dict)

    def __getitem__(self, key):
        """
        Получить значение по ключу.

        Args:
            key: Ключ (имя колонки).
        Returns:
            Значение из строки CSV.
        """
        return self.data[key]

    def __setitem__(self, key, value):
        """
        Установить значение по ключу.

        Args:
            key: Ключ (имя колонки).
            value: Значение для установки.
        """
        self.data[key] = value

    def __getattr__(self, key):
        """
        Получить значение по атрибуту (если нет обычного атрибута).

        Args:
            key: Имя атрибута/колонки.
        Returns:
            Значение из строки CSV.
        Raises:
            AttributeError: Если ключ не найден.
        """
        try:
            return self.data[key]
        except KeyError:
            raise AttributeError(key)
