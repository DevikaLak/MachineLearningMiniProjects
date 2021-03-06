#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
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
from sklearn import tree
from sklearn.metrics import accuracy_score

print "No. of features is: ",len(features_train[0])

myClassifier = tree.DecisionTreeClassifier(min_samples_split=40)

startTrainingTime = time()
myClassifier.fit(features_train,labels_train)
print "Training time is: ",round(time()-startTrainingTime,3),"seconds"

startPredictionTime = time()
myPredictions = myClassifier.predict(features_test)
print "Prediction time is: ",round(time()-startPredictionTime,3),"seconds"

accuracy = accuracy_score(labels_test,myPredictions)
print "Accuracy is: ",accuracy


#########################################################


