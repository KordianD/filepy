from filepy.analyse_helper import is_line_containing_declaration, split_attributes
from filepy.dto import DTO


class ArffReader:
    def __init__(self, path_to_file, delimiter=','):
        self._path_to_file: str = path_to_file
        self._delimiter = delimiter
        self.dto: DTO = None
        self._analyse()

    def _analyse(self):
        is_collecting_data = False
        data: list = []
        columns: list = []
        additional: dict = {'relation': "", 'attributes': []}

        for line in open(self._path_to_file):
            if line.strip() == [] or line.startswith('%'):
                continue
            if is_line_containing_declaration(line, 'relation'):
                additional['relation'] = line.split()[1]
            if is_line_containing_declaration(line, 'data'):
                is_collecting_data = True
            if is_line_containing_declaration(line, 'attribute'):
                column, attribute = split_attributes(line)
                columns.append(column)
                additional['attributes'].append(attribute)
            if is_collecting_data and not is_line_containing_declaration(line, 'data'):
                data.append(line.strip().split(self._delimiter))

        self.dto = DTO(data=data, columns=columns, additional=additional)
