from classes.csvReader.vendor.CsvReaderInterface import CsvReaderInterface

"""interface for the CsvReaderFactory."""
class CsvReaderInterfaceFactory:

    def __init__(self, path :str) -> None:
        """Initialize the CsvReader interface."""
        pass

    def createReader(self) -> CsvReaderInterface:
        """Create an instance from csv reader"""
        pass