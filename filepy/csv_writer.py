from filepy.dto import DTO


class CsvWriter:
    def __init__(self, path_to_file: str, delimiter: str = ','):
        self._path_to_file = path_to_file
        self._delimiter = delimiter

    def write(self, dto: DTO):
        with open(self._path_to_file, 'w') as file:
            if dto.columns:
                file.write("{}".format(self._delimiter).join(dto.columns) + '\n')

            for row in dto.data:
                file.write("{}".format(self._delimiter).join(row) + '\n')
