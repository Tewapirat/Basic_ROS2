from setuptools import find_packages, setup

import os
from glob import glob
package_name = 'mypkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),(os.path.join('share',package_name),glob("launch/*.launch.py")),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='vm22',
    maintainer_email='vm22@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "frist_publisher = mypkg.frist_node:main",
            "twist_publisher = mypkg.twist_pub:main",
            "frist_subscription = mypkg.frist_sub:main",
            "twist_subscription = mypkg.twist_sub:main",
            "turtle_avoidance= mypkg.turtle_control:main",
            "frist_param= mypkg.frist_param:main",
            "turtle_service_server = mypkg.turtle_service_server:main",


        ],
    },
)
