# Developed by ARLunan based on wimblerobotics/sigyn
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

    oakd_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
         [base_pgk, "/launch/sub_launch/oakd_stereo.launch.py"]
       )
    )

    ld.add_action(oakd_launch)
    
    return ld