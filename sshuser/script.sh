#!/bin/bash

while true; do
    echo "SSH connect"

    # Connect to the target via the jumphost using the -J option with key-based authentication
    ssh -o StrictHostKeyChecking=no -J jumphost -tt target << 'EOF'
    sleep 5
    touch /tmp/hello.txt
    exit
EOF

    # Sleep 1 second before repeating
    sleep 1
done