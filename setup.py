from setuptools import setup, find_packages

setup(
    name='EasyGraph',
    version='0.1.0',
    url='https://github.com/ahmedreza1/EasyGraph',
    author='Md Ahmed Reza',
    author_email='ahmedreza80@gmail.com',
    description='A simple python module to create all types of graphs.',
    packages=find_packages(),    
    install_requires=['matplotlib', 'pandas'],
)
