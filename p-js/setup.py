from setuptools import setup

setup(
    name='p-js',
    version='1.0.0',
    description='A package for working with JSON files',
    author='Rajveer Singh',
    author_email='rajveersingh81248@gmail.com',
    packages=['pjs'],
    entry_points={
        'console_scripts': [
            'pjs = pjs.pjs:main',
        ],
    },
)
