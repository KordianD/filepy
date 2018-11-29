import re

from filepy.dto import DTO


class CsvReader:
    def __init__(self, path_to_file: str, delimiter: str = ',', first_line_column_names: bool = True,
                 skip_first_column: bool = False):
        self._path_to_file: str = path_to_file
        self._delimiter: str = delimiter
        self._first_line_column_names: bool = first_line_column_names
        self._skip_first_column: bool = skip_first_column
        self.dto = None
        self._analyse()

    def _analyse(self):
        data: list = []
        columns: list = []

        for index, line in enumerate(open(self._path_to_file)):
            if index == 0 and self._first_line_column_names:
                if self._skip_first_column:
                    columns = re.compile(
                        self._delimiter).split(line.strip())[1:]
                else:
                    columns = re.compile(self._delimiter).split(line.strip())
                continue
            if self._skip_first_column:
                data.append(re.compile(
                    self._delimiter).split(line.strip())[1:])
            else:
                data.append(re.compile(self._delimiter).split(line.strip()))

        self.dto = DTO(data=data, columns=columns)
