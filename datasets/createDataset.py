import csv;

sourceCsv = open("../dataset.csv","r");
destCsv = open("./unshuffledDataset.csv","w");

csvTags=["url","length","dotCount","slashCount","numberCount","underscoreCount","hyphenCount","ampersandCount","equalCount","status"];
destCsvWriter = csv.DictWriter(destCsv,fieldnames = csvTags);
destCsvWriter.writerow({
	"url":"url",
	"length":"length",
	"dotCount":"dotCount",
	"slashCount":"slashCount",
	"numberCount":"numberCount",
	"underscoreCount":"underscoreCount",
	"hyphenCount":"hyphenCount",
	"ampersandCount":"ampersandCount",
	"equalCount":"equalCount",
	"status":"status"
});
destCsv.flush();

allRows=csv.DictReader(sourceCsv);

urlData=dict();

for row in allRows:
	url=row["Phishing URL"];

	urlData["url"]=url;
	urlData["status"]=row["status"];
	urlData["length"]=row["URL_Size"];
	urlData["hyphenCount"]=row["NH"];
	urlData["dotCount"]=row["ND"];
	urlData["numberCount"]=row["NNC"];

	urlData["slashCount"]=url.count("/");
	urlData["underscoreCount"]=url.count("_");
	urlData["ampersandCount"]=url.count("&");
	urlData["equalCount"]=url.count("=");

	destCsvWriter.writerow(urlData);
	destCsv.flush();
	urlData.clear();

destCsv.close();
sourceCsv.close();