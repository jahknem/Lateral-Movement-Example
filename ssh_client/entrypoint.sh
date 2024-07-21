#!/bin/sh

# Ensure .ssh directory exists
mkdir -p /root/.ssh

# Write the KEY variable to the id_rsa file
echo "$KEY" | base64 -d > /root/.ssh/id_rsa
chmod 600 /root/.ssh/id_rsa

# Write the PUB variable to the id_rsa.pub file
echo "$PUB" | base64 -d > /root/.ssh/id_rsa.pub
chmod 644 /root/.ssh/id_rsa.pub

# Add the private key to the SSH agent
eval "$(ssh-agent -s)"
ssh-add /root/.ssh/id_rsa

# Execute the main application
exec "python3" "/usr/local/bin/main.py"
# Output DONE to indicate the script has completed
echo "DONE"


