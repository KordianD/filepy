class CsvReader:
    def __init__(self, path_to_file: str, delimiter: str = ',', first_line_column_names: bool = True,
                 skip_first_column: bool = False):
        self._path_to_file: str = path_to_file
        self._delimiter: str = delimiter
        self._first_line_column_names: bool = first_line_column_names
        self._skip_first_column: bool = skip_first_column
        self._data: list = []
        self._column_names: list = []
        self._analyse()

    def _analyse(self):
        for index, line in enumerate(open(self._path_to_file)):
            if index == 0 and self._first_line_column_names:
                self._column_names = line.strip().split(self._delimiter)
                continue
            if self._skip_first_column:
                self._data.append(line.strip().split(self._delimiter)[1:])
            else:
                self._data.append(line.strip().split(self._delimiter))
