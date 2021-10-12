#!/usr/bin/env python

import os, sys
from setuptools import setup, find_packages

setup(
    name='gs',
    version='1.0.0',
    url='https://github.com/kislyuk/gs',
    license='MIT License',
    author='Andrey Kislyuk',
    author_email='kislyuk@gmail.com',
    description='A minimalistic Google Storage client',
    long_description=open('README.rst').read(),
    install_requires=[
        "tweak >= 1.0.3, < 2",
        "pyjwt >= 2.2.0, < 3",
        "requests >= 2.22.0, < 3",
        "click >= 7, < 9",
        "cryptography >= 3.3.2",
        "python-dateutil >= 2.7.3, < 3",
        "crc32c >= 2.0.1, < 3"
    ],
    tests_require=["coverage", "flake8", "wheel"],
    packages=find_packages(exclude=['test']),
    entry_points={
        'console_scripts': [
            'gs=gs.cli:cli'
        ],
    },
    platforms=['MacOS X', 'Posix'],
    include_package_data=True,
    test_suite='test',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
