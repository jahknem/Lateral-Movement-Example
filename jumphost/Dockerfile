# Dockerfile for "jumphost"
FROM alpine:latest

# Install OpenSSH
RUN apk add --no-cache openssh openssh-client sshpass doas shadow bash sudo nmap iputils coreutils procps \
    && echo "root:Wintermute" | chpasswd

# Configure SSH to allow TCP forwarding
RUN ssh-keygen -A \
    && sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config \
    && sed -i 's/^AllowTcpForwarding.*/AllowTcpForwarding yes/' /etc/ssh/sshd_config \
    && sed -i 's/^PermitTunnel.*/PermitTunnel yes/' /etc/ssh/sshd_config \
    && sed -i 's/^GatewayPorts.*/GatewayPorts yes/' /etc/ssh/sshd_config \
    && sed -i 's/^AllowAgentForwarding.*/AllowAgentForwarding yes/' /etc/ssh/sshd_config \
    && sed -i 's/^#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config \
    && { grep -q '^AllowTcpForwarding' /etc/ssh/sshd_config || echo 'AllowTcpForwarding yes' >> /etc/ssh/sshd_config; } \
    && { grep -q '^PermitTunnel' /etc/ssh/sshd_config || echo 'PermitTunnel yes' >> /etc/ssh/sshd_config; } \
    && { grep -q '^GatewayPorts' /etc/ssh/sshd_config || echo 'GatewayPorts yes' >> /etc/ssh/sshd_config; } \
    && { grep -q '^AllowAgentForwarding' /etc/ssh/sshd_config || echo 'AllowAgentForwarding yes' >> /etc/ssh/sshd_config; }

RUN echo -e "\nHost *\n    ForwardAgent yes\n" >> /etc/ssh/ssh_config

# Add bob and alice users. Make Alice part of the wheel group
RUN adduser -D -s /bin/bash bob \
    && echo "bob:Summermute" | chpasswd \
    && adduser -D -s /bin/bash alice \ 
    && echo "alice:Neuromancer" | chpasswd \
    && adduser alice wheel

# Configure sudo for wheel group
RUN echo "%wheel ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

# Add Bob public key to authorized_keys
COPY .ssh/bob.pub /home/bob/.ssh/authorized_keys
RUN chmod 600 /home/bob/.ssh/authorized_keys
RUN chown bob:bob /home/bob/.ssh/authorized_keys
RUN chown -R bob:bob /home/bob

# Add Alice public key to authorized_keys
COPY .ssh/id_ed25519.pub /home/alice/.ssh/authorized_keys
RUN chmod 600 /home/alice/.ssh/authorized_keys
RUN chown alice:alice /home/alice/.ssh/authorized_keys
RUN chown -R alice:alice /home/alice

# Ensure SSH agent is started
RUN mkdir -p /etc/service/ssh-agent \
    && echo '#!/bin/sh' > /etc/service/ssh-agent/run \
    && echo 'exec /usr/bin/ssh-agent -D' >> /etc/service/ssh-agent/run \
    && chmod +x /etc/service/ssh-agent/run

# Expose SSH port
EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
