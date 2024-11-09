# ROS Turtle Rectangle Movement

This ROS package contains Python nodes for controlling the turtlesim turtle in various movement patterns, including rectangular path movement.

## Prerequisites
- ROS (tested on ROS Noetic)
- Python 3
- turtlesim package

## Installation
```bash
# Create a workspace (if you don't have one)
mkdir -p ~/ros_ws/src
cd ~/ros_ws/src

# Clone this repository
git clone https://github.com/Darshan-1820/ros-turtle-rectangle.git

# Build the package
cd ~/ros_ws
catkin_make

# Source the workspace
source devel/setup.bash
```

## Available Scripts
1. `move_rectangle.py`: Makes the turtle move in a rectangular path
2. `move_circle.py`: Makes the turtle move in a circular path
3. `move_straight.py`: Makes the turtle move in a straight line

## Usage for Rectangle Movement
1. Start ROS master:
```bash
roscore
```

2. In a new terminal, launch turtlesim:
```bash
rosrun turtlesim turtlesim_node
```

3. In another terminal, run the rectangle movement node:
```bash
rosrun ros_session move_rectangle.py
```

## Description
The rectangular movement script will:
1. Move the turtle in a rectangular path
2. Complete one full rectangle
3. Stop automatically after completion

## Video Demo
https://www.loom.com/share/8f62e3aad19c410ba5fcc2b8065d2729?sid=04139e6d-62f3-477d-916b-55425c65cf3d

## Author
Darshan
