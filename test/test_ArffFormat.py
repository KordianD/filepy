import pytest

from filepy.ArffFormat import ArffFormat

TEST_FILENAME = 'test'


@pytest.fixture
def arff_format():
    return ArffFormat(TEST_FILENAME)


def test_when_line_contains_data_declaration_is_line_containing_declaration_should_return_true(arff_format):
    line_with_data_declaration = '@data'
    assert arff_format.is_line_containing_declaration(line_with_data_declaration, 'data')


def test_when_line_is_empty_is_line_containing_declaration_should_return_false(arff_format):
    empty_line = ""
    assert not arff_format.is_line_containing_declaration(empty_line, 'data')
