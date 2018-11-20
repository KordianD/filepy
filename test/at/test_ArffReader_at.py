from filepy.ArffReader import ArffReader

TEST_FILENAME = 'test/at/data/arff_files/with_matrix_10_x_10_and_column_names.arff'


def test_correctly_read_matrix_with_column_labels():
    arff_reader = ArffReader(TEST_FILENAME)
    assert arff_reader.relation == 'iris'
    assert arff_reader.attributes == [('sepallength', 'NUMERIC'), ('sepalwidth', 'NUMERIC'),
                                      ('petallength', 'NUMERIC'),
                                      ('petalwidth', 'NUMERIC'),
                                      ('class', '{Iris-setosa,Iris-versicolor,Iris-virginica}')]
