from filepy.arff_reader import ArffReader
from filepy.arff_writer import ArffWriter
from filepy.file_converter import convert
import filecmp
import os

ARFF_TEST_FILE = 'test/data/arff_files/arff_to_arff.arff'
ARFF_OUTPUT_TEST_FILE = 'test/data/arff_to_arff.arff'
ARFF_CORRECT_FILE = 'test/data/arff_files/arff_to_arff.arff'


def test_should_correctly_convert_arff_to_arff():
    arff_reader = ArffReader(ARFF_TEST_FILE)
    arff_writer = ArffWriter(ARFF_OUTPUT_TEST_FILE)

    convert(input_reader=arff_reader, output_writer=arff_writer)

    assert filecmp.cmp(ARFF_OUTPUT_TEST_FILE, ARFF_CORRECT_FILE)
    os.remove(ARFF_OUTPUT_TEST_FILE)
