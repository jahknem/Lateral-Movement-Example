# Dockerfile for "target"
FROM alpine:latest

# Install OpenSSH and iproute2
RUN apk add --no-cache openssh iproute2 \
    && echo "root:aHyN7NJov38I77q" | chpasswd \
    && ssh-keygen -A \
    && sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config \
    && sed -i 's/#LogLevel INFO/LogLevel VERBOSE/' /etc/ssh/sshd_config

# Expose SSH port
EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
