import argparse
from tabulate import tabulate
import sys
from csv_reader import CSVReader
from factory import FilterFactory, AggregationFactory


def main() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description="Обработка CSV: фильтрация и агрегация (ООП)"
    )
    parser.add_argument("--file", required=True, help="Путь к CSV-файлу")
    parser.add_argument("--where", help="Фильтрация, например: price>500")
    parser.add_argument("--aggregate", help="Агрегация, например: price=avg")
    parser.add_argument(
        "--order-by", help="Сортировка, например: price:asc или price:desc"
    )
    args = parser.parse_args()

    reader: CSVReader = CSVReader(args.file)
    rows: list = reader.read()

    # Сортировка до агрегации и вывода
    if args.where:
        try:
            filter_obj = FilterFactory.create(args.where)
        except Exception as e:
            print(f"Ошибка фильтрации: {e}", file=sys.stderr)
            sys.exit(1)
        filtered: list = [row for row in rows if filter_obj.apply(row)]
    else:
        filtered = rows

    # Сортировка
    if args.order_by:
        try:
            if ":" in args.order_by:
                column, direction = args.order_by.split(":", 1)
                column = column.strip()
                direction = direction.strip().lower()
            else:
                column = args.order_by.strip()
                direction = "asc"
            reverse = direction == "desc"
            filtered = sorted(filtered, key=lambda row: row[column], reverse=reverse)
        except Exception as e:
            print(f"Ошибка сортировки: {e}", file=sys.stderr)
            sys.exit(1)

    if args.aggregate:
        try:
            column, agg_obj = AggregationFactory.create(args.aggregate)
        except Exception as e:
            print(f"Ошибка агрегации: {e}", file=sys.stderr)
            sys.exit(1)
        try:
            values: list[float] = [float(row[column]) for row in filtered]
        except Exception as e:
            print(f"Ошибка преобразования данных для агрегации: {e}", file=sys.stderr)
            sys.exit(1)
        agg_type = args.aggregate.split("=")[1]
        key = f"{column} {agg_type}"
        result: dict = {key: agg_obj.aggregate(values)}
        print(tabulate([result], headers="keys", tablefmt="grid"))
    else:
        # Преобразуем список CSVRow в список dict для корректного вывода таблицы
        print(tabulate([row.data for row in filtered], headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    main()
