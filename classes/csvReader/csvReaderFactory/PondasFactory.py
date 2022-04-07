from classes.csvReader.csvReaderFactory.vendor.CsvReaderFactoryInterface import CsvReaderInterfaceFactory
from classes.csvReader.vendor.CsvReaderInterface import CsvReaderInterface
from classes.csvReader.PondasReader import PondasReader


"""PondasFactory class."""
class PondasFactory(CsvReaderInterfaceFactory):

    def __init__(self, path :str) -> None:
        # Initialize path
        self.path = path

    def createReader(self) -> CsvReaderInterface:
        # create an instance of PondasReader
        return PondasReader(self.path)