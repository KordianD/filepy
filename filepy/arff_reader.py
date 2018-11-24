class ArffReader:
    def __init__(self, path_to_file):
        self._path_to_file: str = path_to_file
        self._relation: str = ""
        self._attributes: list = []
        self._data: list = []
        self._analyse()

    def _analyse(self):
        is_collecting_data = False
        for line in open(self._path_to_file):
            if line.strip() == [] or line.startswith('%'):
                is_collecting_data = False
                continue
            if ArffReader._is_line_containing_declaration(line, 'relation'):
                self._relation = line.split()[1]
            if ArffReader._is_line_containing_declaration(line, 'data'):
                is_collecting_data = True
            if ArffReader._is_line_containing_declaration(line, 'attribute'):
                self._attributes.append((line.split()[1], line.split()[2]))
            if is_collecting_data and not ArffReader._is_line_containing_declaration(line, 'data'):
                self._data.append(line.strip().split(','))

    @staticmethod
    def _is_line_containing_declaration(line: str, declaration: str):
        return line.strip() and line.split()[0].lower() == '@' + declaration
