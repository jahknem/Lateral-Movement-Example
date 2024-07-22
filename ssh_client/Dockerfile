# Use a lightweight base image with sshpass and ssh installed
FROM python:3

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update -y && apt-get install -y --no-install-recommends \
    openssh-client \
    sshpass

# RUN mkdir -p /root/.ssh && \
#     touch /root/.ssh/config && \
#     touch /root/.ssh/known_hosts && \
#     chmod -R 400 /root/.ssh

# Copy the entrypoint script into the container
COPY entrypoint.sh /usr/local/bin/entrypoint.sh

# Ensure the script is executable
RUN chmod +x /usr/local/bin/entrypoint.sh

COPY main.py ./

# Set the entrypoint script
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

# Default command
CMD ["python", "./main.py"]
