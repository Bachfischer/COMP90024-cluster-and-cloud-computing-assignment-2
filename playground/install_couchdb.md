## Installation of CouchDB

Enable Apache CouchDB package repository
```
echo "deb https://apache.bintray.com/couchdb-deb bionic main" | sudo tee -a /etc/apt/sources.list.d/couchdb.list
```

Install CouchDB repository key
```
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 8756C4F765C9AC3CB6B85D62379CE192D401AB61

Alternative:
gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 8756C4F765C9AC3CB6B85D62379CE192D401AB61 
gpg --export 8756C4F765C9AC3CB6B85D62379CE192D401AB61 > couchdb.key
sudo apt-key add ../couchdb.key
```

Update the repository and install CouchDB
```
sudo apt update
sudo apt install -y couchdb
```

Create a special couchdb user for CouchDB
```
adduser --system --shell /bin/bash --group --gecos "CouchDB Administrator" couchdb
```

Start CouchDB
```
sudo service couchdb start
```

Make sure to expose port 5984 (CouchDB admin port)! (but issues with updating security groupss)

Connect via web http://172.26.132.56:5984/_utils