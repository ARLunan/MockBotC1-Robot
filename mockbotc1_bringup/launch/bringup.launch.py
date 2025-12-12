# Launch script for MOCKBOTc1 mockbotc1_bringup package by ARLunan November 2025 derived from 
# https://github.com/linorobot/linorobot2.git
# 
# Launches ROS 2 Python launch scripts, for the Base, Sensors:SLLIdar, OAK-D-Lite RGB Inertial Camera and IMU), 
# Logitech F710 Gamepad Joystick, ekf_filter_node, description (joint & robot state publisher) 
# For compatibility with the Extended Kalman Filter (EKF) & slam_toolbox localization 
# Revise odom_topic default_value to /odom/unfiltered and
# Revise remappings "odometry/unfiltered", odom_topic and add odometry/filtered, "/odom" 
# Using Substitutions for Large Projects https://docs.ros.org/en/kilted/Tutorials/Int`ermediate/Launch/Using-ROS2-Launch-For-Large-Projects.html
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http:#www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, LogInfo, TimerAction
from launch.substitutions import PathJoinSubstitution, LaunchConfiguration
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node
 
def generate_launch_description():
    bringup_launch_dir = PathJoinSubstitution([FindPackageShare('mockbotc1_bringup'), 'launch'])
    
    desc_launch_dir = PathJoinSubstitution([FindPackageShare('mockbotc1_description'), 'launch'])

    ekf_config_path = PathJoinSubstitution([FindPackageShare('mockbotc1_bringup'), 'config', 'ekf.yaml'])
    
    use_sim_time = LaunchConfiguration('use_sim_time', default='false')
    
    return LaunchDescription ([
         LogInfo(msg="Starting MockBOTc1 bringup..."),

         DeclareLaunchArgument(
            name='odom_topic', 
            # default_value='/odom',
            default_value='/odom/unfiltered',
            description='EKF out odometry topic'
         ),
         
         IncludeLaunchDescription(
           PathJoinSubstitution([bringup_launch_dir, 'base.launch.py'])
         ),

        IncludeLaunchDescription(
           PathJoinSubstitution([bringup_launch_dir, 'sllidar_a1.launch.py'])
         ),

        IncludeLaunchDescription(
           PathJoinSubstitution([bringup_launch_dir, 'joy_teleop.launch.py'])
         ),

         IncludeLaunchDescription(
           PathJoinSubstitution([bringup_launch_dir, 'twist_mux.launch.py'])
         ),
       
         Node(
            package='robot_localization',
            executable='ekf_node',
            name='ekf_filter_node',
            output='screen',
            parameters=[
                ekf_config_path
            ],
            remappings=[("odometry/unfiltered", LaunchConfiguration("odom_topic")),
                        ("odometry/filtered", "/odom")],
         ),
        
         TimerAction(
            period=5.0,
            actions=[
                LogInfo(msg='Localization Complete'),
            ]
         ),

         IncludeLaunchDescription(
            PathJoinSubstitution([desc_launch_dir, 'description.launch.py'])
         ), 

         LogInfo(msg="Completed MockBOTc1 bringup...")
    ])
