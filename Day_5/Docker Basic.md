# Docker: Getting Started

> A hands-on step-by-step basic guide to Docker essentials.
>
> Developed by the H3ABionet Pipelines and Computing Work Package, Computing Infrastructure project team.
>
> Prepared for the greater H3ABioNet and H3Africa Consortium communities.

## Document Control

- Version: 1.0
- Notes: Initial guide development

## Contents

1. [What are Containers?](#1-what-are-containers)
   - [Types of Containers](#11-types-of-containers)
   - [Popular Container Providers](#111-popular-container-providers)
   - [What is Docker](#12-what-is-docker)
   - [When to Use Docker](#13-when-to-use-docker)
   - [When Not to Use Docker](#14-when-not-to-use-docker)
   - [Core Components of Docker](#15-core-components-of-docker)
   - [Docker Terminology](#16-docker-terminology)
   - [Docker Editions](#17-docker-editions)
2. [Installing Docker CE on Ubuntu 20.04/20.04 LTS](#2-installing-docker-ce-on-ubuntu-20042004-lts)
3. [Getting Started](#3-getting-started)
4. [Docker Images](#4-docker-images)
5. [Docker Registry](#5-docker-registry)
6. [Docker Networking](#6-docker-networking)
7. [Docker Volumes](#7-docker-volumes)
8. [Docker Applications](#8-docker-applications)

## Background

This guide is produced by the Computing & Infrastructure working group under the Pipelines and Computing work package. It is intended to serve as a self-sufficient support guide on major aspects of Docker technology for system administrators across the H3ABioNet and collaborating partners.

All commands and screenshots are based on Ubuntu 20.04 OS. The guide is designed as a standalone self-guided walkthrough of installing, deploying and managing Docker containers. It assumes familiarity with navigating an Ubuntu 20.04 Linux system.

Following the instructions gives hands-on experience with installing the Docker Community Edition, creating a basic Docker container with a static web page, and using commands to manage multiple containers and images.

### Assumptions

- The reader is comfortable navigating the Ubuntu 20.04 Linux OS.
- The reader is able to install software and edit files at the command line.

## How to Read This Guide

- General text describes each section and command operation.
- Variations to default commands or warnings are highlighted in the original document.
- Tips are highlighted in the original document.
- Examples of expected output are shown separately.
- Commands to be run by the reader are specially formatted in the original document.

## Abbreviations

| Abbreviation | Description |
|---|---|
| OS | Operating System |
| CLI | Command Line Interface |
| GUI | Graphical User Interface |
| DHCP | Dynamic Host Configuration Protocol |
| IP | Internet Protocol |
| VM | Virtual Machine |

# 1. What are Containers?

In the recent past, the industry standard was to use Virtual Machines (VMs) to run software applications. VMs run applications inside a guest Operating System, which runs on virtual hardware powered by the host server's OS.

VMs provide full process isolation for applications, but this isolation comes with substantial computational overhead because hardware is virtualized for the guest OS.

Containers take a different approach. By leveraging the low-level mechanics of the host operating system, containers provide much of the isolation of virtual machines with a fraction of the computing power.

Essentially, Docker is a container-based system for applications. Docker provides another level of abstraction for applications beyond virtual servers.

## 1.1 Types of Containers

### Linux Containers (LXC)

Linux Containers, commonly known as LXC, are a Linux operating-system-level virtualization method for running multiple isolated Linux systems on a single host.

### Docker

Docker started as a project to build single-application LXC containers. It introduced changes that made containers more portable and flexible and later became its own container runtime environment.

At a high level, Docker is a Linux utility that can efficiently create, ship, and run containers.

### 1.1.1 Popular Container Providers

1. Linux Containers
   - LXC
   - LXD
   - CGManager
2. Docker
3. Singularity
4. Windows Server Containers

## 1.2 What is Docker?

Docker is described in the guide as an open platform for developers and sysadmins of distributed applications.

In simpler words, Docker is a tool that allows developers and system administrators to deploy applications in a sandbox called a **container** to run on the host operating system.

The key benefit of Docker is that it allows users to package an application with all of its dependencies into a standardized unit for software development.

Unlike virtual machines, containers do not have high overhead and therefore enable more efficient use of the underlying system resources.

## 1.3 When to Use Docker

Docker may be a good fit for the following situations:

### Learning New Technologies

Docker provides an isolated and disposable environment for trying new tools without spending time on installation and configuration.

Many projects maintain Docker images with their applications already installed and configured.

### Basic Use Cases

Pulling images from Docker Hub is useful when an application is basic or standard enough to work with a default Docker image.

Examples include hosting a website using a LAMP stack or using a reverse proxy when an official or well-supported image is available.

### App Isolation

If multiple applications need to run on one server, keeping the components of each application in separate containers can prevent dependency-management problems.

### Developer Teams

Docker provides convenient local development environments that can closely match production environments without requiring developers to SSH into a remote machine.

## 1.4 When Not to Use Docker

### Complicated Applications

For large or complicated applications, using a pre-made Dockerfile or pulling an existing image may not be sufficient. Building, editing, and managing communication between multiple containers on multiple servers can be time-consuming.

### Performance Is Critical

Docker has advantages compared with virtual machines because containers share the host kernel and do not emulate a complete operating system. However, Docker still imposes performance costs.

Processes running inside a container may not be as fast as processes running directly on the native OS.

### Security Is Critical

Containerization provides some security benefits by separating application components, but Docker also introduces its own security challenges, especially for complicated applications. These issues require appropriate security expertise.

### Multiple Operating Systems

Because Docker containers share the host computer's operating system, virtual machines may be required when the same application must be run or tested on different operating systems.

### Clusters

Docker containers on separate servers can be combined to form a cluster with Docker Swarm. However, Docker does not replace provisioning or automation tools such as Ansible, SaltStack, and Chef.

The guide also notes Docker's support for Kubernetes.

## 1.5 Core Components of Docker

Docker Engine is one of the core components of Docker and is responsible for the overall functioning of the Docker platform.

Docker Engine is a client-server application with three main components:

1. **Server**
2. **REST API**
3. **Client**

### Server

The server runs a daemon known as `dockerd` (Docker Daemon). It is responsible for creating and managing Docker images, containers, networks, and volumes.

### REST API

The REST API specifies how applications can interact with the server and instruct it to perform tasks.

### Client

The client is a command-line interface that allows users to interact with Docker using commands.

## 1.6 Docker Terminology

### Docker Image

A Docker image is a template that contains an application and all the dependencies required to run that application on Docker.

### Docker Container

A Docker container is a running instance of a Docker image.

### Docker Hub

Docker Hub is the official online repository where Docker images are available. Docker Hub also allows users to store and distribute custom images publicly or privately.

## 1.7 Docker Editions

Docker is available in two editions:

- **Community Edition (CE)**
- **Enterprise Edition (EE)**

### Community Edition (CE)

Suitable for individual developers and small teams. It offers limited functionality compared with Enterprise Edition.

### Enterprise Edition (EE)

Suitable for large teams and production environments.

The Enterprise Edition is further categorized into:

- Basic Edition
- Standard Edition
- Advanced Edition

# 2. Installing Docker CE on Ubuntu 20.04/20.04 LTS

The guide covers installing Docker on Ubuntu 20.04 LTS using:

- Advanced Packaging Tool (APT)
- Snap

## 2.1 Install Using Advanced Packaging Tool (APT)

### Update Existing Packages

```bash
sudo apt update
```

### Install Prerequisite Packages

```bash
sudo apt install curl apt-transport-https ca-certificates software-properties-common
```

### Add the Docker Repository

Add the GPG key:

```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add –
```

Add the Docker repository:

```bash
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
```

Update the package database:

```bash
sudo apt update
```

Check the Docker repository:

```bash
apt-cache policy docker-ce
```

### Install Docker

```bash
sudo apt install docker-ce
```

Start Docker:

```bash
sudo service docker start
```

Check Docker status:

```bash
sudo systemctl status docker
```

Enable Docker to start automatically during system boot:

```bash
sudo systemctl enable docker
```

Check Docker version:

```bash
docker --version
```

### Optional: Add Current User to Docker Group

```bash
sudo usermod -aG docker ubuntu
```

Give permissions to execute the Docker binary:

```bash
sudo chmod 755 /usr/bin/docker
```

## 2.2 Install Using Snap

Snap packages are universal Linux packages that make it easy to deploy applications/software on Linux distributions.

Check Docker versions available through Snap:

```bash
snap info docker
```

Install Docker:

```bash
sudo snap install docker
```

Verify installation:

```bash
snap services docker
```

Start Docker:

```bash
sudo snap start docker
```

Stop Docker:

```bash
sudo snap stop docker
```

Remove Docker installed using Snap:

```bash
sudo snap remove docker
```

# 3. Getting Started

## 3.1 Basic Commands

### Docker Info

Gives information about the Docker setup on the machine/VM.

```bash
docker info
```

### Run a Container and Enter Its Shell

```bash
sudo docker run -i -t ubuntu /bin/bash
```

The `-i` and `-t` flags provide an interactive session with a TTY attached. `/bin/bash` gives a Bash shell.

When you exit the shell, the container stops because containers only run as long as their main process.

### Run a Container and Print Output

```bash
docker run ubuntu echo hello-world
```

Output:

```text
hello-world
```

### Run a Container with a Name/Hostname

```bash
docker run -h CONTAINER1 -i -t ubuntu /bin/bash
```

### Run a Container with Networking Mode

```bash
docker run -h CONTAINER2 -i -t --net="bridge" ubuntu /bin/bash
```

### List Docker Containers

```bash
docker ps -a
```

### Inspect a Container

```bash
docker inspect CONTAINER_NAME
```

### Start a Stopped Container

```bash
docker start CONTAINER_NAME
```

### Enter the Shell of a Started Container

```bash
docker attach CONTAINER_NAME
```

### Delete a Container

```bash
docker rm CONTAINER_NAME
```

### Detach from a Container

```bash
docker run -t -i
```

A container started with `-t -i` can be detached with `^P^Q` and reattached with:

```bash
docker attach
```

A container started with `-i` cannot be detached with `^P^Q` without disrupting stdin.

### Docker Logs

Get a list of commands executed in a container:

```bash
docker logs CONTAINER_NAME
```

### Pause a Container

The container needs to be in the Started phase.

```bash
docker pause CONTAINER_NAME
```

### Unpause a Container

```bash
docker unpause CONTAINER_NAME
```

### Remove All Containers

```bash
docker rm `docker ps --no-trunc -aq`
```

### List Docker Networks

```bash
docker network ls
```

### Rename a Docker Container

```bash
docker rename OLD_NAME NEW_NAME
```

# 4. Docker Images

### Show Images

```bash
sudo docker images
```

### Specify an Image Variant

```bash
sudo docker run -i -t ubuntu:20.04 /bin/bash
```

### Pull an Image

```bash
sudo docker pull ubuntu
```

## Create Your Own Image

Create a directory:

```bash
mkdir docker-file
```

Enter the directory:

```bash
cd docker-file/
```

Create a Dockerfile:

```bash
touch Dockerfile
```

Add the following content:

```dockerfile
FROM ubuntu:20.04
MAINTAINER xyz "xyz@xyz.com"
RUN apt-get update
RUN apt-get install -y nginx
RUN echo 'Our first Docker image for Nginx' > /usr/share/nginx/html/index.html
EXPOSE 80
```

Press `Ctrl+D` to save the changes.

### Build a Docker Image

```bash
sudo docker build -t="test/my_nginx"
```

Check that the image has been created:

```bash
docker images | grep nginx
```

Expected:

```text
test/my_nginx
```

### Remove a Docker Image

```bash
docker rmi test/my_nginx
```

# 5. Docker Registry

Docker allows customized images to be bundled and pushed to Docker Hub or a locally hosted Docker registry. Images can be pushed to or pulled from these registries.

## Docker Hub Login

```bash
sudo docker login
```

Example:

```text
Username: username
Password:
Email: email@example.com
```

The guide notes that login credentials are saved in:

```text
/home/username/.dockercfg
```

## Search Public Images

For example, search for `centos`:

```bash
sudo docker search centos
```

## Push a Customized Image

The repository name should meet the username of the Docker Hub account.

```bash
sudo docker push username/newimage
```

## Install a Private Local Docker Registry

```bash
docker run -p 5000:5000 registry
```

## Tag an Image

```bash
docker tag username/newimage:latest localhost:5000/newimage:latest
```

## Push to a Private Docker Registry

```bash
docker push localhost:5000/newimage:latest
```

# 6. Docker Networking

## 6.1 Bind Host Port to Container Port

Run the previously created `my_ngnix` image with port binding:

```bash
sudo docker run -d -p 8080:80 --name test_container test/my_nginx nginx -g "daemon off;"
```

The `-p 8080:80` option binds host port `8080` to container port `80`.

The default web page can then be accessed using the Docker host's IP address.

```bash
curl http://docker-host-ip:8080
```

# 7. Docker Volumes

## 7.1 Get Started with Volumes

A Docker volume can be created and mounted in a container.

### Volume Mounted in a Container

Use the `-v` parameter:

```bash
docker run -v /volume1 -i -t ubuntu /bin/bash
```

Verify the volume:

```bash
ls
```

Example output includes:

```text
bin boot dev etc home lib lib64 var volume1
```

## Mount a Host Directory as a Volume

### 1. Create a Local Directory

```bash
sudo mkdir -p /host/logs
```

Create a file:

```bash
sudo touch /host/logs/log1.txt
```

### 2. Bind the Host Directory to a Container Volume

```bash
docker run -v /host/logs:/container/logs -i -t ubuntu /bin/bash
```

### 3. Check the Mounted Volume

```bash
ls
```

The contents are the same as those created in the host directory.

```bash
ls container/logs/
```

Expected:

```text
log1.txt
```

# 8. Docker Applications

## 8.1 Static Site on Nginx Server from Docker

The guide demonstrates hosting a static site using an Nginx server inside Docker.

### 1. Create a Dockerfile

```dockerfile
FROM ubuntu:20.04
RUN apt-get update
RUN apt-get install nginx -y
COPY index.html /var/www/html/
EXPOSE 80
CMD ["nginx", "-g", "daemon off:"]
```

### 2. Create `index.html`

```html
<html>
<h1>Hello World!</h1>
<p>Hi there – This is a simple static website!</p>
</html>
```

### 3. Directory Structure

```text
.
├── Dockerfile
└── public_html
    └── index.html
```

### 4. Create a Docker Image

```bash
docker build -t my-nginx .
```

### 5. Create a Docker Container

```bash
docker run -p 80:80 --name my-nginx-01 my-nginx
```

### 6. Open the Website

Open the host browser at:

```text
http://localhost:80
```

The website should be running.

---

## End

The guide ends with a request for comments or recommendations through the H3ABioNet helpdesk.

> oOo END oOo
