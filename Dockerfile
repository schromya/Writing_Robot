# Use an official Ubuntu 20.04 LTS as a parent image
FROM ubuntu:24.04

# Set noninteractive to avoid prompts during the build
ARG DEBIAN_FRONTEND=noninteractive

# INSTALL PACKAGES
RUN apt-get update &&\
    apt-get install -y \
    curl\
    python3-pip


# Install python packages (WARNING: Only use break-system-packages in container!!!!)
RUN pip install --break-system-packages \
    pin\
    numpy\
    pybullet

WORKDIR /workspace/

# Set the default command to execute
# When creating a container, this will simulate `docker run -it`
CMD ["bash"]

