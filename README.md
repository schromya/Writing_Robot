# Writing Robot
M^3 project


## Setup
These are the instructions for setting up your system using Docker. We have only tested these instructions on Ubuntu and Windows.

### 1. Install and Start Docker
Make sure you have installed docker. You can install docker [here for windows](https://docs.docker.com/desktop/install/windows-install/) or [here for linux](https://docs.docker.com/desktop/install/linux/).

Now make sure docker is started.

### 2. Setup display forwarding

**If you are on Windows...**
Install https://sourceforge.net/projects/vcxsrv/. Start XLaunch (from the VcXsrv program group), set display settings to multiple windows, and ensure "Disable access control" is checked.

**If you are on Linux...**
Set up display forwarding by running:
```bash
xhost +local:
```
### 3. Build and Start The Container
Now  build the container image and start the container. Make sure you are in this directories root directory. These commands use the current directory as the containers file system so any changes you make to the files on your host machine will be mirrored in the container. These commands also allow the container's display to be forwarded to your host machine so that you can see it.

**If you are on Linux...**
```bash
sudo docker build -t robot-container .
sudo docker run  --rm -it -e DISPLAY=$DISPLAY --privileged -v /tmp/.X11-unix:/tmp/.X11-unix -v $(pwd):/workspace --net=host robot-container
```

**If you are on Windows...**
```bash
docker build -t robot-container .
docker run --rm -it -e  DISPLAY=host.docker.internal:0.0 --privileged -v ${PWD}:/workspace --net=host robot-container
```
### 3. Setting up Container
Now your container should be running and you should be in its terminal. But wait, there's more. You still have to do some container setup for ROS:
```bash
source /opt/ros/noetic/setup.sh
cd src/relaxed_ik_ros1/relaxed_ik_core
cargo build

cd /workspace
catkin build
source devel/setup.sh

chmod +x /workspace/src/panda_benchmark/scripts/*
```

## Running
Now, to run the simulation, do the following.


```bash
roslaunch panda_benchmark simulation.launch 

# Run the following in another  terminal to move the bot to a position
source devel/setup.sh
rosrun panda_benchmark main.py 
```

Note: If you get `lbGL error: MESA-LOADER: failed to retrieve device information` and Gazebo does not launch, please run `export LIBGL_ALWAYS_SOFTWARE=1` and you can try running the below commands again.

You should see a window pop up with the simulation.



## Docker Tips
* To open another docker terminal for a running container, run the following on your home-machine:
    ```bash
    # Show your running CONTAINER_ID
    docker ps 

    # Open another terminal using that CONTAINER_ID
    docker exec -it  <YOUR_CONTAINER_ID> bash

    # Source ROS properly
    source devel/setup.sh
    ```


## Resources
https://docs.google.com/document/d/10sXEhzFRSnvFcl3XxNGhnD4N2SedqwdAvK3dsihxVUA/edit?tab=t.0#heading=h.2ye70wns7io3

https://github.com/bhtxy0525/A_Example_for_Calculating_Robot_Dynamics_Using_Pinocchio_Library/blob/main/README.md

https://gepettoweb.laas.fr/doc/stack-of-tasks/pinocchio/devel/doxygen-html/md_doc_b-examples_i-inverse-kinematics.html

https://gepettoweb.laas.fr/hpp/pinocchio/doxygen-html/index.html

https://www.andre-gaschler.com/rotationconverter/   

https://frankaemika.github.io/docs/control_parameters.html

https://stack-of-tasks.github.io/pinocchio/download.html

https://docs.ros.org/en/jazzy/p/pinocchio/