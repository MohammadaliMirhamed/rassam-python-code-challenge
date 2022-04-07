from classes.csvReader.vendor.CsvReaderInterface import CsvReaderInterface
import pandas as pd

"""Pondas CSV Reader class."""
class PondasReader(CsvReaderInterface):

    def __init__(self, path: str) -> None:
        self.path = path

    def get_data(self) -> list:
        return pd.read_csv(self.path)
