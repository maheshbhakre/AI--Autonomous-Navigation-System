from glob import glob
from setuptools import setup

package_name = "autonomous_navigation"

setup(
    name=package_name,
    version="0.1.0",
    packages=[],
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
        ("share/" + package_name + "/launch", glob("launch/*.launch.py")),
        ("share/" + package_name + "/config", glob("config/*.yaml")),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Project Maintainer",
    maintainer_email="maintainer@todo.todo",
    description="Gazebo and Nav2 A* simulation configuration for autonomous navigation.",
    license="TODO",
    tests_require=["pytest"],
    entry_points={"console_scripts": []},
)
