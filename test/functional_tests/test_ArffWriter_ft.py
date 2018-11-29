import filecmp
import os

from filepy.arff_writer import ArffWriter
from filepy.dto import DTO

TEST_FILE = 'test/data/arff.txt'

columns = ['first', 'second', 'third']
data = [['1.0', '2.0', '3.0'], ['4.0', '5.0', '6.0']]
TEST_DTO = DTO(data=data, columns=columns)


def test_should_correctly_save_file():
    correct_file = 'test/data/arff_files/ft_arffWriter_1.arff'
    arff_writer = ArffWriter(path_to_file=TEST_FILE)

    arff_writer.write(TEST_DTO)
    assert filecmp.cmp(TEST_FILE, correct_file)
    os.remove(TEST_FILE)


def test_should_corectly_save_file_with_non_default_delimiter():
    correct_file = 'test/data/arff_files/ft_arffWriter_2.arff'
    arff_writer = ArffWriter(path_to_file=TEST_FILE, delimiter=' ')

    arff_writer.write(TEST_DTO)
    assert filecmp.cmp(TEST_FILE, correct_file)
    os.remove(TEST_FILE)
