# Revised by ARLunan for use in MockBOTc1 Nov 10, 2025
# Derived from "create_driver" Node in slgrobotics (publish_tf:False)
# https://github.com/slgrobotics/articubot_one/blob/main/robots/turtle/launch/turtle.drive.launch.py
# To configure the /odom topic names for compatibility with the Extended Kalman Filter (EKF) &
# slam_toolbox localization packages.
# remappings 'odom', from  /odom to /odom/unfiltered 
# dev=/dev/create_1 due to udev rules 
# remapping to /odom/unfiltered

from launch import LaunchDescription
from launch_ros.actions import Node

#
# See https://github.com/slgrobotics/robots_bringup/tree/main/Docs/Create1
#
# This file goes to ~/launch folder on Create 1 Turtlebot Raspberry Pi
#

def generate_launch_description():

    create_driver_node = Node(
        package='create_driver',
        namespace='',
        executable='create_driver',
        name='create_driver',
        output='screen',
        respawn=True,
        respawn_delay=4,
        parameters=[{
            'robot_model': 'CREATE_1',
            'dev': '/dev/create_1',
            # 'dev': '/dev/ttyUSB0',
            'baud': 57600,
            'base_frame': 'base_link',
            'odom_frame': 'odom',
            'latch_cmd_duration': 0.5,
            'loop_hz': 5.0,
            'publish_tf': False,
            'gyro_offset': 0.0,
            'gyro_scale': 1.19,
            'distance_scale': 1.02
        }],
        #remappings=[('cmd_vel', '/cmd_vel'),('odom','/odom')]
        remappings=[('cmd_vel', '/cmd_vel'),('odom','/odom/unfiltered')]
    )
    return LaunchDescription([
        create_driver_node,
    ])