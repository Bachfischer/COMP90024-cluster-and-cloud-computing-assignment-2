import csv,json
import couchdb
import pandas as pd

server = couchdb.Server("http://172.26.133.36:5984")
server.resource.credentials = ("admin", "data-miner!")
db = server['geo_json']
print("connected")

json_file = "shapes/sydney_postcodes.json"
with open(json_file) as f:
    json_obj = json.load(f)

city_data = pd.read_csv("sydneyAggregatedAurinData.csv")

def get_postcode(i):
    postcode = i['properties']['postcode']
    if postcode == "2000":
        postcode = "12000"
    elif postcode == "3000":
        postcode = "13000"
    elif postcode == "4000":
        postcode = "14000"
    elif postcode == "5000":
        postcode = "15000"
    elif postcode == "6000":
        postcode = "16000"
    return postcode

def get_installations(postcode):
    row = city_data.loc[city_data[' postcode'] == int(postcode)]
    val = row.values[0]
    return val[2]


count = 0
for entry in json_obj:
    if len(json_obj[entry]) > 40:
        for i in json_obj[entry]:
            postcode = i['properties']['postcode']
            if postcode == "6161":
                continue
            installations = get_installations(postcode)
            postcode = get_postcode(i)
            i['_id'] = postcode
            i['properties']['0total_ins'] = str(installations)

count = 0
for entry in json_obj:
    if len(json_obj[entry]) > 50:
        for i in json_obj[entry]:
            if i['properties']['postcode'] == "6161":
                continue
            db.save(i)
            count+= 1
            print("wrote the " + str(count) + "th element" )
    #print("wrote the " + str(count) + "th element" )
