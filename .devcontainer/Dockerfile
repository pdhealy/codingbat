FROM python:3-slim

RUN apt-get update && apt-get install -y \
    git \
    openssh-server \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Configure SSH
RUN mkdir -p /var/run/sshd /root/.ssh \
    && chmod 700 /root/.ssh \
    && sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config \
    && sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config \
    && echo 'root:root' | chpasswd

EXPOSE 22
