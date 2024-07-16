# Dockerfile for "sshuser"
FROM python:3.9-slim

# Install SSH client and necessary Python package
RUN apt-get update && \
    apt-get install -y openssh-client && \
    pip install paramiko && \
    rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Copy the Python script
COPY ssh_script.py /app/

# Command to run the script
CMD ["python", "ssh_script.py"]
