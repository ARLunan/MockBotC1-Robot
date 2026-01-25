# Developed by ARLunan based on depthai-ros/depthai_ros_driver/camera_as...robot.launch.py 
# and wimblerobotics/sigyn repo. Uses OAK-D-Lite camera model and enable imu. 
# ros2 launch mockbotc1_bringup robot_camera_launch.py
# Install ros-jazzy-depthai-ros-driver package
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription, launch_description_sources
from launch.actions import IncludeLaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.conditions import IfCondition, LaunchConfigurationEquals, LaunchConfigurationNotEquals
import launch_ros.actions
import launch_ros.descriptions

def generate_launch_description():

    ld = LaunchDescription()
    camera_launch_dir = get_package_share_directory('depthai_ros_driver')

    oakd_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
         [camera_launch_dir, "/launch/camera_as_part_of_a_robot.launch.py"]
       ), launch_arguments={
                    'camera_model': 'OAK-D-LITE',
                    'imu_from_desc': 'false',
                    # remapping imu topics to match MockBOTc1 expectations
                    # 'imu_out': 'ekt_imu_in',
                    }.items()
    )

    ld.add_action(oakd_launch)
    
    return ld