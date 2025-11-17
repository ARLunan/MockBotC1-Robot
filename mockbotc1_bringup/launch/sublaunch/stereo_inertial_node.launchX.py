## wimplerobotics sigyn robot design

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

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription, launch_description_sources
from launch.actions import GroupAction, IncludeLaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from  launch_ros.actions import PushRosNamespace
import launch_ros.actions
import launch_ros.descriptions
from launch_ros.substitutions import FindPackageShare
import sys


def generate_launch_description():
    oakd_launch_path = PathJoinSubstitution(
        [FindPackageShare('base'), 'launch', 'sub_launch',
         'stereo_inertial_node.launchX.py'
        ]
    )


    ld = LaunchDescription()

    stereo_node_left = GroupAction(
        actions=[
            PushRosNamespace('oakd_top'),
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(oakd_launch_path),
                launch_arguments={
                    'base_frame' : 'oak',
                    'camera_model' : 'OAK-D',
                    'rgbResolution': '1080p',
                    'tf_prefix' : 'oak',
                    'mxId' : '14442C1051B665D700',
                    'previewWidth': '640',    # match NN input size
                    'previewHeight': '640',
                    # Switch to a non-YOLO SSD-based model to avoid side7 mask errors:
                    'resourceBaseFolder': PathJoinSubstitution([FindPackageShare('depthai_examples'), 'resources']),
                    'nnName': 'yolov4_tiny_coco_416x416_openvino_2021.4_6shave_bgr.blob',  # SSD retail model
                    # 'numShaves': '7',          # match blob's shave count
                    'enableSpatialDetection': 'true',
                    'syncNN': 'true',
                    'detectionClassesCount': '80',
                }.items()
            )
        ]
    )
    ld.add_action(stereo_node_left)

    return ld