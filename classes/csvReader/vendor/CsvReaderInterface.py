"""interface for the CsvReader."""
class CsvReaderInterface:

    def __init__(self, path :str) -> None:
        """Initialize the CsvReader interface."""
        pass

    def get_data(self) -> list:
        """Return the data from the csv file."""
        pass