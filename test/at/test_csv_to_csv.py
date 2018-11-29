from filepy.csv_reader import CsvReader
from filepy.csv_writer import CsvWriter
from filepy.file_converter import convert
import filecmp
import os

CSV_TEST_FILE = 'test/data/csv_files/at_csv_to_csv_1_input.csv'
CSV_OUTPUT_TEST_FILE = 'test/data/csv_to_csv.csv'
CSV_CORRECT_FILE = 'test/data/csv_files/at_csv_to_csv_1_output.csv'


def test_should_correctly_convert_csv_to_csv():
    csv_reader = CsvReader(CSV_TEST_FILE, delimiter=';')
    csv_writer = CsvWriter(CSV_OUTPUT_TEST_FILE,
                           delimiter=' ', skip_writing_columns=True)

    convert(input_reader=csv_reader, output_writer=csv_writer)

    assert filecmp.cmp(CSV_OUTPUT_TEST_FILE, CSV_CORRECT_FILE)
    os.remove(CSV_OUTPUT_TEST_FILE)
