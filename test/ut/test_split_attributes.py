from filepy.analyse_helper import split_attributes


def test_should_return_correctly_split_attributes_when_columns_are_passed_in_parentheses():
    line_with_parentheses = '@attribute age 			{young, pre-presbyopic, presbyopic}'
    assert split_attributes(line_with_parentheses) == (
        'age', '{young, pre-presbyopic, presbyopic}')
