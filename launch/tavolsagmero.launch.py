from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='far_c1f_tavolsagmero',
            executable='distance_generate',
            output='log',
            parameters=[{'log_level': 'WARN'}]
        ),
        Node(
            package='far_c1f_tavolsagmero',
            executable='distance_monitoring',
            output='screen'
        ),
    ])
