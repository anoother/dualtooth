from setuptools import setup, find_packages

setup(name='winblue',
    version='0.1.0',
    packages=find_packages(),
    description='Extract Bluetooth pairing information from a Windows registry hive',
    author='Ahmad Jagot',
    install_requires=[
        'python-registry'
    ],
    entry_points={
        'console_scripts': [
        'winblue=winblue:main',
        ],
    },
)
