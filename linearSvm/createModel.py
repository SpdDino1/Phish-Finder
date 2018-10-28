import pandas as pd;
from sklearn import svm;
from sklearn.externals import joblib

#dataset
data=pd.read_csv("../datasets/csvFiles/shuffledDataset.csv");

#Model creation + Training
model=svm.SVC(kernel="rbf",C=1,gamma=0.2);

x=data[[
	"length",
	"dotCount",
	"underscoreCount",
	"numberCountInTld",
	"hyphenCount",
	"ampersandCount",
	"equalCount",
	"slashCount",
	"numberCountInPath"
	]];

y=data["status"];

model.fit(x,y);

joblib.dump(model,"./modelDump.pkl");

#Warnings <-----> Output 
for i in range(0,5):
	print

#Model Prediction
print "Model Built!";