from filepy.csv_reader import CsvReader

TEST_FILENAME = 'test/at/data/csv_files/reader_example_1.csv'


def test_correctly_read_csv_with_column_labels():
    csv_reader = CsvReader(TEST_FILENAME)
    assert csv_reader._column_names == ['Index', 'Girth (in)', 'Height (ft)', 'Volume (ft^3)']

    assert csv_reader._data == [['1', '8.3', '70', '10.3'],
                                ['2', '8.6', '65', '10.3'],
                                ['3', '8.8', '63', '10.2'],
                                ['4', '10.5', '72', '16.4'],
                                ['5', '10.7', '81', '18.8']]
