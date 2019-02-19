#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


### Default Values of SVC Parameters
#kernel = "rbf"
#gamma = "auto_deprecated" 
#C = 1.0

#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]

#myClassifier = SVC(kernel = "linear")
#myClassifier = SVC(kernel = "rbf")
#myClassifier = SVC(C=10.0,kernel = "rbf")
#myClassifier = SVC(C=100.0,kernel = "rbf")
#myClassifier = SVC(C=1000.0,kernel = "rbf")
myClassifier = SVC(C=10000.0,kernel = "rbf")

#startTrainingTime = time()
myClassifier.fit(features_train,labels_train)
#print "Training time: ",round(time()-startTrainingTime,3),"seconds"

#startPredictionTime = time()
myPredictions = myClassifier.predict(features_test)
#print "Prediction time: ",round(time() - startPredictionTime,3),"seconds"

#accuracy = accuracy_score(labels_test,myPredictions)
#print "Accuracy is: ",accuracy

"""
indexList = [10,26,50]
for index in indexList:
	predicted = myPredictions[index]

	if predicted == 0:
		authorPredicted = "Sara"
	elif predicted == 1:
		authorPredicted = "Chris"
	else:
		raise ValueError

	print "The predicted author for element ",index," of test data is: "+authorPredicted," with label: ",predicted
"""

print "No. of emails in the test data, predicted to be in the \"Chris \" (1) class = ", list(myPredictions).count(1)
#########################################################


