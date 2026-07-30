from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([
        Node(
            package='camera_ros',
            executable='camera_node',
            output='screen',
            parameters=[{
                'frame_id': 'camera_link_optical',
            }]
        )
    ])