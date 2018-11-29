from filepy.dto import DTO


class CsvWriter:
    def __init__(self, path_to_file: str, delimiter: str = ',', skip_writing_columns=False):
        self._path_to_file: str = path_to_file
        self._delimiter: str = delimiter
        self._skip_writing_columns: bool = skip_writing_columns

    def write(self, dto: DTO):
        with open(self._path_to_file, 'w') as file:
            if dto.columns and not self._skip_writing_columns:
                file.write("{}".format(self._delimiter).join(
                    dto.columns) + '\n')

            for row in dto.data:
                file.write("{}".format(self._delimiter).join(row) + '\n')
