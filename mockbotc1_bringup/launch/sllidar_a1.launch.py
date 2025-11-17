#!/usr/bin/env python3

# Revised by ARLunan Rossbots Oct 3, 2025 for MOCKBOTc1
# Due sue of udev rules, serial_port default changed to /dev/rplidar
# Package installed in mockbotc1_ws/src workspace

import os

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():

    package_name ='sllidar_ros2'

    return LaunchDescription([
        IncludeLaunchDescription(
            PathJoinSubstitution([
                FindPackageShare(package_name), 'launch', 'sllidar_a1_launch.py']),       
            launch_arguments={
                'serial_port' : '/dev/rplidar', 
            }.items(),
        )
    ])