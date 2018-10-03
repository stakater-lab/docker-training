### Step 1

Run the docker bench security script with docker compose

`git clone https://github.com/docker/docker-bench-security.git`

`cd docker-bench-security`

`docker-compose run --rm docker-bench-security`

### Step 2

#### Step 2a

Pull the hello-world-back image on the machine

`docker pull stakaterlabs/hello-world-back`

#### Step 2b

Specify the particular check categories in the docker-compose command arguments

`docker-compose run --rm docker-bench-security "-c container_images,docker_daemon_configuration,docker_daemon_files"`

### Step 3

#### Step 3a

Edit the daemon configuration file /etc/docker/daemon.json and fix the required settings. [File contents](daemon.json)

`vi /etc/docker/daemon.json`

#### Step 3b

Restart docker daemon

`kill -SIGHUP $(pidof dockerd)`

### Step 4

Change the permissions on the daemon configuration file

`chmod 644 /etc/docker/daemon.json`

### Step 5

#### Step 5a

Edit the Dockerfile for the image. [File Contents](Dockerfile)

`git clone https://github.com/stakater-lab/docker-training.git`

`cd docker-training/labs/backend/`

`vi Dockerfile`

#### Step 5b

Rebuild the image

`docker build -t stakaterlabs/hello-world-back .`


