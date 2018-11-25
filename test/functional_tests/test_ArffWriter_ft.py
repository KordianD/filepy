from filepy.arff_writer import ArffWriter
from filepy.dto import DTO
import filecmp
import os

TEST_FILE = 'test/functional_tests/data/arff.txt'
TEST_FILENAME = 'arff.txt'
CORRECT_FILE = 'test/functional_tests/data/arff_files/writer_example_1.arff'

columns = ['first', 'second', 'third']
data = [['1.0', '2.0', '3.0'], ['4.0', '5.0', '6.0']]
TEST_DTO = DTO(data=data, columns=columns)


def test_should_correctly_save_file():
    arff_writer = ArffWriter(path_to_file=TEST_FILE)

    arff_writer.write(TEST_DTO)
    assert filecmp.cmp(TEST_FILE, CORRECT_FILE)
    os.remove(TEST_FILE)


def test_should_correctly_save_file_with_only_filename():
    arff_writer = ArffWriter(path_to_file=TEST_FILENAME)

    arff_writer.write(TEST_DTO)
    assert filecmp.cmp(TEST_FILENAME, CORRECT_FILE)
    os.remove(TEST_FILENAME)
