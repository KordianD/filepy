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
            if ArffReader._is_line_containing_declaration(line, 'relation'):
                additional['relation'] = line.split()[1]
            if ArffReader._is_line_containing_declaration(line, 'data'):
                is_collecting_data = True
            if ArffReader._is_line_containing_declaration(line, 'attribute'):
                columns.append(line.split()[1])
                additional['attributes'].append(line.split()[2])
            if is_collecting_data and not ArffReader._is_line_containing_declaration(line, 'data'):
                data.append(line.strip().split(','))

        self.dto = DTO(data=data, columns=columns, additional=additional)

    @staticmethod
    def _is_line_containing_declaration(line: str, declaration: str):
        return line.strip() and line.split()[0].lower() == '@' + declaration
