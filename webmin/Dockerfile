# Use a Debian base image
FROM debian:latest

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive

# Install necessary packages and Webmin
RUN apt-get update && \
    apt-get install -y wget apt-transport-https gnupg && \
    wget -q http://www.webmin.com/jcameron-key.asc -O- | apt-key add - && \
    echo "deb http://download.webmin.com/download/repository sarge contrib" > /etc/apt/sources.list.d/webmin.list && \
    apt-get update && \
    apt-get install -y webmin && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Expose the Webmin port
EXPOSE 10000

# Start Webmin
CMD ["/usr/share/webmin/miniserv.pl", "/etc/webmin/miniserv.conf"]
