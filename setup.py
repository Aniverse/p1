#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name="PtpUploader",
    version="0.1",
    author="kannibalox",
    url="https://github.com/kannibalox/PTPAPI",
    install_requires=[
        "poster",
        "pyrocore",
        "sqlalchemy",
        "flask",
        "requests",
        "watchdog"
    ],
    packages=find_packages('src'),
    package_dir={'':'src'},
    license='MIT',
    entry_points={
        'console_scripts': [
            'PtpUploader=PtpUploader.Main:Main',
            'ReleaseInfoMaker=PtpUploader.ReleaseInfoMaker:Main'
        ],
    }
)
