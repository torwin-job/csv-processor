from abc import ABC, abstractmethod
from typing import Any
from models import CSVRow


class Filter(ABC):
    """
    Абстрактный базовый класс для фильтров.
    Определяет интерфейс для фильтрации строк CSV.
    """
    @abstractmethod
    def apply(self, row: dict[str, Any] | CSVRow) -> bool:
        """
        Проверяет, удовлетворяет ли строка условию фильтра.

        Args:
            row (dict[str, Any] | CSVRow): Строка CSV для проверки.
        Returns:
            bool: True, если строка проходит фильтр, иначе False.
        """
        pass


class GreaterThanFilter(Filter):
    def __init__(self, column: str, value: float) -> None:
        self.column: str = column
        self.value: float = value

    def apply(self, row: dict[str, Any] | CSVRow) -> bool:
        try:
            return float(row[self.column]) > self.value
        except Exception:
            return False


class LessThanFilter(Filter):
    def __init__(self, column: str, value: float) -> None:
        self.column: str = column
        self.value: float = value

    def apply(self, row: dict[str, Any] | CSVRow) -> bool:
        try:
            return float(row[self.column]) < self.value
        except Exception:
            return False


class EqualFilter(Filter):
    """
    Фильтр для проверки равенства значения в колонке.
    """
    def __init__(self, column: str, value: Any) -> None:
        """
        Инициализация фильтра.

        Args:
            column (str): Имя колонки.
            value (Any): Значение для сравнения.
        """
        self.column: str = column
        self.value: Any = value

    def apply(self, row: dict[str, Any] | CSVRow) -> bool:
        """
        Проверяет, равно ли значение в колонке заданному.

        Args:
            row (dict[str, Any] | CSVRow): Строка CSV для проверки.
        Returns:
            bool: True, если значение равно заданному, иначе False.
        """
        try:
            return str(row[self.column]) == str(self.value)
        except Exception:
            return False
