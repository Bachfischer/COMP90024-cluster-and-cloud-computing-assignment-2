#!/usr/bin/env python
#
# Part of Assignment 2 - COMP90024 course at The University of Melbourne 
#
# Cluster and Cloud Computing - Team 24 
# 
# Authors: 
#
#  * Liam Simon (Student ID: 1128453)
#  * Rejoy Benjamin (Student ID: 1110935)
#  * Parikshit Diwan (Student ID: 1110497)
#  * Colin McLean (Student ID: 1139518)
#  * Matthias Bachfischer (Student ID: 1133751)
#
# Location: Melbourne
#

import couchdb
import json
import time

username = "admin"
password = "data-miner!"

geojsondb = couchdb.Database("http://172.26.133.36:5984/geo_json")
geojsondb.resource.credentials = (username, password)
resultdb = couchdb.Database("http://172.26.133.36:5984/twitter_result_db")
resultdb.resource.credentials = (username, password)
join_db = couchdb.Database("http://172.26.133.36:5984/postcode_aurin")
join_db.resource.credentials = (username, password)

def main():
    while(True):
        postcodes=dict()

        aurin=[]

        joint=[]
        print("starting")
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
                ratio = float(suburb_prop['0total_ins'])/postcodes.get(postcode)
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
            if pc["_id"] in join_db:
                db_pc = join_db[pc["_id"]]
                pc["_rev"] = db_pc['_rev']
                join_db[pc["_id"]] = pc
            else:
                del pc['_rev']
                join_db[pc["_id"]] = pc
        print("updated db")
        print("sleeping")
        time.sleep(300)

if __name__ == "__main__":
    main()
