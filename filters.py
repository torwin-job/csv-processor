from abc import ABC, abstractmethod
from typing import Any
from models import CSVRow


class Filter(ABC):
    @abstractmethod
    def apply(self, row: dict[str, Any] | CSVRow) -> bool:
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
    def __init__(self, column: str, value: Any) -> None:
        self.column: str = column
        self.value: Any = value

    def apply(self, row: dict[str, Any] | CSVRow) -> bool:
        try:
            return str(row[self.column]) == str(self.value)
        except Exception:
            return False
