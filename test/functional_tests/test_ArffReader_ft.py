from filepy.arff_reader import ArffReader


def test_correctly_read_matrix_with_column_labels():
    test_filename = 'test/data/arff_files/ft_arffReader_1.arff'
    arff_reader = ArffReader(test_filename)
    assert arff_reader.dto.additional['relation'] == 'iris'
    assert arff_reader.dto.additional['attributes'] == ['NUMERIC', 'NUMERIC', 'NUMERIC', 'NUMERIC',
                                                        '{Iris-setosa,Iris-versicolor,Iris-virginica}']

    assert arff_reader.dto.data == [['5.0', '3.4', '1.5', '0.2', 'Iris-setosa'],
                                    ['4.4', '2.9', '1.4', '0.2', 'Iris-setosa'],
                                    ['4.9', '3.1', '1.5', '0.1', 'Iris-setosa']]


def test_correctly_read_when_comments_are_put_between_data_and_data_attribute():
    test_filename = 'test/data/arff_files/ft_arffReader_2.arff'
    arff_reader = ArffReader(test_filename)
    assert arff_reader.dto.additional['relation'] == 'contact-lenses'
    assert arff_reader.dto.additional['attributes'] == ['{young, pre-presbyopic, presbyopic}', '{myope, hypermetrope}',
                                                        '{no, yes}', '{reduced, normal}',
                                                        '{soft, hard, none}']

    assert arff_reader.dto.data == [['young', 'myope', 'no', 'reduced', 'none'],
                                    ['young', 'myope', 'no', 'normal', 'soft'],
                                    ['young', 'myope', 'yes', 'reduced', 'none']]
