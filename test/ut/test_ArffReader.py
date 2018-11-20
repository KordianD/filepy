import pytest

from filepy.ArffReader import ArffReader

TEST_FILENAME = 'test'


@pytest.fixture
def arff_reader():
    return ArffReader(TEST_FILENAME)


def test_when_line_contains_data_declaration_is_line_containing_declaration_should_return_true(arff_reader):
    line_with_data_declaration = '@data'
    assert arff_reader.is_line_containing_declaration(line_with_data_declaration, 'data')


def test_when_line_is_empty_is_line_containing_declaration_should_return_false(arff_reader):
    empty_line = ""
    assert not arff_reader.is_line_containing_declaration(empty_line, 'data')
