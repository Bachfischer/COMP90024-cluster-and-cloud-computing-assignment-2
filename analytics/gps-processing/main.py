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
from geopy import Point
from geopy.geocoders import Nominatim
import time

geolocator = Nominatim(timeout=10)
username = "admin"
password = "data-miner!"
cdb = couchdb.Database("http://172.26.133.36:5984/twitter_raw_data")
cdb.resource.credentials = (username, password)
resultdb = couchdb.Database("http://172.26.133.36:5984/twitter_result_db")
resultdb.resource.credentials = (username, password)
mango = {'selector': {'Flag': 'N'}}

def getZipCode(longfield, latfield, geolocation_enabled):
    location = geolocator.reverse(Point(latfield, longfield))
    try:
        if geolocation_enabled.lower() == 'true':
            postcode = location.raw['address']['postcode']
            return postcode
        else:
            postcode = location.raw['address']['postcode']
            postcode = "1" + postcode
            return postcode
    except KeyError:
        pass
        postcode = "Nil"
        return postcode


def dataProcessing(couchdbdoc_id):
    try:
        if not "design" in couchdbdoc_id:
            geo_enabled = str(cdb[couchdbdoc_id]['geo_enabled'])
            latitude = str(cdb[couchdbdoc_id]['latitude'])
            longitude = str(cdb[couchdbdoc_id]['longitude'])
            zipcode = getZipCode(longitude, latitude, geo_enabled)
            doc = cdb[couchdbdoc_id]
            if not "Nil" in zipcode:
                doc['Postcode'] = str(zipcode)
                del doc['_id']
                del doc['_rev']
                resultdb.save(doc)
                print("Result DB updated")
            else:
                print("ZipCode not found ... Moving to next document.")
        updatingflag = cdb[couchdbdoc_id]
        updatingflag['Flag'] = "Y"  # Updating Flag in Raw DB
        cdb.save(updatingflag)
    except TypeError:
        pass

def main():
    doc_id = []
    while 1:
        dataset = cdb.find(mango)
        for dbname in dataset:
            docu_id = dbname['_id']
            doc_id.append(docu_id)
        if len(doc_id) == 0:
            print("Waiting for 1 minute")
            time.sleep(60)
            print("Checking Raw DB for new tweets....")
        else:
            for document in doc_id:
                dataProcessing(document)   
        doc_id = []

if __name__ == "__main__":
    main()