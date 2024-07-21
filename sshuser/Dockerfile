# Use a lightweight base image with sshpass and ssh installed
FROM alpine:latest

# Install necessary packages
RUN apk add --no-cache openssh sshpass bash

RUN adduser -D -s /bin/bash bob

RUN mkdir -p /home/bob/.ssh
RUN chown -R bob:bob /home/bob/

# Copy the script into the container
COPY script.sh /script.sh
RUN chmod +x /script.sh
RUN chown bob:bob /script.sh

# Copy the bob key file into the container
COPY .ssh/bob /home/bob/.ssh/bob
RUN chown bob:bob /home/bob/.ssh/bob
RUN chmod 600 /home/bob/.ssh/bob

# copy the config file into the container
COPY .ssh/config /home/bob/.ssh/config
RUN chown bob:bob /home/bob/.ssh/config
RUN chmod 644 /home/bob/.ssh/config

# Make the script executable
RUN chmod +x /script.sh

RUN echo -e "\nHost *\n    ForwardAgent yes\n" >> /etc/ssh/ssh_config

USER bob

# Set the entrypoint to run the wrapper script
ENTRYPOINT ["/bin/bash", "./script.sh"]
