import os
import tempfile
import pytest
from csv_reader import CSVReader
from factory import FilterFactory, AggregationFactory



TEST_CSV = """name,price,qty
apple,100,5
banana,50,10
orange,70,7
"""


def create_temp_csv(content):
    fd, path = tempfile.mkstemp(suffix=".csv")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(content)
    return path


def test_csv_read():
    path = create_temp_csv(TEST_CSV)
    reader = CSVReader(path)
    rows = reader.read()
    assert len(rows) == 3
    assert rows[0]["name"] == "apple"
    assert rows[1]["price"] == "50"
    os.remove(path)


def test_filter_gt():
    path = create_temp_csv(TEST_CSV)
    reader = CSVReader(path)
    rows = reader.read()
    filter_obj = FilterFactory.create("price>60")
    filtered = [row for row in rows if filter_obj.apply(row)]
    assert len(filtered) == 2
    assert filtered[0]["name"] == "apple"
    os.remove(path)


def test_filter_eq():
    path = create_temp_csv(TEST_CSV)
    reader = CSVReader(path)
    rows = reader.read()
    filter_obj = FilterFactory.create("name=banana")
    filtered = [row for row in rows if filter_obj.apply(row)]
    assert len(filtered) == 1
    assert filtered[0]["price"] == "50"
    os.remove(path)


def test_filter_lt():
    path = create_temp_csv(TEST_CSV)
    reader = CSVReader(path)
    rows = reader.read()
    filter_obj = FilterFactory.create("qty<8")
    filtered = [row for row in rows if filter_obj.apply(row)]
    assert len(filtered) == 2
    assert filtered[0]["name"] == "apple"
    os.remove(path)


def test_filter_nonexistent_column():
    path = create_temp_csv(TEST_CSV)
    reader = CSVReader(path)
    rows = reader.read()
    filter_obj = FilterFactory.create("notacolumn=123")
    filtered = [row for row in rows if filter_obj.apply(row)]
    assert len(filtered) == 0
    os.remove(path)


def test_aggregation_avg():
    path = create_temp_csv(TEST_CSV)
    reader = CSVReader(path)
    rows = reader.read()
    column, agg_obj = AggregationFactory.create("price=avg")
    values = [float(row[column]) for row in rows]
    avg = agg_obj.aggregate(values)
    assert avg == pytest.approx((100 + 50 + 70) / 3)
    os.remove(path)


def test_aggregation_min():
    path = create_temp_csv(TEST_CSV)
    reader = CSVReader(path)
    rows = reader.read()
    column, agg_obj = AggregationFactory.create("price=min")
    values = [float(row[column]) for row in rows]
    result = agg_obj.aggregate(values)
    assert result == 50
    os.remove(path)


def test_aggregation_max():
    path = create_temp_csv(TEST_CSV)
    reader = CSVReader(path)
    rows = reader.read()
    column, agg_obj = AggregationFactory.create("qty=max")
    values = [float(row[column]) for row in rows]
    result = agg_obj.aggregate(values)
    assert result == 10
    os.remove(path)


def test_aggregation_nonexistent_column():
    path = create_temp_csv(TEST_CSV)
    reader = CSVReader(path)
    rows = reader.read()
    with pytest.raises(KeyError):
        column, agg_obj = AggregationFactory.create("notacolumn=avg")
        values = [float(row[column]) for row in rows]
        agg_obj.aggregate(values)
    os.remove(path)


def test_aggregation_empty():
    path = create_temp_csv("name,price\n")
    reader = CSVReader(path)
    rows = reader.read()
    column, agg_obj = AggregationFactory.create("price=avg")
    values = [float(row[column]) for row in rows]
    result = agg_obj.aggregate(values)
    assert result is None or result == 0 or result != result  # None или NaN
    os.remove(path)


def test_sorting():
    path = create_temp_csv(TEST_CSV)
    reader = CSVReader(path)
    rows = reader.read()
    sorted_rows = sorted(rows, key=lambda row: float(row["price"]), reverse=True)
    assert sorted_rows[0]["name"] == "apple"
    assert sorted_rows[-1]["name"] == "banana"
    os.remove(path)
