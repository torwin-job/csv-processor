import csv
from models import CSVRow


class CSVReader:
    """
    Класс для чтения CSV-файлов и преобразования их в объекты CSVRow.
    """

    def __init__(self, file_path: str) -> None:
        """
        Инициализация CSVReader.

        Args:
            file_path (str): Путь к CSV-файлу.
        """
        self.file_path: str = file_path

    def read(self) -> list[CSVRow]:
        """
        Читает CSV-файл и возвращает список объектов CSVRow.

        Returns:
            list[CSVRow]: Список строк CSV в виде объектов CSVRow.
        """
        with open(self.file_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            return [CSVRow(data=row) for row in reader]
