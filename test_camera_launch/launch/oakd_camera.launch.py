from launch_ros.substitutions import FindPackageShare

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution, TextSubstitution


def generate_launch_description():
    colors = {
        'background_r': '200'
    }

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                PathJoinSubstitution([
                    FindPackageShare('depthai_ros_driver'),
                    'launch',
                    'camera_as_part_of_a_robot.launch.py'
                ])
            ]),
            launch_arguments={
                'camera_model': 'OAK-D-LITE',
                'imu_from_descr': 'false'
            }.items(),
            remappings=[
                ('/', '/'),
                ('/', '/')
            ]
        )
    ])