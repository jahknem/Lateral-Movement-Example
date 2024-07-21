#!/bin/bash

ssh-keyscan -H jumphost >> ~/.ssh/known_hosts

eval $(ssh-agent)

while true; do
    echo "SSH connect"

ssh -A -i /root/.ssh/id_rsa -tt -o StrictHostKeyChecking=no -J root@jumphost root@target << 'EOF'
sleep 120
touch /tmp/hello.txt
exit
EOF

    sleep 1 # sleep 1 second
done
