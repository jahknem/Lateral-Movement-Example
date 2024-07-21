# Use the latest Ubuntu image as a parent
FROM ubuntu:focal
MAINTAINER "Johan Pienaar" <johan@pienaarfamilie.nl>

ENV DEBIAN_FRONTEND=noninteractive TZ=Europe/Amsterdam

# Initial updates and install core utilities
RUN apt-get update -qq -y && \
    apt-get upgrade -y && \
    apt-get install -y \
       wget \
       curl \
       apt-transport-https \
       lsb-release \
       ca-certificates \
       gnupg2 \
       software-properties-common \
       locales \
       openssh-client \
       nmap \
       inetutils-ping \
       dnsutils \
       iproute2 \
       cron    
RUN dpkg-reconfigure locales

# Install Webmin
RUN echo root:password | chpasswd && \
    echo "Acquire::GzipIndexes \"false\"; Acquire::CompressionTypes::Order:: \"gz\";" >/etc/apt/apt.conf.d/docker-gzip-indexes && \
    update-locale LANG=C.UTF-8 && \
    echo deb https://download.webmin.com/download/repository sarge contrib >> /etc/apt/sources.list && \
    wget http://www.webmin.com/jcameron-key.asc && \
    apt-key add jcameron-key.asc && \
    apt-get update && \
    apt-get install -y webmin

# Add ssh ed25519 keys to /root/.ssh
COPY .ssh/id_ed25519 /root/.ssh/id_ed25519
COPY .ssh/id_ed25519.pub /root/.ssh/id_ed25519.pub
COPY .ssh/config /root/.ssh/config

EXPOSE 10000
ENV LC_ALL C.UTF-8

WORKDIR /home
RUN echo "#! /bin/bash" > entrypoint.sh && \
    echo "sed -i 's;ssl=1;ssl=0;' /etc/webmin/miniserv.conf && systemctl enable cron && service webmin start && tail -f /dev/null" >> entrypoint.sh && \
    chmod 755 entrypoint.sh

CMD /home/entrypoint.sh
