import os
from setuptools import setup

setup(
    name = "batterystaple",
    version = open(os.path.join(os.path.dirname(__file__), 'batterystaple', 'VERSION')).read().strip(),
    description = "A password checker that follows XKCD's sage advice and does some rainbow table checks on top of that.",
    long_description = open("README.rst").read(),
    url = "https://github.com/danielquinn/batterystaple/",
    author = "Danielquinn",
    author_email = "code@danielquinn.org",
    packages = [
        "batterystaple",
    ],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Natural Language :: English",
        "Operating System :: OS Independent",
    ]
)
