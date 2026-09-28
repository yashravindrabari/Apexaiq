# Cheat Sheet: docker CLI & Dockerfile

## Table of Contents

- Introduction
- Container Architecture
- 1. docker CLI
  - 1.1 Container Related Commands
  - 1.2 Image Related Commands
  - 1.3 Network Related Commands
  - 1.4 Registry Related Commands
  - 1.5 Volume Related Commands
  - 1.6 All Related Commands
- 2. Dockerfile
- About the Authors

## Introduction

Containers allow the packaging of an application and everything needed to run it in a **container image**.

Inside a container you can include:

- A base operating system
- Libraries
- Files and folders
- Environment variables
- Volume mount-points
- Application binaries

A **container image** is a template for executing a container. Multiple containers can run from the same image and share the same behavior, which supports application scaling and distribution.

Images can be stored in a remote registry to make distribution easier.

Once a container is created, its execution is managed by the container runtime. You can interact with the container runtime through the `docker` command.

## Container Architecture

The three primary components of a container architecture are:

- **Client**
- **Runtime**
- **Registry**

The runtime contains the Docker daemon and manages containers and images. The registry can be local or remote and stores container images.

# 1. docker CLI

> All examples shown in the source document work in Red Hat Enterprise Linux.

## 1.1 Container Related Commands

### 1. Run a Container in Interactive Mode

Run a Bash shell inside an image:

```bash
docker run -it rhel7/rhel bash
```

Check the release inside a container:

```bash
cat /etc/redhat-release
```

### 2. Run a Container in Detached Mode

```bash
docker run --name mywildfly -d -p 8080:8080 jboss/wildfly
```

### 3. Run a Detached Container in a Previously Created Network

Create a network:

```bash
docker network create mynetwork
```

Run the container:

```bash
docker run --name mywildfly-net -d --net mynetwork \
-p 8080:8080 jboss/wildfly
```

### 4. Run a Detached Container with a Local Folder Mounted

```bash
docker run --name mywildfly-volume -d \
-v myfolder/:/opt/jboss/wildfly/standalone/deployments/ \
-p 8080:8080 jboss/wildfly
```

### 5. Follow Container Logs

```bash
docker logs -f mywildfly
```

Or:

```bash
docker logs -f [container-name|container-id]
```

### 6. List Containers

List only active containers:

```bash
docker ps
```

List all containers:

```bash
docker ps -a
```

### 7. Stop a Container

Stop a container:

```bash
docker stop [container-name|container-id]
```

Stop with a timeout of 1 second:

```bash
docker stop -t1
```

### 8. Remove a Container

Remove a stopped container:

```bash
docker rm [container-name|container-id]
```

Force stop and remove a container:

```bash
docker rm -f [container-name|container-id]
```

Remove all containers:

```bash
docker rm -f $(docker ps -aq)
```

Remove all stopped containers:

```bash
docker rm $(docker ps -q -f "status=exited")
```

### 9. Execute a New Process in an Existing Container

Execute and access Bash inside a WildFly container:

```bash
docker exec -it mywildfly bash
```

## Container Command Reference

Syntax:

```text
docker [CMD] [OPTS] [CONTAINER]
```

| Command | Description |
|---|---|
| `daemon` | Run the persistent process that manages containers |
| `attach` | Attach to a running container to view ongoing output or control it interactively |
| `commit` | Create a new image from a container's changes |
| `cp` | Copy files/folders between a container and the local filesystem |
| `create` | Create a new container |
| `diff` | Inspect changes on a container's filesystem |
| `exec` | Run a command in a running container |
| `export` | Export the contents of a container's filesystem as a tar archive |
| `kill` | Kill a running container using SIGKILL or a specified signal |
| `logs` | Fetch the logs of a container |
| `pause` | Pause all processes within a container |
| `port` | List port mappings or look up the public-facing port NATed to a private port |
| `ps` | List containers |
| `rename` | Rename a container |
| `restart` | Restart a container |
| `rm` | Remove one or more containers |
| `run` | Run a command in a new container |
| `start` | Start one or more containers |
| `stats` | Display one or more containers' resource usage statistics |
| `stop` | Stop a container by sending SIGTERM, then SIGKILL after a grace period |
| `top` | Display the running processes of a container |
| `unpause` | Unpause all processes within a container |
| `update` | Update configuration of one or more containers |
| `wait` | Block until a container stops, then print its exit code |

## 1.2 Image Related Commands

### 1. Tag an Image

Create an image called `myimage` with tag `v1` from `jboss/wildfly:latest`:

```bash
docker tag jboss/wildfly myimage:v1
```

Create a new image with the latest tag:

```bash
docker tag <image-name> <new-image-name>
```

Create a new image specifying a new tag:

```bash
docker tag <image-name>[:tag][username/] <new-image-name>.[:new-tag]
```

### 2. Exporting and Importing an Image

Export the image to an external file:

```bash
docker save -o <filename>.tar
```

Import an image from an external file:

```bash
docker load -i <filename>.tar
```

### 3. Push an Image to a Registry

```bash
docker push [registry/][username/]<image-name>[:tag]
```

### 4. Build an Image Using a Dockerfile

```bash
docker build -t [username/]<image-name>[:tag] <dockerfile-path>
```

Example:

```bash
docker build -t myimage:latest .
```

### 5. List Images

```bash
docker images
```

### 6. Remove an Image

```bash
docker rmi [username/]<image-name>[:tag]
```

### 7. Check Image History

Check the history of the `jboss/wildfly` image:

```bash
docker history jboss/wildfly
```

Check the history of another image:

```bash
docker history [username/]<image-name>[:tag]
```

## Image Command Reference

Syntax:

```text
docker [CMD] [OPTS] [IMAGE]
```

| Command | Description |
|---|---|
| `build` | Build images from a Dockerfile |
| `history` | Show the history of an image |
| `images` | List images |
| `import` | Create an empty filesystem image and import the contents of a tarball |
| `info` | Display system-wide information |
| `inspect` | Return low-level information on a container or image |
| `load` | Load an image from a tar archive or STDIN |
| `pull` | Pull an image or repository from the registry |
| `push` | Push an image or repository to the registry |
| `rmi` | Remove one or more images |
| `save` | Save one or more images to a tar archive |
| `search` | Search configured container registries for images |
| `tag` | Tag an image into a repository |

## 1.3 Network Related Commands

Syntax:

```text
docker network [CMD] [OPTS]
```

| Command | Description |
|---|---|
| `connect` | Connects a container to a network |
| `create` | Creates a new network with the specified name |
| `disconnect` | Disconnects a container from a network |
| `inspect` | Displays detailed information on a network |
| `ls` | Lists all networks created by the user |
| `rm` | Deletes one or more networks |

## 1.4 Registry Related Commands

| Command | Description |
|---|---|
| `login` | Log in to a container registry server. If no server is specified, the default is used |
| `logout` | Log out from a container registry server. If no server is specified, the default is used |

Default registry:

```text
https://index.docker.io/v1/
```

## 1.5 Volume Related Commands

Syntax:

```text
docker volume [CMD] [OPTS]
```

| Command | Description |
|---|---|
| `create` | Create a volume |
| `inspect` | Return low-level information on a volume |
| `ls` | List volumes |
| `rm` | Remove a volume |

## 1.6 Other Commands

| Command | Description |
|---|---|
| `events` | Get real-time events from the server |
| `inspect` | Show low-level information |
| `docker version` | Show version information |
| `docker version --format` / CLI version commands | Show Docker CLI version |

# 2. Dockerfile

A **Dockerfile** provides instructions to build a container image through:

```bash
docker build -t [username/]<image-name>[:tag] <dockerfile-path>
```

It starts from a previously existing base image using the `FROM` instruction, followed by other required Dockerfile instructions.

This process is similar to compiling source code into binary output. In this case, the output of the Dockerfile is a **container image**.

## Example Dockerfile

This example creates a custom WildFly container with a custom administrative user. It exposes administrative port `9990` and binds the administrative interface publicly.

```dockerfile
# Use the existing WildFly image
FROM jboss/wildfly

# Add an administrative user
RUN /opt/jboss/wildfly/bin/add-user.sh admin Admin#70365 --silent

# Expose the administrative port
EXPOSE 8080 9990

# Bind the WildFly management to all IP addresses
CMD ["/opt/jboss/wildfly/bin/standalong.sh", "-b", "0.0.0.0",
     "-bmanagement", "0.0.0.0"]
```

### Build the WildFly Image

```bash
docker build -t mywildfly .
```

### Run a WildFly Server

```bash
docker run -it -p 8080:8080 -p 9990:9990 mywildfly
```

### Access the WildFly Administrative Console

Open the following in a browser:

```text
http://<docker-daemon-ip>:9990
```

The credentials given in the source example are:

```text
admin / Admin#70635
```

## Dockerfile Instruction Reference

| Instruction | Description |
|---|---|
| `FROM` | Sets the base image for subsequent instructions |
| `MAINTAINER` | Sets the author field of the generated images |
| `RUN` | Executes commands in a new layer on top of the current image and commits the results |
| `CMD` | Defines the default command; allowed only once in the traditional Dockerfile syntax, with the last one taking effect |
| `LABEL` | Adds metadata to an image |
| `EXPOSE` | Informs the container runtime that the container listens on specified network ports |
| `ENV` | Sets an environment variable |
| `ADD` | Copies new files, directories, or remote file URLs into the container filesystem |
| `COPY` | Copies new files or directories into the container filesystem |
| `ENTRYPOINT` | Configures a container to run as an executable |
| `VOLUME` | Creates a mount point for externally mounted volumes |
| `USER` | Sets the username or UID used when running the image |
| `WORKDIR` | Sets the working directory for `RUN`, `CMD`, `ENTRYPOINT`, `COPY`, and `ADD` |
| `ARG` | Defines a variable that users can pass at build time using `--build-arg` |
| `ONBUILD` | Adds an instruction to be executed later when the image is used as the base for another build |
| `STOPSIGNAL` | Sets the system-call signal sent to the container to exit |

# Example: Running a Web Server Container

Create a directory:

```bash
mkdir -p www/
```

Create a text file:

```bash
echo "Server is up" > www/index.html
```

Run a process in a container as a daemon:

```bash
docker run -d \
-p 8000:8000 \
--name=pythonweb \
-v `pwd`/www:/var/www/html \
-w /var/www/html \
rhel7/rhel \
/bin/python \
-m SimpleHTTPServer 8000
```

Check that the server is working:

```bash
curl <container-daemon-ip>:8000
```

See that the container is running:

```bash
docker ps
```

Inspect the container:

```bash
docker inspect pythonweb | less
```

Open the running container:

```bash
docker exec -it pythonweb bash
```

### What the Commands Do

- `mkdir -p www/` — Create a directory if it does not already exist.
- `echo "Server is up" > www/index.html` — Create a text file to serve.
- `docker run -d` — Run the process in a container as a daemon.
- `-p 8000:8000` — Map port 8000 in the container to port 8000 on the host.
- `--name=pythonweb` — Name the container `pythonweb`.
- `-v ...:/var/www/html` — Map the container HTML directory to the host `www` directory.
- `-w /var/www/html` — Set the working directory.
- `rhel7/rhel` — Choose the RHEL image.
- `/bin/python -m SimpleHTTPServer 8000` — Run a Python simple web server listening on port 8000.
- `curl ...` — Check that the server is working.
- `docker ps` — See that the container is running.
- `docker inspect pythonweb | less` — Inspect the container.
- `docker exec -it pythonweb bash` — Open the running container and inspect it.

## RHEL Environment Requirement

To successfully run the web-server example in a RHEL environment, the source document specifies:

```bash
chcon -Rt svirt_sandbox_file_t `pwd`
```

# About the Authors

### Bachir Chihani, Ph.D.

Bachir Chihani holds an engineering degree from Ecole Superieure d'Informatique (Algeria) and a PhD in Computer Science from Telecom SudParis (France).

He has worked as a data engineer, software engineer, research engineer, and previously as a network engineer with CCNA Cisco certification.

His programming experience includes Scala/Spark, Java EE, Android, and Go. He has an interest in Open Source technologies, particularly Automation, Distributed Computing, and Software/System Design.

He has authored research papers in Context-Awareness, reviewed papers for international conferences, and served as a technical reviewer for books including *Spring Boot in Action* and *Unified Log Processing*.

### Rafael Benevides

Rafael Benevides is a Director of Developer Experience at Red Hat. He helps developers worldwide become more effective in software development and promotes tools and practices that improve productivity.

He has worked in application architecture and design and is a member of Apache DeltaSpike PMC. He has spoken at conferences including JUDCon, TDC, JavaOne, and Devoxx.

Twitter: `@rafabene`

LinkedIn: `https://www.linkedin.com/in/rafaelbenevides`

Website: `www.rafabene.com`
