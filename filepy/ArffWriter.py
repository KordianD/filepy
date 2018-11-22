class ArffWriter:
    def __init__(self, path_to_file, delimiter=','):
        self.path_to_file = path_to_file
        self.delimiter = delimiter
        self.dto = None

    def write(self):
        with open(self.path_to_file, 'w') as file:
            self._write_relation_to_file(file)
            self._write_labels_to_file(file)

    def _write_relation_to_file(self, file):
        file.write(r'@relation {}'.format(self._extract_filename_from_path_to_file()))

    def _extract_filename_from_path_to_file(self):
        index_of_starting_filename = self.path_to_file.rfind('/')
        if index_of_starting_filename == -1:
            return self.path_to_file
        return self.path_to_file[index_of_starting_filename + 1:]

    def _write_labels_to_file(self, file):
        pass

    def _write_data_to_file(self, file):
        for row in self.dto:
            file.write(",".join(row) + '\n')
