import couchdb

from geopy import Point
from geopy.geocoders import Nominatim

geolocator = Nominatim(timeout=10)

username = "admin"
password = "data-miner!"
cdb = couchdb.Database("http://172.26.132.56:5984/new_twitter_examples")
cdb.resource.credentials = (username, password)
resultdb = couchdb.Database("http://172.26.132.56:5984/result_db")
resultdb.resource.credentials = (username, password)
count = 0
doc_id = []
document_id = []
mango = {'selector': {'Flag': 'N'}, 'limit': 10000000000}

for dbname in cdb.find(mango):
    docu_id = dbname['_id']
    doc_id.append(docu_id)


def getZipCode(longfield, latfield):
    location = geolocator.reverse(Point(latfield, longfield))
    try:
        postcode = location.raw['address']['postcode']
        return postcode
    except KeyError:
        pass
        postcode = "Nil"
        return postcode


for document_id in doc_id:
    try:
        if not "design" in document_id:
            count = count + 1
            latitude = str(cdb[document_id]['latitude'])
            longitude = str(cdb[document_id]['longitude'])
            zipcode = getZipCode(longitude, latitude)
            doc = cdb[document_id]
            if not "Nil" in zipcode:
                doc['Postcode'] = str(zipcode)
                del doc['_id']
                del doc['_rev']
                resultdb.save(doc)
                print("Result DB updated")
            else:
                print("ZipCode not found ... Moving to next document.")
        updatingFlag = cdb[document_id]
        updatingFlag['Flag'] = "Y"  # Updating Flag in Raw DB
        cdb.save(updatingFlag)  # Saving document in Raw DB
    except TypeError:
        pass
