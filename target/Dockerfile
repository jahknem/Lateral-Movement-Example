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

# Expose SSH port
EXPOSE 22

# Start rsyslog and sshd
CMD ["/bin/sh", "-c", "rsyslogd && exec /usr/sbin/sshd -D"]
