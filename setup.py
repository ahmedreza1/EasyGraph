from setuptools import setup, find_packages

# Read the content of your README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='EasyGraph_py',
    version='1.2.1',
    url='https://github.com/ahmedreza1/EasyGraph',
    author='Md Ahmed Reza',
    author_email='ahmedreza80@gmail.com',
    description='A simple python module to create all types of graphs.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),    
    install_requires=['matplotlib', 'pandas', 'seaborn', 'plotly', 'numpy'],
)
