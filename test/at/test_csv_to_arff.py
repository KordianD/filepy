import filecmp
import os

from filepy.arff_writer import ArffWriter
from filepy.csv_reader import CsvReader
from filepy.file_converter import convert

CSV_TEST_FILE = 'test/data/csv_files/at_csv_to_arff_1_input.csv'
ARFF_CORRECT_FILE = 'test/data/arff_files/at_csv_to_arff_1_output.arff'
ARFF_TEST_FILE = 'test/data/test_csv_to_arff.arff'


def test_should_correctly_convert_csv_to_arff():
    csv_reader = CsvReader(
        CSV_TEST_FILE, first_line_column_names=False, delimiter=r',\s*')
    arff_writer = ArffWriter(ARFF_TEST_FILE, delimiter=' ')

    convert(input_reader=csv_reader, output_writer=arff_writer)

    assert filecmp.cmp(ARFF_TEST_FILE, ARFF_CORRECT_FILE)
    os.remove(ARFF_TEST_FILE)
