from setuptools import setup

package_name = 'dog_ia_core'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Marco',
    maintainer_email='marco.silva.101692@a.fecaf.com',
    description='Pacote principal do robo cao-guia DOG-IA',
    license='MIT',
    entry_points={
        'console_scripts': [
            'valida_ambiente = dog_ia_core.valida_ambiente:main',
        ],
    },
)
