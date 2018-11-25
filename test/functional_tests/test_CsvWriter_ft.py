from filepy.csv_writer import CsvWriter
from filepy.dto import DTO
import filecmp
import os

TEST_FILE = 'test/data/csv.txt'
CORRECT_FILE = 'test/data/csv_files/writer_example_1.csv'

columns = ['first', 'second', 'third']
data = [['1.0', '2.0', '3.0'], ['4.0', '5.0', '6.0']]
TEST_DTO = DTO(data=data, columns=columns)


def test_should_correctly_save_file():
    csv_writer = CsvWriter(path_to_file=TEST_FILE)

    csv_writer.write(TEST_DTO)
    assert filecmp.cmp(TEST_FILE, CORRECT_FILE)
    os.remove(TEST_FILE)
