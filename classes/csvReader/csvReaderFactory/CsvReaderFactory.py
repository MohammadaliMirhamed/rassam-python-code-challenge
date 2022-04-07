from classes.csvReader.csvReaderFactory.vendor.CsvReaderFactoryInterface import CsvReaderInterfaceFactory
from classes.csvReader.vendor.CsvReaderInterface import CsvReaderInterface
from classes.csvReader.CsvReader import CsvReader


"""CsvReaderFactory class."""
class CsvReaderFactory(CsvReaderInterfaceFactory):

    def __init__(self, path :str) -> None:
        # Initialize path
        self.path = path

    def createReader(self) -> CsvReaderInterface:
        # create an instance of CsvReader
        return CsvReader(self.path)