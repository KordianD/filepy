from filepy.arff_reader import ArffReader
from filepy.csv_writer import CsvWriter
from filepy.file_converter import convert
import filecmp
import os

ARFF_TEST_FILE = 'test/data/arff_files/reader_example_1.arff'
CSV_TEST_FILE = 'test/data/arff_to_csv.csv'
CSV_CORRECT_FILE = 'test/data/csv_files/test_arff_to_csv.csv'


def test_should_correctly_convert_arff_to_csv():
    arff_reader = ArffReader(ARFF_TEST_FILE)
    csv_writer = CsvWriter(CSV_TEST_FILE)

    convert(input_reader=arff_reader, output_writer=csv_writer)

    assert filecmp.cmp(CSV_TEST_FILE, CSV_CORRECT_FILE)
    os.remove(CSV_TEST_FILE)
