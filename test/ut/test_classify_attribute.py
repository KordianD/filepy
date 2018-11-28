from filepy.analyse_helper import classify_attribute


def test_should_classify_as_numeric_when_number_passed():
    number = 10
    assert classify_attribute(number) == "numeric"


def test_should_classify_as_string_when_string_passed():
    string = "test"
    assert classify_attribute(string) == "string"
