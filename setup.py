from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'far_c1f_tavolsagmero'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*launch.[pxy][yma]*')), 
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Wolreg',
    maintainer_email='farkas8891@gmail.com',
    description='Tavolsagmero: Package description',
    license='GNU General Public License v3.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "distance_generate = far_c1f_tavolsagmero.distance_publisher:main",
            "distance_monitoring = far_c1f_tavolsagmero.distance_monitor:main"
            
            # 'control_vehicle = far_c1f_tavolsagmero.control_vehicle:main',
        ],
    },
)
