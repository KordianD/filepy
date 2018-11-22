class ArffWriter:
    def __init__(self, path_to_file: str, delimiter: str = ','):
        self.path_to_file = path_to_file
        self.delimiter = delimiter
        self.dto = None

    def write(self):
        with open(self.path_to_file, 'w') as file:
            file.write('@relation {}\n\n'.format(self._extract_filename_from_path_to_file()))
            file.write(self._create_attributes_to_save() + '\n')

            file.write('@data\n')
            for row in self.dto.data:
                file.write("{}".format(self.delimiter).join(row) + '\n')

    def _extract_filename_from_path_to_file(self):
        index_of_starting_filename = self.path_to_file.rfind('/')
        if index_of_starting_filename == -1:
            return self.path_to_file
        return self.path_to_file[index_of_starting_filename + 1:]

    def _create_attributes_to_save(self) -> str:
        attributes = ""
        first_data_line = self.dto.data[0]
        for column, data in zip(self.dto.columns, first_data_line):
            attributes += "@attribute {} {}\n".format(column, ArffWriter._classify_attribute(data[0]))
        return attributes

    @staticmethod
    def _classify_attribute(attribute):
        try:
            print(attribute)
            float(attribute)
        except ValueError:
            return "string"
        return "numeric"
