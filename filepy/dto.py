class DTO:
    def __init__(self, data, columns):
        self._data = data
        self._columns = columns

    @property
    def data(self):
        return self._data

    @property
    def columns(self):
        return self._columns
