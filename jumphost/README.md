# Jumphost Docker Container

This repository contains the necessary files to build and run a jumphost Docker container. A jumphost is a server that acts as an intermediary for accessing other servers within a network.

## Prerequisites

Before running the jumphost Docker container, make sure you have the following prerequisites installed:

- Docker: [Install Docker](https://docs.docker.com/get-docker/)

## Building the Container

To build the jumphost Docker container, follow these steps:

1. Clone this repository: `git clone https://github.com/your-username/jumphost.git`
2. Navigate to the repository directory: `cd jumphost`
3. Build the Docker image: `docker build -t jumphost .`

## Running the Container

Once the Docker image is built, you can run the jumphost container using the following command:

```
docker run -d -p 22:22 --name jumphost jumphost
```

This command will start the jumphost container in detached mode and map port 22 of the container to port 22 of the host machine.

## Connecting to the Jumphost

To connect to the jumphost, you can use SSH with the following command:

```
ssh -p 22 user@localhost
```

Replace `user` with the desired username for accessing the jumphost.

## License

This project is licensed under the [MIT License](LICENSE).
