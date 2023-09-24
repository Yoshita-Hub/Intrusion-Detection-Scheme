import pandas as pd
import numpy as np

sample_number = 50000
sample_test_ratio = 20000

if __name__ == '__main__':
    #http://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html
    data = pd.read_csv('data/corrected1')
    featureNameArray = pd.read_csv('data/kddcup.names.txt', header=None).values.ravel()

    data.columns = featureNameArray

    #print(featureNameArray)

    from preprocessing.KDD import myLabelEncoder
    encoder = myLabelEncoder()
    data = encoder.encode(data)

    from preprocessing.KDD import filter
    data = filter(data, 0.1)
    data = data.sample(sample_number)
    X = data.iloc[:, 0:data.shape[1] - 1].values
    y = data.loc[:, "type"].values

    # construct test data 1, 2(split)
    from sklearn.model_selection import train_test_split
    X_train, X_test_data, y_train, y_test_data = train_test_split(X, y, test_size=sample_test_ratio)

    X_test_1, X_test_2, y_test_1, y_test_2 = train_test_split(X_test_data, y_test_data, test_size=5000)
    X_test_1, X_test_3, y_test_1, y_test_3 = train_test_split(X_test_1, y_test_1, test_size=5000)
    X_test_list = [X_test_1, X_test_2, X_test_3]
    y_test_list = [y_test_1, y_test_2, y_test_3];

    print("---------------")
    print("train : ", len(X_train))
    for index in range(0, len(X_test_list)) :
        print("test %d : %s" % (index, len(X_test_list[index])))

    # X_train = [
    #     [2, 0],
    #     [0, 2],
    #     [2, 2],
    #     [3, 3],
    #     [0, 0],
    #     [-1, 2]
    # ]
    # y_train = [1,1,1,1,0,0]
    # X_test_list = [[[10,1],[2,3],[-5,-5]]]
    # y_test_list = [[1,1,0]]

    # Conventional SVM
    print("------Conventional Training Start-----")
    from svm.conventionalSVM import ConventionalSVM
    csvm = ConventionalSVM()
    csvm.train(X_train, y_train)

    print("------Conventional Training Done-----")

    # Conventional test
    from printer import printResult

    for index in range(0, len(X_test_list)):
        csvm_predictions = csvm.test(X_test_list[index])
        printResult(y_test_list[index], csvm_predictions)

    print("------Conventional Test Done-----")

