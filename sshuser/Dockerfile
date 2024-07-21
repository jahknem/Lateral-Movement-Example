# Use a lightweight base image with sshpass and ssh installed
FROM alpine:latest

# Install necessary packages
RUN apk add --no-cache openssh sshpass bash

# Copy the script into the container
COPY script.sh /script.sh

# Copy the id_rsa file into the container
COPY .ssh/id_rsa /root/.ssh/id_rsa
RUN chmod 600 /root/.ssh/id_rsa

# Make the script executable
RUN chmod +x /script.sh

# Set the entrypoint to run the wrapper script
ENTRYPOINT ["/bin/bash", "./script.sh"]
