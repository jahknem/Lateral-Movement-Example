#!/bin/bash

ssh-keyscan -H jumphost >> ~/.ssh/known_hosts

eval $(ssh-agent)

while true; do
    echo "SSH connect"

ssh-add /root/.ssh/id_rsa
ssh -A -tt -o StrictHostKeyChecking=no jumphost << 'EOF'
ssh -tt -o StrictHostKeyChecking=no target "touch /tmp/hello.txt && sleep 120 && exit"
exit
EOF

    sleep 1 # sleep 1 second
done
