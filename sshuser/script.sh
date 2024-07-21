#!/bin/bash

while true; do
    echo "SSH connect"

sshpass -p "Wintermute" ssh -o StrictHostKeyChecking=no -tt jumphost << 'EOF'
sshpass -p "aHyN7NJov38I77q" ssh -o StrictHostKeyChecking=no -tt target << 'EOT'
sleep 120
touch /tmp/hello.txt
exit
EOT
exit
EOF

    sleep 1 # sleep 1 second
done
