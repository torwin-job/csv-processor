from abc import ABC, abstractmethod
from typing import List, Any


class Aggregation(ABC):
    @abstractmethod
    def aggregate(self, values: List[float]) -> Any:
        pass


class AvgAggregation(Aggregation):
    def aggregate(self, values: List[float]) -> float | None:
        return sum(values) / len(values) if values else None


class MinAggregation(Aggregation):
    def aggregate(self, values: List[float]) -> float:
        return min(values)


class MaxAggregation(Aggregation):
    def aggregate(self, values: List[float]) -> float:
        return max(values)
