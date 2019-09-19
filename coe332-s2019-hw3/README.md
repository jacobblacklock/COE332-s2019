# COE332 Fall 2019 Homework 3

### Preliminary Steps

- Make a private fork of this repo
- Clone your fork to wherever you are running Docker - either your computer or one of the training VMs

### Task 1: Dockerize Homework 2

Dockerize your Homework 2 source code by writing commands in the `Dockerfile` to expose the Flask server port and run `python main.py`. Verify this works by building and running your container locally. Some hints:

- Make sure you DO NOT copy your `bitbucket-pipelines.yml` file from HW2
- You will need to modify the `app.run()` call in `main.py` to specify the `0.0.0.0` "all interfaces" host, as well as port 5000.
- When you run your container, you will need to bind the Docker host's port 5000 to the container's port 5000
- On your Docker host, you should be able to `curl http://localhost:5000/` and get a response
- If you get stuck, feel free to Google and/or discuss on Slack.

### Task 2: Add Docker commands to `bitbucket-pipelines.yml`

Enable your fork's pipeline. Add Docker commands to get the pipeline to build and run your Dockerfile. Replace the lines `echo "YOUR COMMANDS"` and `echo "GO HERE"` with Docker commands to build and run your container.

```
pipelines:
  default:
    - step:
        name: Docker Runner
        image: python:3.7
        caches:
          - pip
          - docker
        services:
          - docker
        script:
          - docker version
          - echo "YOUR COMMANDS"
          - echo "GO HERE"
          - sleep 5s
          - curl http://localhost:5000/
```

### How You Will Be Graded

Your pipeline will be inspected to see that the output from `curl http://localhost:5000/` produces the correct output (the JSON structure that should be served from `/`).
