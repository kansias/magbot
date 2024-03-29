import os
from glob import glob
from setuptools import setup

package_name = 'magbot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*.xacro')),   
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*.gazebo')),
        (os.path.join('share', package_name, 'worlds'), glob('worlds/*.world')),
        (os.path.join('share', package_name, 'models'), glob('models/**')),
        (os.path.join('share', package_name, 'config_simul'), glob('config_simul/*.rviz')),
        (os.path.join('share', package_name, 'scripts'), glob('scripts/*.py')),
    
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='aicompany',
    maintainer_email='aico@aico.company',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'map_publisher = map_publisher:main',
        ],
    },
)
