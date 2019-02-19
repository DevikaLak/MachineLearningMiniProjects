#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

print "Number of people in this dataset is: ",len(enron_data)
print "Number of features available for each person is: ",len(enron_data["SKILLING JEFFREY K"])

POICount = 0

for person in enron_data.keys():
	if enron_data[person]["poi"]:
		POICount+=1

print "Number of POIs in E+F dataset is: ",POICount
print "Total number of POIs in '../final_project/poi_names.txt' is: 35"
print "Total value of stock belonging to James Prentice is: ",enron_data["PRENTICE JAMES"]["total_stock_value"]
print "Number of emails from Wesley Colwell to POIs is: ",enron_data["COLWELL WESLEY"]['from_this_person_to_poi']
print "Value of stock options excercised by Jeffery K Skilling is: ",enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

cxos = ["SKILLING JEFFREY K", "LAY KENNETH L","FASTOW ANDREW S"]
maxTotalPayment = 0
for key in cxos:
	maxTotalPayment = max(maxTotalPayment, enron_data[key]['total_payments'])

print "The maximum total payment is: ",maxTotalPayment

salaryCount = 0
emailAddressCount = 0
totalPaymentUnknownCount = 0
POIstotalPaymentUnknownCount = 0
for person in enron_data.keys():
	if enron_data[person]['salary'] != 'NaN':
		salaryCount+=1

	if enron_data[person]['email_address'] != 'NaN':
		emailAddressCount+=1

	if enron_data[person]['total_payments'] == 'NaN':
		totalPaymentUnknownCount+=1
		if enron_data[person]['poi'] :
			POIstotalPaymentUnknownCount+=1

print "Number of persons with quantified salary is: ",salaryCount
print "Number of persons with known email address is: ",emailAddressCount
print "Number of persons with total payment as 'NaN' is: ", totalPaymentUnknownCount," which is: ",100*totalPaymentUnknownCount/(len(enron_data))," % of total dataset"
print "Number of POIs with total payment as 'NaN' is: ", POIstotalPaymentUnknownCount," which is: ",100*POIstotalPaymentUnknownCount/(POICount)," % of total POIs"
