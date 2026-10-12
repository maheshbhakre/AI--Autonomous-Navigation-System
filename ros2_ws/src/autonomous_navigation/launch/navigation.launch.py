from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    package_share = FindPackageShare("autonomous_navigation")
    nav2_share = FindPackageShare("nav2_bringup")
    slam_share = FindPackageShare("slam_toolbox")
    use_sim_time = "true"

    slam = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution(
                [slam_share, "launch", "online_async_launch.py"]
            )
        ),
        launch_arguments={
            "use_sim_time": use_sim_time,
            "slam_params_file": PathJoinSubstitution(
                [package_share, "config", "slam_params.yaml"]
            ),
        }.items(),
    )

    navigation = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution(
                [nav2_share, "launch", "navigation_launch.py"]
            )
        ),
        launch_arguments={
            "use_sim_time": use_sim_time,
            "params_file": PathJoinSubstitution(
                [package_share, "config", "nav2_params.yaml"]
            ),
        }.items(),
    )

    rviz = Node(
        package="rviz2",
        executable="rviz2",
        arguments=[
            "-d",
            PathJoinSubstitution(
                [nav2_share, "rviz", "nav2_default_view.rviz"]
            ),
        ],
        parameters=[{"use_sim_time": True}],
        output="screen",
    )

    return LaunchDescription([slam, navigation, rviz])
