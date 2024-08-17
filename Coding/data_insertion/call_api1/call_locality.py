import requests
import json
import csv
#// POST API
url ='http://127.0.0.1:8080/api/localitydescription'
#// Reading JSON file
with open('locality_datajson.json','r')as infile:
    indata = json.load(infile)
output =[]
#//Calling API POST method on requests one by one
for data in indata:
    r= requests.post(url, json=data)
    print(r, r.text)
