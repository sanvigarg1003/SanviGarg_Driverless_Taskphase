from setuptools import find_packages, setup

package_name = 'rt2string'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sanvi_garg',
    maintainer_email='sanvi_garg@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
        'node1_publisher = rt2string.node1_publisher:main',
        'node2_checker = rt2string.node2_checker:main',
        'node3_responder = rt2string.node3_responder:main',
          ],
    },
)
