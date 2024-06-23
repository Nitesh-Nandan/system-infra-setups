# syntax=docker/dockerfile:1
FROM ubuntu:latest

# Install app dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip mysql-shell curl vim && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /home

# COPY Scritps for easy access
COPY commands.md /home/commands.md

CMD ["tail", "-f", "/dev/null"]
LABEL authors="niteshnandan"
# Expose the port
EXPOSE 7001
