# Use a lightweight base image with sshpass and ssh installed
FROM alpine:latest

# Install necessary packages
RUN apk add --no-cache openssh sshpass bash

# Copy the script into the container
COPY script.sh /script.sh

# Make the script executable
RUN chmod +x /script.sh

# Set the entrypoint to run the wrapper script
ENTRYPOINT ["/bin/bash", "./script.sh"]
