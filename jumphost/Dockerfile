# Dockerfile for "jumphost"
FROM ubuntu:focal

# Install OpenSSH
RUN apt update && \
    apt install openssh-server openssh-client sshpass -y \
    && echo "root:Wintermute" | chpasswd

# Configure SSH to allow TCP forwarding
RUN ssh-keygen -A \
    && sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config \
    && echo "AllowTcpForwarding yes" >> /etc/ssh/sshd_config \
    && echo "PermitTunnel yes" >> /etc/ssh/sshd_config \
    && echo "GatewayPorts yes" >> /etc/ssh/sshd_config

COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

# Expose SSH port
EXPOSE 22

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]