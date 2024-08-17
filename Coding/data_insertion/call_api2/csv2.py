import csv
import json
output =[]
#// open input file
with open('housing_data.csv','r') as f:
    reader = csv.DictReader(f)
#//appending each record in list
    for records in reader:
        output.append(records)
#// Create JSON file
with open('housing_datajson.json','w') as outfile:
    json.dump(output,outfile,sort_keys=True, indent=4)

