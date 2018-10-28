import pandas as pd;
from sklearn import svm;
from sklearn.cross_validation import cross_val_score;

#dataset
data=pd.read_csv("../datasets/csvFiles/shuffledDataset.csv");

#Temp Model
model=svm.SVC(kernel="rbf",C=1,gamma=0.2)

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

#4 Fold Cross Validation
validationScores=cross_val_score(model,x,y,cv=4,scoring="accuracy");

#Warnings <-----> Output 
for i in range(0,5):
	print;

print "Score Results"
print

print "4 Fold Cross Validation Accuracy:";
print validationScores;

print

scoreSum=0.0;
for score in validationScores:
	scoreSum+=score;

print "Average Accuracy:";
print str(scoreSum/4.0);