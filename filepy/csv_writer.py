class CsvWriter:
    def __init__(self, path_to_file: str, delimiter: str = ','):
        self.path_to_file = path_to_file
        self.delimiter = delimiter
