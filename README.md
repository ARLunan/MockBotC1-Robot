# MockBOT Project - TurtleTron iRobot© Create 1/Roomba 400 Base

This project defines the Jazzy branch for the TurtleTron Roomba 400/Create 1 base only.  
At this time, this repository is "Work in Progress" so expect errors to be displayed after launching many of the scripts and packages. 

The purpose of the work in this repository is to document the development and post the release of ROS 2 Packages that migrate the original "Willow Garage" / Open Robotics Turtlebot (tm) where the last released repository was ROS Indigo, to ROS 2 Jazzy Robot and Navigation 2 autonomous navigation packages. This new repository called "MockBOTc1" uses this original iRobot Create (™) (Now referred to as Create 1) Base, is a Roomba 400 Robot Vacuum product. It should be mentioned that while this repository is written to use with a iRobot Create 1, the installed base drive package by slgrobotics [](https://github.com/slgrobotics) which is a fork of (_Autonomy Labs ™_) includes support for the Roomba Model 400, 500 or 600) and Create 2 base. See Wikipedia for details of the various Roomba Models from 2004 to 2013. [] (https://en.wikipedia.org/wiki/IRobot_Create) To enable these drivers, a varient ot the bringup.launch.py must be used that is installed in the mockBOTc1_ws workspace and compiled.

TurtleTron MockBOTc1-Robot
Repository for the mockbotc1\_bringup, mockbotc1\_description, and EKF Sensor fusion functions
**NOTE**: At the current **commit** status of this repository, the **Launch** script, **\$ ros2 launch
mockbotc1\_bringup bringup.launch.py**. This script launches the Create\_1/ Roomba 400 Base, RPLidar, ekf\_filter, robot_description, joy\_teleop, twist\_mux. The other launch scripts in the launch folder such as for the Camera Oak-D Lite are in development.

Launching the slam\_toolbox, mapping and locaization, navigation functions are executed on the Desktop.

The Robot ekt Sensor Fusion and twist\_mux packages manage the several /cmd_vel messages from the  teleop (/cmd_vel_joy, cmd_vel_key, cmd_vel_key and Desktop  navigation (cmd_vel_nav) packages functions into a single /cmd_vel to drive the Create Base.

For ongoing work it is customary and conveninet to include the ros2 and workspace path locations saved into the Raspberry Pi Ubuntu root directory /home/ubuntu/ .bashrc file, as follows:  

.bashrc

\$ source /opt/ros/jazzy/setup.bash  
\$ source /home/ubuntu/ros2\_ws/install/setup.bash  

Another required deveopment task was to design a powering configuration due to the new "Power Delivery" function of the Raspberry Pi 5. With typical choices of a 1) "Power Bank" or 2) Lipo Battery/Buck DC-DC Converor, 2) was selected for this TurTleTron. More detail is included in the MockBOT Book and a "Powering Raspberry Pi 5" read.me.
