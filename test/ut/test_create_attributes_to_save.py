from filepy.analyse_helper import create_attributes_to_save
from filepy.dto import DTO


def test_should_return_numeric_attributes():
    columns = ['first', 'second', 'third']
    data = [['1.0', '2.0', '3.0'], ['4.0', '5.0', '6.0']]
    TEST_DTO = DTO(data=data, columns=columns)
    attributes = create_attributes_to_save(TEST_DTO)
    assert attributes == "@attribute first numeric\n@attribute second numeric\n@attribute third numeric\n"


def test_should_return_numeric_and_string_attributes():
    columns = ['first', 'second', 'third']
    data = [['Text', '2.0', 'Second_text'], ['T', '5.0', 'Test']]
    TEST_DTO = DTO(data=data, columns=columns)
    attributes = create_attributes_to_save(TEST_DTO)
    assert attributes == "@attribute first string\n@attribute second numeric\n@attribute third string\n"
