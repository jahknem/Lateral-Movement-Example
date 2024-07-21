import os
import paramiko

# Connect to 'target' via 'jumphost' jumphost using /root/.ssh/id_rsa as private key
def connect_to_target(jumphost, target):
    jumphost_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
    target_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
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
    target_client = connect_to_target('jumphost', 'target')
except Exception as e:
    print(f"Error: {e}")
# Wait for 5 minutes