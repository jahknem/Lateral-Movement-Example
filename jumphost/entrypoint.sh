#!/bin/sh

# Write the PUB variable to the .pub file
echo "$PUB" | base64 -d > /root/.ssh/id_25519.pub
chmod 644 /root/.ssh/id_25519.pub

# Start the SSH daemon
exec /usr/sbin/sshd -D
