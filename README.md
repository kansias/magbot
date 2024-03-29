# ROS2 Magnetic Wall Climbing Robot

This repository contains the code for a wall climbing robot that uses magnetic wheels to climb walls. The robot is controlled using ROS2 and is capable of climbing walls with a variety of surfaces. The robot is equipped with a camera and a LiDAR sensor for navigation and obstacle avoidance.

## 1. Environment Setup

The robot is built using the following hardware components:

- NVIDIA Jetson Nano Developer Kit or Raspberry Pi 4
- Ubuntu 22.04 LTS
- ROS2 Humble

The following software packages are required to run the code:

in terminal( zsh or bash):

```bash
cd $(your workspace)/src
git clone
cd ..
colcon build

# bash
source install/setup.bash

## or if you are using zsh
source install/setup.zsh
```

## 2. Add model path to Gazebo

```bash
vi ~/.gazebo/gui.ini

```

```bash
[geometry]
x=0
y=0
[model_paths]
filenames=/home/$(your username)/$(your workspace)/src/magbot/models
```

## 3. Launching the Robot Simulation

To launch the robot simulation, run the following command:

```bash
cd $(your workspace)
source install/setup.bash # or source install/setup.zsh
ros2 launch magbot magbot.launch.py
```

This will launch the Gazebo simulation with the robot model and the environment. And Rviz2 will be launched to visualize the robot's sensor data.

## 4. Controlling the Robot

To control the robot, you can use the `teleop_twist_keyboard` package to send velocity commands to the robot. To install the package, run the following command:

```bash

# if you already have the package installed,
# you can skip this step

sudo apt install ros-humble-teleop-twist-keyboard
```

Then, run the following command to control the robot using the keyboard.

Open a new terminal and run the following command:

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

You can now use the keyboard to control the robot. The following keys can be used to control the robot:
