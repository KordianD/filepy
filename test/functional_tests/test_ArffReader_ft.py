from filepy.arff_reader import ArffReader

TEST_FILENAME = 'test/data/arff_files/reader_example_1.arff'


def test_correctly_read_matrix_with_column_labels():
    arff_reader = ArffReader(TEST_FILENAME)
    assert arff_reader.dto.additional['relation'] == 'iris'
    assert arff_reader.dto.additional['attributes'] == ['NUMERIC', 'NUMERIC', 'NUMERIC', 'NUMERIC',
                                                        '{Iris-setosa,Iris-versicolor,Iris-virginica}']

    assert arff_reader.dto.data == [['5.0', '3.4', '1.5', '0.2', 'Iris-setosa'],
                                    ['4.4', '2.9', '1.4', '0.2', 'Iris-setosa'],
                                    ['4.9', '3.1', '1.5', '0.1', 'Iris-setosa']]
