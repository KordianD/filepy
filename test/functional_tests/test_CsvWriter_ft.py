import filecmp
import os

from filepy.csv_writer import CsvWriter
from filepy.dto import DTO

TEST_FILE = 'test/data/csv.txt'

columns = ['first', 'second', 'third']
data = [['1.0', '2.0', '3.0'], ['4.0', '5.0', '6.0']]
TEST_DTO = DTO(data=data, columns=columns)


def test_should_correctly_save_file():
    correct_file = 'test/data/csv_files/ft_csvWriter_1.csv'
    csv_writer = CsvWriter(path_to_file=TEST_FILE)

    csv_writer.write(TEST_DTO)
    assert filecmp.cmp(TEST_FILE, correct_file)
    os.remove(TEST_FILE)


def test_should_corectly_save_file_with_non_default_delimiter():
    correct_file = 'test/data/csv_files/ft_csvWriter_2.csv'
    csv_writer = CsvWriter(path_to_file=TEST_FILE, delimiter=' ')

    csv_writer.write(TEST_DTO)
    assert filecmp.cmp(TEST_FILE, correct_file)
    os.remove(TEST_FILE)
