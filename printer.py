def printResult(test_y, predictions):
    from sklearn.metrics import confusion_matrix, accuracy_score
    print("Precison : ", accuracy_score(test_y, predictions)*100);
    cm = confusion_matrix(test_y, predictions)
    #print(cm)