from filepy.analyse_helper import create_attributes_to_save
from filepy.analyse_helper import extract_filename_from_path_to_file
from filepy.dto import DTO


class ArffWriter:
    def __init__(self, path_to_file: str, delimiter: str = ','):
        self._path_to_file: str = path_to_file
        self._delimiter: str = delimiter

    @property
    def path_to_file(self):
        return self._path_to_file

    @property
    def delimiter(self):
        return self._delimiter

    def write(self, dto: DTO):
        with open(self.path_to_file, 'w') as file:
            file.write('@relation {}\n\n'.format(
                extract_filename_from_path_to_file(self.path_to_file)))
            file.write(create_attributes_to_save(dto) + '\n')

            file.write('@data\n')
            for row in dto.data:
                file.write("{delimiter}".format(
                    delimiter=self.delimiter).join(row) + '\n')
