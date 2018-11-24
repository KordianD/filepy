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
        with open(self._path_to_file, 'w') as file:
            file.write('@relation {}\n\n'.format(
                self._extract_filename_from_path_to_file()))
            file.write(ArffWriter._create_attributes_to_save(dto) + '\n')

            file.write('@data\n')
            for row in dto.data:
                file.write("{}".format(self._delimiter).join(row) + '\n')

    def _extract_filename_from_path_to_file(self):
        index_of_starting_filename = self._path_to_file.rfind('/')
        if index_of_starting_filename == -1:
            return self._path_to_file
        return self._path_to_file[index_of_starting_filename + 1:]

    @staticmethod
    def _create_attributes_to_save(dto: DTO) -> str:
        attributes = ""
        first_data_line = dto.data[0]
        for column, data in zip(dto.columns, first_data_line):
            attributes += "@attribute {} {}\n".format(
                column, ArffWriter._classify_attribute(data[0]))
        return attributes

    @staticmethod
    def _classify_attribute(attribute):
        try:
            float(attribute)
        except ValueError:
            return "string"
        return "numeric"
