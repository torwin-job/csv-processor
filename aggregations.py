from abc import ABC, abstractmethod
from typing import Any


class Aggregation(ABC):
    """
    Абстрактный базовый класс для агрегаторов.
    Определяет интерфейс для агрегирующих функций над списком чисел.
    """
    @abstractmethod
    def aggregate(self, values: list[float]) -> Any:
        """
        Выполняет агрегирование значений.

        Args:
            values (list[float]): Список числовых значений для агрегирования.
        Returns:
            Any: Результат агрегирования (тип зависит от реализации).
        """
        pass


class AvgAggregation(Aggregation):
    """
    Агрегатор для вычисления среднего значения.
    """
    def aggregate(self, values: list[float]) -> float | None:
        """
        Вычисляет среднее значение списка.

        Args:
            values (list[float]): Список чисел.
        Returns:
            float | None: Среднее значение или None, если список пуст.
        """
        return sum(values) / len(values) if values else None


class MinAggregation(Aggregation):
    """
    Агрегатор для поиска минимального значения.
    """
    def aggregate(self, values: list[float]) -> float:
        """
        Находит минимальное значение в списке.

        Args:
            values (list[float]): Список чисел.
        Returns:
            float: Минимальное значение.
        """
        return min(values)


class MaxAggregation(Aggregation):
    """
    Агрегатор для поиска максимального значения.
    """
    def aggregate(self, values: list[float]) -> float:
        """
        Находит максимальное значение в списке.

        Args:
            values (list[float]): Список чисел.
        Returns:
            float: Максимальное значение.
        """
        return max(values)
