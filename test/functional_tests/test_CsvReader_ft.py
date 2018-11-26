from filepy.csv_reader import CsvReader

TEST_FILENAME = 'test/data/csv_files/reader_example_1.csv'


def test_should_correctly_read_csv_with_column_labels():
    csv_reader = CsvReader(TEST_FILENAME)
    assert csv_reader.dto.columns == [
        'Index', 'Girth (in)', 'Height (ft)', 'Volume (ft^3)']

    assert csv_reader.dto.data == [['1', '8.3', '70', '10.3'],
                                   ['2', '8.6', '65', '10.3'],
                                   ['3', '8.8', '63', '10.2'],
                                   ['4', '10.5', '72', '16.4'],
                                   ['5', '10.7', '81', '18.8']]


def test_should_correctly_read_csv_without_column_labels():
    csv_reader = CsvReader(TEST_FILENAME, first_line_column_names=False)
    assert csv_reader.dto.columns == []

    assert csv_reader.dto.data == [['Index', 'Girth (in)', 'Height (ft)', 'Volume (ft^3)'],
                                   ['1', '8.3', '70', '10.3'],
                                   ['2', '8.6', '65', '10.3'],
                                   ['3', '8.8', '63', '10.2'],
                                   ['4', '10.5', '72', '16.4'],
                                   ['5', '10.7', '81', '18.8']]


def test_should_correctly_read_csv_without_first_column():
    csv_reader = CsvReader(TEST_FILENAME, skip_first_column=True)
    assert csv_reader.dto.columns == [
        'Girth (in)', 'Height (ft)', 'Volume (ft^3)']

    assert csv_reader.dto.data == [['8.3', '70', '10.3'],
                                   ['8.6', '65', '10.3'],
                                   ['8.8', '63', '10.2'],
                                   ['10.5', '72', '16.4'],
                                   ['10.7', '81', '18.8']]
