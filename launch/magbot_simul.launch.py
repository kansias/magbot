import os
from tkinter import E
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess, IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    package_name = 'magbot'
    rviz_file = 'magbot.rviz'
    world_file = 'world_industry.world'
    
    pkg_path = os.path.join(get_package_share_directory(package_name))
    rviz_config = os.path.join(pkg_path, "config_simul", rviz_file)
    world_path = os.path.join(pkg_path, "worlds", world_file)
    
    rsp = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [os.path.join(get_package_share_directory(package_name), 'launch', 'magbot.launch.py')]
        ),
        launch_arguments={'use_sim_time': 'true', 'world': world_path}.items()
        
    )
    
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [os.path.join(get_package_share_directory("gazebo_ros"), "launch", "gazebo.launch.py")]
        ),
    )
    
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-topic', 'robot_description', '-entity', 'with_robot'],
        output='screen',
    )
    
    joint_state_publisher = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher'
    )
    
    map_publisher_node = Node(
        package = 'magbot',
        executable='map_publisher',
        name='map_publisher',
        output='screen'
    )
    
    rviz_start = ExecuteProcess(
        cmd=["ros2", "run", "rviz2", "rviz2", "-d", rviz_config], 
        output='screen'
    )
        
    
    return LaunchDescription(
        [
            TimerAction(
                period = 2.0,
                actions = [
                    rviz_start
                ]
            ),
            rsp,
            joint_state_publisher,
            map_publisher_node,
            gazebo,
            spawn_entity
        ]
    )