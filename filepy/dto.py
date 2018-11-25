class DTO:
    def __init__(self, data: list, columns: list, additional=None):
        self._data: list = data
        self._columns: list = columns
        self._additional: dict = additional

    @property
    def data(self):
        return self._data

    @property
    def columns(self):
        return self._columns

    @property
    def additional(self):
        return self._additional
