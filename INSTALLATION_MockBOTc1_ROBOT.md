## Manual installation of MockBOTc1-Robot packages on Robot Computer  

### Refer to separate Manual Installation of MockBOTc1-Desktop on the Desktop computer

This Repository is a varient of the Linorobot2 Repository with hardwire specific revisions to an URDF applicable to the AutonomyLab Create1 Base (https://github.com/AutonomyLab/create_robot), SlamTech© RPLidar, Luxonis© Oak-D-Lite Camera & IMU.

Note: This Procedure installs all base, sllidar, joy_teleop bringup, description scripts, on the Robot Computer (RaspBerry Pi) that does not necessarily require a connected monitor, though any robot SLAM & Nav Visualization functions should be done on the Remote Desktop Computer. These hardware launch procedures can be done directly on the Robot Computer running Ubuntu 24.04 Desktop with a connected dMonitor, Keyboard & Mouse, or from a Ubuntu Desktop with a SSH remote connnection.  

### 1. Install specfic functional Packages from ROS 2 and MockBOTc1-ROBOT Github Repository into the workspace. e.g. ros2_ws

### 1.1 Install and Source your ROS2 distro including colcon development packages, and workspace
If it's your first time using ROS 2 and haven't created your ROS2 workspace yet, you can check out 
[ROS2 Creating a Workspace](https://docs.ros.org/en/jazzy/Tutorials/Workspace/Creating-A-Workspace.html) tutorial. 
The MockBOTc1 code supports ros-distro = **jazzy** currently.  

From a Linux Terminal install the joy teleop packages
    \$ sudo apt install ros-jazzy-joy-linux
    \$ sudo apt install ros-jazzy-teleop\-twist\-joy  
    Then \$ source \/opt\/ros\/jazzy\/setup.bash  
    As a reminder, the .bashrc file should have this string above any other source commands.  

#### Check that ROS 2 is installed and sourced

In a Terminal, type
\$ which ros2
/opt/ros/jazzy/bin/ros2
should be displayed

#### Check that the Environmental variables are set  

\$ printenv | grep -i ROS  

ROS_VERSION\=2  
ROS_PYTHON_VERSION\=3  
ROS_DISTRO\=jazzy

A reminder that , as described in this repository's README.me, configure the **.gitignore** file if using Git and VSCode applications to develop code.  

### 1.2 Robot Launch packages  

Three repositries are available that describes and define the packages in the MockBOT TurtleTron Robot

https://github.com/ARLunan/MockBOTc1-Robot.git [MockBOTc1-Robot](https://github.com/ARLunan/MockBOTc1-Robot.git)  
https://github.com/ARLunan/MockBOTc1-Desktop.git [MockBOTc1-Desktop](https://github.com/ARLunan/MockBOTc1-Desktop.git)  
https://github.com/Slamtec/sllidar_ros2.git [MockBOTc1-Docs] (https://github.com/Slamtec/sllidar_ros2.git)

\$ mkdir -p ~/ros2\_ws/src  
\$ cd ~/ros2_ws/src  
\$ git clone https://github.com/ARLunan/MockBOTc1-Robot.git  
\$ cd ~/ros2_ws  

Note: See https://docs.ros.org/en/jazzy/Tutorials/Intermediate/Rosdep.html  

\$ colcon build  

The "colcon build" on a Raspberry Pi 4 or 5 - should take a few minutes.

### 1.3 Configure Environment in Ubuntu Terminal  

\$ cd ~/  
\$ nan0 .bashrc  
Add  
source /opt/ros/jazzy/setup.bash  
source /ros2_ws/install/setup.bash  
Save  
Restart Terminal

### 1.4 Install Create Base Library and driver

This Turtlebot Create Robot uses an iRobot Roomba 400 or Create 1 Base having a battery, Differerential Drive (2WD) motors controlled from a serial protocol with Subscription to /cmd_vel and  Publishes Odometry data. The driver packages are installed from a gthub.com repository, cloned onto a local workspace and colcon build:  

### Here are all commands on the Raspberry Pi  

### Create/Roomba Base Drivers  
The required AutonomyLabs create_robot and libcreate packages will be installed in the ros2\_ws/src workspace and a build done [https://github.com/AutonomyLab](https://github.com/AutonomyLab) As described earlier, see Appendix-1 UDEV Rules in [MockBot-DOCS/Supplementary Content](https://github.com/ARLunan/MockBot-Docs/tree/main/Supplementary%20Content)

\$ cd ros2_ws\/src  

Refering to the AutonomyLabs Repository, clone the create\_robot repository  
\$ cd ~/ros2\_ws/src  
\$ git clone https://github.com/autonomylab/create_robot.git  
\$ git clone https://github.com/AutonomyLab/libcreate.git

Note: See https://docs.ros.org/en/jazzy/Tutorials/Intermediate/rosdep.html  
\$ cd ~/ros2_ws
\$ sudo rosdep init     -- do it once  
\$ rosdep update  

\$ rosdep install --from-paths src --ignore-src -r -y  
this will take a while, many additional packages installed:  

The "colcon build" on a Raspberry Pi 4 or 5 - should take a few minutes.

### 1.5 Sensors: Slamtech© RPLIdar, Luxonis© OAK-D-Lite Camera RGB image, Stereo depth drivers, and IMU  

**SllIDAR**  
\$ cd ros2_ws\/src
ros2_ws\/ sudo git clone https://github.com/Slamtec/sllidar_ros2.git.  

Note that it is necssary configure USB udev rules **50-create.rules** and  **60-rplidar.rules**  into /etc/udev/rules.d directory. Refer to MockBOT-Docs / Supplementary Cntent / Appendix 1-UDEV Rules.  

First unplug Create/Roomba and SLLIdar USB cable. 

Open the above Repository and navigate to folder with the UDEV rules.  

*Camera and IMU*  
An **Luxonis OAK-D-Lite Camera** includes a RBG Color Camera to Publish a Color Image,  Stereo pair Camera to Publish a Depth Image, and IMU Publishing Acceleration motion and GyroScope position data in a coordinate protocol. 

Power and Data data connection is to a USB-3 connector on the Raspberry Pi.

The drivers are installed from a Binary package on the ROS Repository with the following script run from a Terminal : (where \$ROS_DISTRO is humble, previously installed on the Robot. 

   \$ sudo apt install ros_\$ROS_DISTRO-depthai-ros
    
Of many ARGUMENTS used in the Oak-D-Lite driver,  several values in the Launch scripts are set that are suitable for this robot model: camera_model = OAK-D-LITE, mode = depth, imu_Mode = 1 (LINEAR_INTERPOLATE_GYRO to prioritize gyroscope & interpolates Accelerometer Data suitable for yaw rate use), stereo_fps = 10 (to reduce message load), previewWidth, previewHeight = 412, enableRviz = False (no Rviz display on the Robot).

A suitable launch script will be provided to launch the Camera and IMU in the "bringup.launch.py script.

The camera is powered from a USB-C connector preferably configured with a Power Splitter to power the camera directly from the battery source and data connection to USB-3 on the Raspberry Pi.  

### 1.6 Configure Serial USB Permissions and Install USB Serial Port udev Rules

USB Permissions
In order to connect to Create over USB, ensure your user is in the dialout group. Refer also to MockBOT-DOCs https://github.com/ARLunan/MockBot-Docs.git [Appendix 1: UDEV Rules to manage USB Connected Devices](https://github.com/ARLunan/MockBot-Docs.git)

\$ sudo usermod -a -G dialout \$USER
Logout and login for permission to take effect

**Install USB udev rules**
With Create 1 Base and RPLidar USB serial connection, it is essential that Linux Device manager interface to assign persistant names for these two serial ports in the /dev folder. /dev/create1 and /dev/rlidar.

The two necessary udev rules are posted in the MockBot-Docs repository /Supplementary Content/ folder ( https://github.com/ARLunan/MockBot-Docs.git )

**Create1**: The udev file *50-create.rule* 

KERNEL=="ttyUSB*", ATTRS{idVendor}=="0403" ATTRS{idProduct}=="6001", MODE:-"0666', SYMLINK+="create_1"

In Linux terminal, navigate to the mockbotc1_bringup/scripts folder and manually execute the following commands:
\$ sudo cp 50-create.rules /etc/udev/rules.d
\$ sudo service udev reload
\$ sudo service udev restart
\$ sudo udevadm control --reload && sudo udevadm trigger

**SLLidar**: 
The udev file *60-create.rule*s is included in the above repository 

KERNEL=="ttyUSB*", ATTRS{idVendor}=="10c4" ATTRS{idProduct}=="ea60", MODE:-"0666', SYMLINK+="rplidar1"

In Linux terminal, navigate to the mockbotc1_bringup/scripts folder and manually execute the following commands:
\$ sudo cp 60-create.rules /etc/udev/rules.d
\$ sudo service udev reload
\$ sudo service udev restart
\$ sudo udevadm control --reload && sudo udevadm trigger
To verify the correct functioning of the udev rules, rom a terminal running the following command should list the MockBOTc1 USB serial ports with assigned names:x ports:

ubuntu@rp5-ub24h-mt:\~\$ ls -l /dev/ |grep USB

lrwxrwxrwx  1 root   root           7 Mar  5 14:02 create_1 -> ttyUSB0  
lrwxrwxrwx  1 root   root           7 Mar  5 14:02 rplidar -> ttyUSB1  
crw-rw-rw-  1 root   dialout 188,   0 Mar  5 14:02 ttyUSB0  
crw-rw-rw-  1 root   dialout 188,   1 Mar  5 14:02 ttyUSB1  

### 2 Laser Sensor  

The installation procedure for the OAK-D-Lite Camera and IMU will be posted here when complete

### 3. Save changes

Source your ~/.bashrc to apply the changes you made:  
   \$ source ~/.bashrc

## Miscellaneous

Future launch on powerup will be included here
