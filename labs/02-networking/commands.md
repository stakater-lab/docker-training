### Step 1

Create a user-defined bridge network

`docker network create mybridge --subnet=192.19.0.0/16`

List networks

`docker network ls`

### Step 2

Run backend and frontend containers with the name flag and attach them to our new bridge network

`docker run -d --name=hello-world-back --network mybridge stakaterlabs/hello-world-back`

`docker run -d --name=hello-world-front --network mybridge stakaterlabs/hello-world-front`

### Step 3

Check the frontend container IP

`docker inspect --format='{{.NetworkSettings.Networks.mybridge.IPAddress}}' hello-world-front`

Call the frontend application endpoint with curl or open in browser

`curl http://<ip-address>:5000/`

### Step 4

Lookup the records on the nameserver

`docker exec hello-world-front cat /etc/resolv.conf`

`docker exec hello-world-front nslookup hello-world-back <nameserver-ip>`

`docker exec hello-world-back nslookup hello-world-front <nameserver-ip>`

### Step 5

#### Step 5a

Stop and remove the backend container

`docker stop hello-world-back && docker rm hello-world-back`

#### Step 5b

Rerun backend container again on the mybridge network but with the IP specified

`docker run -d --name=hello-world-back --network=mybridge --ip=192.19.1.1 stakaterlabs/hello-world-back`

#### Step 5c

Check the IP address of the backend

`docker inspect --format='{{.NetworkSettings.Networks.mybridge.IPAddress}}' hello-world-back`

#### Step 5d

Call the frontend application endpoint with curl or open in browser to recheck that it is still working

`curl http://<ip-address>:5000/`


#### Step 5e

Lookup the records on the nameserver for the backend container

`docker exec hello-world-front cat /etc/resolv.conf`

`docker exec hello-world-front nslookup hello-world-back <nameserver-ip>`


