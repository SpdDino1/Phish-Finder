def countDigits(stringInput):
	count=0;

	for letter in stringInput:
		if(letter.isdigit()):
			count+=1;

	return count;

import csv;
from urlparse import urlparse;

sourceCsv = open("/home/vikram/Downloads/top500.pages.05.18.csv","r");
destCsv = open("./csvFiles/updatedDataset.csv","a");

csvTags=["url","length","dotCount","underscoreCount","numberCountInTld","hyphenCount","ampersandCount","equalCount","slashCount","numberCountInPath","status"];
destCsvWriter = csv.DictWriter(destCsv,fieldnames = csvTags);
'''destCsvWriter.writerow({
	"url":"url",
	"length":"length",
	"dotCount":"dotCount",
	"underscoreCount":"underscoreCount",
	"numberCountInTld":"numberCountInTld",
	"hyphenCount":"hyphenCount",
	"ampersandCount":"ampersandCount",
	"equalCount":"equalCount",
	"slashCount":"slashCount",
	"numberCountInPath":"numberCountInPath",
	"status":"status"
});
destCsv.flush();'''

allRows=csv.DictReader(sourceCsv);

urlData=dict();

for row in allRows:
	url="http://"+row["URL"];
	rawUrl=urlparse(url)[1];

	urlData["url"]=row["URL"];
	urlData["status"]="legitimate";
	urlData["length"]=len(rawUrl);
	urlData["hyphenCount"]=rawUrl.count("-");
	urlData["dotCount"]=rawUrl.count(".");
	urlData["numberCountInTld"]=countDigits(rawUrl);
	urlData["underscoreCount"]=rawUrl.count("_");

	path = row["URL"][len(rawUrl):]
	urlData["slashCount"]=path.count("/");
	urlData["ampersandCount"]=path.count("&");
	urlData["equalCount"]=path.count("=");
	urlData["numberCountInPath"]=countDigits(path);

	destCsvWriter.writerow(urlData);
	destCsv.flush();
	urlData.clear();

destCsv.close();
sourceCsv.close();

