from filepy.analyse_helper import is_line_containing_declaration
from filepy.dto import DTO


class ArffReader:
    def __init__(self, path_to_file):
        self._path_to_file: str = path_to_file
        self.dto: DTO = None
        self._analyse()

    def _analyse(self):
        is_collecting_data = False
        data: list = []
        columns: list = []
        additional: dict = {'relation': "", 'attributes': []}

        for line in open(self._path_to_file):
            if line.strip() == [] or line.startswith('%'):
                is_collecting_data = False
                continue
            if is_line_containing_declaration(line, 'relation'):
                additional['relation'] = line.split()[1]
            if is_line_containing_declaration(line, 'data'):
                is_collecting_data = True
            if is_line_containing_declaration(line, 'attribute'):
                columns.append(line.split()[1])
                additional['attributes'].append(line.split()[2])
            if is_collecting_data and not is_line_containing_declaration(line, 'data'):
                data.append(line.strip().split(','))

        self.dto = DTO(data=data, columns=columns, additional=additional)
