from filepy.ArffReader import ArffReader


def test_when_line_contains_data_declaration_is_line_containing_declaration_should_return_true():
    line_with_data_declaration = '@data'
    assert ArffReader._is_line_containing_declaration(
        line_with_data_declaration, 'data')


def test_when_line_is_empty_is_line_containing_declaration_should_return_false():
    empty_line = ""
    assert not ArffReader._is_line_containing_declaration(empty_line, 'data')
