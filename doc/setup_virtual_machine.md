## Setup Virtual Machine

Connect to CouchDB database server (make sure you're connected to Unimelb VPN)
```
ssh -i ~/.ssh/cloud_unimelb_assignment_2_rsa ubuntu@172.26.132.56
```

To set system-wide proxy on Ubuntu, edit the file /etc/environment (with sudo permissions) and add
```
http_proxy=http://wwwproxy.unimelb.edu.au:8000/
https_proxy=http://wwwproxy.unimelb.edu.au:8000/
no_proxy="localhost,127.0.0.1,localaddress,172.16.0.0/12,.melbourne.rc.nectar.org.au,.storage.unimelb.edu.au,.cloud.unimelb.edu.au"
HTTP_PROXY=http://wwwproxy.unimelb.edu.au:8000/
HTTPS_PROXY=http://wwwproxy.unimelb.edu.au:8000/
```

To make sudo use the correct proxy environment variables, run the following commands:
```
sudo update-alternatives --config editor
```
and select the number that corresponds with the choice you would like to make.

Source the file to implement the changes:
```
 ~/.bashrc
```

Preserver proxy environment variables in sudo by running `sudo visudo`
```
Defaults env_keep += "ftp_proxy http_proxy https_proxy no_proxy"
```