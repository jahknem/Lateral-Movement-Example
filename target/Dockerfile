# Dockerfile for "target"
FROM alpine:latest

# Install OpenSSH and rsyslog
RUN apk add --no-cache bash openssh iproute2 rsyslog \
    && echo "root:aHyN7NJov38I77q" | chpasswd \
    && ssh-keygen -A \
    && sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config \
    && sed -i 's/#LogLevel INFO/LogLevel INFO/' /etc/ssh/sshd_config \
    && sed -i 's/#SyslogFacility AUTH/SyslogFacility AUTH/' /etc/ssh/sshd_config

# Configure rsyslog to log SSH auth messages
RUN echo "auth.* /var/log/auth.log" >> /etc/rsyslog.conf \
    && mkdir -p /var/spool/rsyslog \
    && touch /var/log/auth.log

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


# Add the public key to authorized_keys
COPY .ssh/id_rsa.pub /root/.ssh/id_rsa.pub
RUN mkdir -p /root/.ssh \
    && cat /root/.ssh/id_rsa.pub >> /root/.ssh/authorized_keys \
    && chmod 600 /root/.ssh/authorized_keys \
    && rm /root/.ssh/id_rsa.pub

# Expose SSH port
EXPOSE 22

# Start rsyslog and sshd
CMD ["/bin/sh", "-c", "rsyslogd && exec /usr/sbin/sshd -D"]
