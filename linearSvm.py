def countDigits(stringInput):
	count=0;

	for letter in stringInput:
		if(letter.isdigit()):
			count+=1;

	return count;

import pandas as pd
from sklearn import svm
from urlparse import urlparse;

#dataset
data=pd.read_csv("./datasets/csvFiles/shuffledDataset.csv");

#Model creation + Training
model=svm.SVC(kernel="linear",C=1);
#model=svm.SVC(gamma="scale");
model.fit(data[[
	"length",
	"dotCount",
	"underscoreCount",
	"numberCountInTld",
	"hyphenCount",
	"ampersandCount",
	"equalCount",
	"slashCount",
	"numberCountInPath"
	]],
	data["status"]);

#Model Prediction
print "Model Trained!";

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