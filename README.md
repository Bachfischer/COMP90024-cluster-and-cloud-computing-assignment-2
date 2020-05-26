# Cluster and Cloud Computing - Assignment 2 (Team 24)
This repository contains the source code for assignment 2 of the COMP90024 Cluster and Cloud Computing course at the University of Melbourne.

The system can be accessed via the following URL: 

**Web App:** 

[Environmental Sustainability Tweet Analysis](http://172.26.130.40/) (requires active connection Unimelb VPN)

**YouTube:**

[Walkthrough of visualization tool](https://youtu.be/7oCPjouVqUs) 


### Submission Details

**Team members:**

- Matthias Bachfischer (Student ID: 1133751)

- Liam Simon (Student ID: 1128453)

- Rejoy Benjamin (Student ID: 1110935)

- Colin McLean (Student ID: 1139518)

- Parikshit Diwan (Student ID: 1110497)

**Tean location:** Melbourne


## Project structure

* `analytics/` -- Source code for processing of tweet data (conversion of GPS to postcodes)
* `data/` -- Dataset and scripts for processing of AURIN Clean Energy Regulator dataset
* `deployment/` -- Ansible scripts for orchestration of cloud infrastructure and deployment of app code 
* `doc/` -- Documentation and implementation notes
* `playground/` -- Random stuff
* `twitter-harvester/` -- Source code for twitter harvester scripts
* `web/` -- Source code for web-based visualization frontend

## System architecture

The system architecture designed for this project is deployed on the [University of Melbourne Research Cloud](https://dashboard.cloud.unimelb.edu.au/). It makes use of various technologies such as [Ansible](https://www.ansible.com), [Docker](https://www.docker.com) and [Apache CouchDB](https://couchdb.apache.org). 

For further information, please refer to the project report attached to this submission.
