import paramiko
import time

JUMPHOST_SSH_PORT = 2222
TARGET_SSH_PORT = 2223


def ssh_jump(host, port, username, password, key_filename=None):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, port, username, password, key_filename=key_filename)
    return client

def main():
    jumphost = 'jumphost'
    target = 'target'
    while True:
        try:
            # Establish SSH connection to jumphost
            jumphost_client = ssh_jump(jumphost, JUMPHOST_SSH_PORT, 'root', 'Wintermute')
            jumphost_transport = jumphost_client.get_transport()
            dest_addr = (target, TARGET_SSH_PORT)
            local_addr = (jumphost, JUMPHOST_SSH_PORT)
            channel = jumphost_transport.open_channel("direct-tcpip", dest_addr, local_addr)

            # Connect to target machine through jumphost
            target_client = paramiko.SSHClient()
            target_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            target_client.connect(target, TARGET_SSH_PORT, 'root', 'aHyN7NJov38I77q', sock=channel)

            # Execute a command (e.g., 'date') on the target machine
            stdin, stdout, stderr = target_client.exec_command('date')
            print(stdout.read().decode())

            # Close connections
            target_client.close()
            jumphost_client.close()
            print("Sleeping for 30 seconds...")
            time.sleep(30)

        except Exception as e:
            print(f"Connection failed: {e}")
            time.sleep(30)

if __name__ == "__main__":
    main()
