from filepy.ArffWriter import ArffWriter
from filepy.DTO import DTO
import filecmp
import os

TEST_FILE = 'test/at/data/output/arff.txt'
CORRECT_FILE = 'test/at/data/output/correct_arff.txt'

columns = ['first', 'second', 'third']
data = [['1.0', '2.0', '3.0'], ['4.0', '5.0', '6.0']]
TEST_DTO = DTO(data=data, columns=columns)


def test_should_correctly_save_file():
    arff_writer = ArffWriter(path_to_file=TEST_FILE)
    arff_writer.dto = TEST_DTO

    arff_writer.write()
    assert filecmp.cmp(TEST_FILE, CORRECT_FILE)
    os.remove(TEST_FILE)