from filepy.analyse_helper import extract_filename_from_path_to_file


def test_should_return_correct_filename_when_absolute_path_passed():
    test_path = 'test/data/arff_files/writer_example_1.arff'
    assert extract_filename_from_path_to_file(
        test_path) == 'writer_example_1.arff'


def test_should_return_correct_filename_when_only_filename_passed():
    test_path = 'only_filename_passed.arff'
    assert extract_filename_from_path_to_file(
        test_path) == 'only_filename_passed.arff'
