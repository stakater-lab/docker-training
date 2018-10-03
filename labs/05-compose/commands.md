### Step 1

#### Step 1a

Create a docker compose file. [File contents](step1a/docker-compose.yml)

`vi docker-compose.yaml`

#### Step 1b

Run the docker compose services

`docker-compose up -d`

View list of created containers

`docker container ls`

### Step 2

#### Step 2a

Cleanup existing services

`docker-compose down`

#### Step 2b

Edit the compose file to add a spec for a user-defined bridge network. [File contents](step2b/docker-compose.yml)

`vi docker-compose.yml`

#### Step 2c

Run the services

`docker-compose up -d`

Verify the created containers

`docker container ls`

Verify the created network

`docker network ls`

### Step 3

#### Step 3a

Cleanup existing services

`docker-compose down`

#### Step 3b

Add a volume mount in the container. [File contents](step3b/docker-compose.yml)

`vi docker-compose.yml`

#### Step 3c

Run the services

`docker-compose up -d`

Verify the created containers

`docker container ls`

Verify the created volume
`docker volume ls`

### Step 4

#### Step 4a

Cleanup existing services

`docker-compose down`

#### Step 4b

Clone the repository

`git clone https://github.com/stakater-lab/docker-training.git`

Edit the compose file to specify a build context instead of image. [File contents](step4b/docker-compose.yml)

`vi docker-compose.yml`

#### Step 4c

Run the services and verify the created resources

`docker-compose up -d`

Verify the built image

`docker image ls`

Verify the create containers

`docker container ls`

