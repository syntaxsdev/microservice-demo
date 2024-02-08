# Python Micorservices Demo

### Red Hat Learning Experience Workshop: Building Microservices w/FastAPI.
In this workshop we will discover how to work with FastAPI, a web framework tool similar to Flask. 
It is just as easy to use, but more powerful.

### What does this cover?
1. We explore how to use GET methods
2. Demonstrate how to query a list of users
3. Show how to handle pictures
4. Create a basic webpage in HTML and JavaScript

## Requirements:
1. Laptop running Windows, Mac, or Linux
2. Python 3.9+ installed
3. A browser

## How To Setup

1. Clone the project
```sh
git clone git@github.com:syntaxsdev/microservice-demo.git
```

2. Change into directory
```sh
cd microservice-demo
```

3. Open `exercise.ipynb` and follow along!

## Running the FastAPI service in a Container

As an extension of Ryan Gniadek's [podman demo](https://github.com/ryangniadek/podman-demo) for Red Hat Edge to Cloud Learning Experience 2024 Hackathon, you can use the [Containerfile](./Containerfile) to build and run this application in a container.

See podman-demo [How to buld a container image](https://github.com/ryangniadek/podman-demo?tab=readme-ov-file#how-to-build-a-container-image) [Run your container image](https://github.com/ryangniadek/podman-demo?tab=readme-ov-file#run-your-container-image) for a detailed explanation of the commands below

```bash
# Build the container
$ podman build -f Containerfile -t python-fastapi-demo

# Run the container and expose port 8000 on the host system as a redirect to port 8000 in the container
$ podman run --rm -d --name fastapi-demo -p 8000:8000 localhost/python-fastapi-demo

# Query the FastAPI endpoint
$ curl http://localhost:8000

...

# Stop the FastAPI container
$ podman stop fastapi-demo
```
