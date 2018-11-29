from filepy.analyse_helper import create_attributes_to_save
from filepy.dto import DTO


def test_should_return_numeric_attributes():
    columns: list = ['first', 'second', 'third']
    data: list = [['1.0', '2.0', '3.0'], ['4.0', '5.0', '6.0']]
    test_dto: DTO = DTO(data=data, columns=columns)
    attributes: str = create_attributes_to_save(test_dto)
    assert attributes == "@attribute first numeric\n@attribute second numeric\n@attribute third numeric\n"


def test_should_return_numeric_and_string_attributes():
    columns: list = ['first', 'second', 'third']
    data: list = [['Text', '2.0', 'Second_text'], ['T', '5.0', 'Test']]
    test_dto: DTO = DTO(data=data, columns=columns)
    attributes: str = create_attributes_to_save(test_dto)
    assert attributes == "@attribute first string\n@attribute second numeric\n@attribute third string\n"


def test_should_return_numeric_attributues_and_columns_ordered_by_number_when_dto_without_columns_passed():
    columns: list = []
    data: list = [['Text', '2.0', 'Second_text'], ['T', '5.0', 'Test']]
    test_dto: DTO = DTO(data=data, columns=columns)
    attributes: list = create_attributes_to_save(test_dto)
    assert attributes == "@attribute col0 string\n@attribute col1 numeric\n@attribute col2 string\n"
