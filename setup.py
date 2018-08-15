from setuptools import setup, find_packages

setup(name='dualtooth',
    version='0.1.1',
    packages=find_packages(),
    description='Extract Bluetooth pairing information from a Windows registry hive',
    author='Ahmad Jagot',
    install_requires=[
        'python-registry'
    ],
    entry_points={
        'console_scripts': [
        'dualtooth=dualtooth.run:main',
        ],
    },
)
