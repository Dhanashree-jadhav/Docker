📌 Dockerfile Instructions


🔸 FROM ubuntu:22.04

Defines the base image

Provides OS, shell, and package manager

Every Dockerfile must start with FROM

🔸 RUN apt-get update && apt-get install -y curl

Executes commands during image build

Installs required dependencies

Creates a new image layer

🔸 WORKDIR /app

Sets default directory inside the container

Avoids using absolute paths repeatedly

🔸 COPY . .

Copies files from host system to container

Syntax: COPY <source> <destination>

🔸 CMD ["echo", "..."]

Default command executed when container starts


🔨 How to Build the Docker Image

docker build -t docker-demo .

Important points:

-t docker-demo → image name

. → build context (current directory)

Docker looks for Dockerfile in this directory

-t = tag

A tag is made of:

image-name:version

If you don’t specify a version, Docker assumes:
:latest

▶️ How to Run the Container
docker run docker-demo

Output:
Hello Docker! My first Dockerfile is working 🚀

Only one CMD is effective

Can be overridden at runtime
