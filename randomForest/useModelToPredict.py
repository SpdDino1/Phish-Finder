def countDigits(stringInput):
	count=0;

	for letter in stringInput:
		if(letter.isdigit()):
			count+=1;

	return count;

import pandas as pd;
from urlparse import urlparse;
from sklearn.externals import joblib;

#Load Model
model=joblib.load("./modelDump.pkl");

#Warnings <-----> Output 
for i in range(0,5):
	print

while(True):
	inVector=[];
	inUrl=raw_input("Enter Url:");

	protocol=urlparse(inUrl)[0]
	tld=urlparse(inUrl)[1];

	inVector.append(len(tld));
	inVector.append(tld.count("."));
	inVector.append(tld.count("_"));
	inVector.append(countDigits(tld));
	inVector.append(tld.count("-"));

	path=inUrl[len(protocol+"://"+tld):]

	inVector.append(path.count("&"));
	inVector.append(path.count("="));
	inVector.append(path.count("/"));
	inVector.append(countDigits(path));

	print model.predict([inVector]);