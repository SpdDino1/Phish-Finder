import csv,random;

#fiel openings
try:
	sourceSet = open("./csvFiles/shuffledDataset.csv","r");
except:
	sourceSet = open("./csvFiles/updatedDatasetSlashed.csv","r");

allRows=csv.reader(sourceSet);

#push to list
dataList=list();

for row in allRows:
	dataList.append(row);

#pop and get tags
csvTags=dataList.pop(0);

#shuffle
for i in range(0,1000):
	a=random.randint(0,len(dataList)-1);
	b=random.randint(0,len(dataList)-1);

	dataList[a],dataList[b]=dataList[b],dataList[a];

#write to file
shuffledSet = open("./csvFiles/shuffledDataset.csv","w");
shuffledSetWriter=csv.writer(shuffledSet);
shuffledSetWriter.writerow(csvTags);

for row in dataList:
	shuffledSetWriter.writerow(row);
	shuffledSet.flush();

sourceSet.close();
shuffledSet.close();