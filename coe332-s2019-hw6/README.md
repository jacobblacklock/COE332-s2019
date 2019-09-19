# COE332 Spring 2019 Homework 4

This homework asks you to docker-compose your homework 3. 

### Preliminary Steps

- Make a *private fork* of this repo
- Clone your fork to wherever you are running Docker - either your computer or one of the training VMs
- Share it with `abkahn`, `jchuahtacc`, `jismisk`
- Create a file called `HW4.md` with your name and EID. Make sure that you add, commit and push it with git
- Enable a pipeline on your private fork of this repository
- You may run the server locally by running `python3 main.py`
- You may also run the server by running `docker-compose up`
- IMPORTANT: Look at the output messages when running `docker-compose up` or when running the pipeline on BitBucket to see if any errors happen. That is a good way to debug your code.

### Task 1: Docker-compose your Homework 3

Docker-compose your Homework 3 source code by creating a `docker-compose.yml` file. Verify this works by building and running your container locally (or on VM) using `docker-compose up`. Some hints:

- You will need to create services for flask and redis and connect them with a docker network
- `volumes` does not work on BitBucket, but it will work locally and on your VMs. So *make sure to remove the `volumes` clauses from the docker-compose.yml*
- On your Docker host, you should be able to `curl http://localhost:5000/` and get a response
- If you get stuck, feel free to Google and/or discuss on Slack.

### Task 2: Modify your `bitbucket-pipeline.yml` to docker-compose your homework in the pipeline

You will need to *modify your `bitbucket-pipelines.yml` file from HW3* by removing the `docker build` and `docker run` commands with `docker-compose up`. Some hints:

- You need to install docker-compose into the BitBucket pipeline
- You need to run docker-compose in detached mode (see https://docs.docker.com/compose/reference/up/)

### How you will be graded

You will be graded on the basis of your Bitbucket Pipeline output. Full credit is awarded to repositories that demonstrate:
- All unit tests passing
- Full coverage of `app.py`
- Your app should "compose" using the pipeline
- Your pipeline will be inspected to see that the output from `curl http://localhost:5000/` produces the correct output (the JSON structure that should be served from `/`).
