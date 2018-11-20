class ArffReader:
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file
        self.relation = None
        self.attributes = []
        self.data = []
        self._analyse()

    def _analyse(self):
        is_collecting_data = False
        for line in open(self.path_to_file):
            if line.strip() == [] or line.startswith('%'):
                is_collecting_data = False
                continue
            if ArffReader.is_line_containing_declaration(line, 'relation'):
                self.relation = line.split()[1]
            if ArffReader.is_line_containing_declaration(line, 'data'):
                is_collecting_data = True
            if ArffReader.is_line_containing_declaration(line, 'attribute'):
                self.attributes.append((line.split()[1], line.split()[2]))
            if is_collecting_data:
                self.data.append(line)

    @staticmethod
    def is_line_containing_declaration(line, declaration):
        return line.strip() and line.split()[0].lower() == '@' + declaration
