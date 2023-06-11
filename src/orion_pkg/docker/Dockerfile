FROM ros:humble

# Create a directory inside the container to copy the folder to
RUN mkdir /Code

# Copy the folder from the host machine to the container
#COPY orion_ws /Code/orion_ws/   ---------------------------------   This is to get the folders in there. 

# Basic tools
RUN apt-get update && \
    apt-get install vim nano git tmux wget curl python-pip net-tools iputils-ping  -y
    
# Add ros sourcing to bashrc
RUN echo ". /opt/ros/humble/setup.bash" >> ~/.bashrc   

# Set the working directory to the location where the folder is copied
WORKDIR /Code/orion_ws

COPY ./entrypoint.sh /

# Add ros sourcing to bashrc
RUN echo ". /opt/ros/humble/setup.bash" >> ~/.bashrc 

ENTRYPOINT ["/entrypoint.sh"]

# Add ros sourcing to bashrc
RUN echo ". /opt/ros/humble/setup.bash" >> ~/.bashrc 

