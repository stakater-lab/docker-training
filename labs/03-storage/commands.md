### Step 1

We can create a volume with the name "myvol"

`docker volume create myvol`

### Step 2

Inspect the mount point of the new volume we have created

`docker volume ls`

`docker inspect myvol`

### Step 3

Create the container and mount the volume at the /vol mount point

`docker run -d --mount source=myvol,target=/vol --name hello-world-back stakaterlabs/hello-world-back`

### Step 4

Let's write a small text file into the volume path. Let's verify the contents

`docker exec hello-world-back sh -c "cd /vol && wget http://localhost:5000/getmessage"`

`docker exec hello-world-back sh -c "cd /vol && ls -lah"`

`docker exec hello-world-back sh -c "cat /vol/getmessage"`

### Step 5

Let's verify the file contents on the host machine mount point

`docker inspect myvol`

`ls /var/lib/docker/volumes/myvol/_data`

`cat /var/lib/docker/volumes/myvol/_data/getmessage`

