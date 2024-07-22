#!/bin/bash

# output current location
cd ~
pwd

ssh-keyscan -H jumphost >> /home/bob/.ssh/known_hosts

eval $(ssh-agent)
ssh-add /home/bob/.ssh/bob
while true; do
    echo "SSH connect"

ssh -A -tt -o StrictHostKeyChecking=no bob@jumphost << 'EOF'
ssh -tt -o StrictHostKeyChecking=no root@target "touch /tmp/hello.txt && sleep 120 && exit"
exit
EOF
echo "SSH disconnect"

    sleep 10 # sleep 1 second
done
