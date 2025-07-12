from abc import ABC, abstractmethod
from typing import Any


class Aggregation(ABC):
    @abstractmethod
    def aggregate(self, values: list[float]) -> Any:
        pass


class AvgAggregation(Aggregation):
    def aggregate(self, values: list[float]) -> float | None:
        return sum(values) / len(values) if values else None


class MinAggregation(Aggregation):
    def aggregate(self, values: list[float]) -> float:
        return min(values)


class MaxAggregation(Aggregation):
    def aggregate(self, values: list[float]) -> float:
        return max(values)
