from classes.csvReader.vendor.CsvReaderInterface import CsvReaderInterface
import csv

"""CSV Reader class."""
class CsvReader(CsvReaderInterface):

    def __init__(self, path: str) -> None:
        self.path = path

    def get_data(self) -> list:
        with open(self.path) as csvfile:
            return csv.reader(csvfile, delimiter=',')
