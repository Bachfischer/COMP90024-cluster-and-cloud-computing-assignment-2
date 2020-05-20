import couchdb
import logging
import json


username = "admin"
password = "data-miner!"
logger = logging.getLogger('db join')
logger.setLevel(logging.DEBUG)

logger.info("init creds")
geojsondb = couchdb.Database("http://172.26.132.56:5984/geo_json")
geojsondb.resource.credentials = (username, password)
resultdb = couchdb.Database("http://172.26.132.56:5984/result_db")
resultdb.resource.credentials = (username, password)
join_db = couchdb.Database("http://172.26.132.56:5984/aurin_postcode")
join_db.resource.credentials = (username, password)
logger.info("Connected")


postcodes=dict()

aurin=[]

joint=[]

#get map/reduce out of postcodes attached tweet
for item in resultdb.view('count/count_postcode',group=True,group_level=1):
    postcodes[item.key] = item.value

#get all suburbs from aurin database
for item in geojsondb.view('get_all/id'):
    aurin.append(item)

#combine the count and suburb data
for suburb in aurin:
    postcode = suburb.value['_id']
    if postcode in postcodes:
        suburb_prop = suburb.value['properties']
        #installations / tweet count
        ratio = postcodes.get(postcode)/suburb_prop['0total_ins']
        suburb_prop['ratio'] = ratio
        suburb_prop['tweet_count'] = postcodes.get(postcode)
        suburb.value['properties'] = suburb_prop
        joint.append(suburb.value)
        postcodes.pop(postcode)
    else:
        suburb_prop = suburb.value['properties']
        #installations / tweet count
        suburb_prop['ratio'] = -1
        suburb.value['properties'] = suburb_prop
        joint.append(suburb.value)
        postcodes.pop(postcode)



print(joint)


