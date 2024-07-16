# Dockerfile for "jumphost"
FROM alpine:latest

# Install OpenSSH
RUN apk add --no-cache openssh \
    && echo "root:Wintermute" | chpasswd

# Configure SSH
RUN ssh-keygen -A \
    && sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# Expose SSH port
EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
