import couchdb
import json
import time

username = "admin"
password = "data-miner!"

geojsondb = couchdb.Database("http://172.26.133.36:5984/geo_json")
geojsondb.resource.credentials = (username, password)
resultdb = couchdb.Database("http://172.26.133.36:5984/twitter_result_db")
resultdb.resource.credentials = (username, password)
join_db = couchdb.Database("http://172.26.133.36:5984/aurin_postcode")
join_db.resource.credentials = (username, password)

postcodes=dict()

aurin=[]

joint=[]
while True{
#get map/reduce out of postcodes attached tweet
    for item in resultdb.view('count/count_postcode',group=True,group_level=1):
        print(item)
        postcodes[item.key] = item.value
    print(postcodes)
#get all suburbs from aurin database
    for item in geojsondb.view('get_all/id'):
        aurin.append(item)

#combine the count and suburb data
    for suburb in aurin:
        postcode = suburb.value['_id']
        if postcode in postcodes:
            suburb_prop = suburb.value['properties']
            #installations / tweet count
            
            print(postcodes.get(postcode),float(suburb_prop['0total_ins']))
            ratio = postcodes.get(postcode)/float(suburb_prop['0total_ins'])
            suburb_prop['ratio'] = ratio
            suburb_prop['tweet_count'] = postcodes.get(postcode)
            suburb.value['properties'] = suburb_prop
            joint.append(suburb.value)
        else:
            suburb_prop = suburb.value['properties']
            #ratio is 0 if the postcode doesnt exist
            suburb_prop['ratio'] = 0 
            suburb.value['properties'] = suburb_prop
            joint.append(suburb.value)

    for pc in joint:
        db_pc = join_db[pc["_id"]]
        if db_pc:
            pc["_rev"] = db_pc['_rev']
            join_db[pc["_id"]] = pc
        else:
            del pc['_rev']
            join_db[pc["_id"]] = pc

}
