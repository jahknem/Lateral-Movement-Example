import os
import paramiko
import time

print("Starting...")

# Connect to 'target' via 'jumphost' jumphost using /root/.ssh/id_rsa as private key
def connect_to_target(jumphost, target):
    print(f"Connecting to {target} via {jumphost}...")
    jumphost_key = paramiko.Ed25519Key.from_private_key_file('/root/.ssh/id_rsa')
    target_key = paramiko.Ed25519Key.from_private_key_file('/root/.ssh/id_rsa')
    jumphost_client = paramiko.SSHClient()
    jumphost_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    jumphost_client.connect(jumphost, username='root', pkey=jumphost_key)
    transport = jumphost_client.get_transport()
    target_channel = transport.open_channel('direct-tcpip', (target, 22), ('localhost', 0))
    target_client = paramiko.SSHClient()
    target_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    target_client.connect(target, username='root', pkey=target_key, sock=target_channel)
    return target_client

# Run
try:
    print("Running...")
    while True:
        target_client = connect_to_target('jumphost', 'target')
        print("Running 'uptime' command on target machine...")
        stdin, stdout, stderr = target_client.exec_command('uptime')
        print(stdout.read().decode())
        target_client.close()
        # Write uptime to file
        with open('/root/uptime.txt', 'w') as f:
            f.write(stdout.read().decode())
        print("Sleeping for 30 seconds...")
        
        time.sleep(30)
except Exception as e:
    print(f"Error: {e}")
    time.sleep(600)
# Wait for 5 minutes




