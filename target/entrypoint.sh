#!/bin/sh

# Ensure .ssh directory exists
mkdir -p /root/.ssh

# Write the PUB variable to the .pub file
echo "$PUB" | base64 -d > /root/.ssh/authorized_keys
chmod 600 /root/.ssh/authorized_keys

# Start rsyslog and sshd
rsyslogd
exec /usr/sbin/sshd -D
