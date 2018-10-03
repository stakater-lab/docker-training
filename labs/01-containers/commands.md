### Step 1

#### Step 1a

Create a simple shell script to print an environment variable. [File Contents](script.sh)

`vi script.sh`

#### Step 1b

Create a Dockerfile that includes the script file and has a default value for the variable.  [File Contents](Dockerfile)

`vi Dockerfile`

#### Step 1c

Build the dockerfile into an image

`docker build -t printer .`

### Step 2

Run a container from the image

`docker run --rm printer`

### Step 3

Rerun the container with a different value for the environment variable

`docker run --rm -e msg=Goodbye printer`

