from filepy.analyse_helper import is_line_containing_declaration


def test_should_return_true_when_line_contains_passed_declaration():
    line = "@data"
    assert is_line_containing_declaration(line, 'data')


def test_should_return_false_when_line_does_not_contain_passed_declaration():
    line = "@test without declaration"
    assert not is_line_containing_declaration(line, 'relation')
