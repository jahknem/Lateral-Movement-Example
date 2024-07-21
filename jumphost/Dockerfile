# Dockerfile for "jumphost"
FROM alpine:latest

# Install OpenSSH
RUN apk add --no-cache openssh openssh-client sshpass \
    && echo "root:Wintermute" | chpasswd

# Configure SSH to allow TCP forwarding
RUN ssh-keygen -A \
    && sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config \
    && sed -i 's/^AllowTcpForwarding.*/AllowTcpForwarding yes/' /etc/ssh/sshd_config \
    && sed -i 's/^PermitTunnel.*/PermitTunnel yes/' /etc/ssh/sshd_config \
    && sed -i 's/^GatewayPorts.*/GatewayPorts yes/' /etc/ssh/sshd_config \
    && sed -i 's/^AllowAgentForwarding.*/AllowAgentForwarding yes/' /etc/ssh/sshd_config \
    && { grep -q '^AllowTcpForwarding' /etc/ssh/sshd_config || echo 'AllowTcpForwarding yes' >> /etc/ssh/sshd_config; } \
    && { grep -q '^PermitTunnel' /etc/ssh/sshd_config || echo 'PermitTunnel yes' >> /etc/ssh/sshd_config; } \
    && { grep -q '^GatewayPorts' /etc/ssh/sshd_config || echo 'GatewayPorts yes' >> /etc/ssh/sshd_config; } \
    && { grep -q '^AllowAgentForwarding' /etc/ssh/sshd_config || echo 'AllowAgentForwarding yes' >> /etc/ssh/sshd_config; }

RUN echo -e "\nHost *\n    ForwardAgent yes\n" >> /etc/ssh/ssh_config

# Add the public key to authorized_keys
COPY .ssh/id_rsa.pub /root/.ssh/id_rsa.pub
RUN mkdir -p /root/.ssh \
    && cat /root/.ssh/id_rsa.pub >> /root/.ssh/authorized_keys \
    && chmod 600 /root/.ssh/authorized_keys \
    && rm /root/.ssh/id_rsa.pub

# Ensure SSH agent is started
RUN mkdir -p /etc/service/ssh-agent \
    && echo '#!/bin/sh' > /etc/service/ssh-agent/run \
    && echo 'exec /usr/bin/ssh-agent -D' >> /etc/service/ssh-agent/run \
    && chmod +x /etc/service/ssh-agent/run

# Expose SSH port
EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
