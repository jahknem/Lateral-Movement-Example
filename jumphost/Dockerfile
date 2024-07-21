# Dockerfile for "jumphost"
FROM alpine:latest

# Install OpenSSH
RUN apk add --no-cache openssh openssh-client sshpass \
    && echo "root:Wintermute" | chpasswd

# Configure SSH to allow TCP forwarding
RUN ssh-keygen -A \
    && sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config \
    && echo "AllowTcpForwarding yes" >> /etc/ssh/sshd_config \
    && echo "PermitTunnel yes" >> /etc/ssh/sshd_config \
    && echo "GatewayPorts yes" >> /etc/ssh/sshd_config

# Add the public key to authorized_keys
COPY .ssh/id_rsa.pub /root/.ssh/id_rsa.pub
RUN mkdir -p /root/.ssh \
    && cat /root/.ssh/id_rsa.pub >> /root/.ssh/authorized_keys \
    && chmod 600 /root/.ssh/authorized_keys \
    && rm /root/.ssh/id_rsa.pub

# Expose SSH port
EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
