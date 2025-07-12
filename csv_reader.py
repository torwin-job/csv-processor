import csv
from models import CSVRow


class CSVReader:
    def __init__(self, file_path: str) -> None:
        self.file_path: str = file_path

    def read(self) -> list[CSVRow]:
        with open(self.file_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            return [CSVRow(data=row) for row in reader]
