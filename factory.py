from filters import GreaterThanFilter, LessThanFilter, EqualFilter, Filter
from aggregations import AvgAggregation, MinAggregation, MaxAggregation, Aggregation


class FilterFactory:
    @staticmethod
    def create(where: str) -> Filter:
        if ">" in where:
            column, value = where.split(">", 1)
            return GreaterThanFilter(column.strip(), float(value.strip()))
        elif "<" in where:
            column, value = where.split("<", 1)
            return LessThanFilter(column.strip(), float(value.strip()))
        elif "=" in where:
            column, value = where.split("=", 1)
            return EqualFilter(column.strip(), value.strip())
        else:
            raise ValueError("Некорректное условие фильтрации")


class AggregationFactory:
    @staticmethod
    def create(aggregate: str) -> tuple[str, Aggregation]:
        if "=" not in aggregate:
            raise ValueError("Некорректное условие агрегации")
        column, func = aggregate.split("=", 1)
        func = func.strip()
        if func == "avg":
            return column.strip(), AvgAggregation()
        elif func == "min":
            return column.strip(), MinAggregation()
        elif func == "max":
            return column.strip(), MaxAggregation()
        else:
            raise ValueError("Неизвестная агрегация: " + func)
