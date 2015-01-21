import os
import re

from setuptools import setup

def get_version():
    version_file = os.path.join(
        os.path.dirname(__file__), 
        'issac', 
        '__init__.py'
    )
    with open(version_file) as f:
        regex = re.compile("^__version__.*?(?P<version>[\d.]+).*")
        for line in f.readlines():
            m = regex.match(line)
            if m:
                return m.group("version")

setup(
    name="issac",
    version=get_version(),
    description="A password checker that uses the natural rainbow table that is Google Search for validation.",
    long_description=open("README.rst").read(),
    url="https://github.com/danielquinn/issac/",
    author="Daniel Quinn",
    author_email="code@danielquinn.org",
    license="AGPL3",
    packages=[
        "issac",
    ],
    scripts=[
        "bin/issac",
    ],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Natural Language :: English",
        "Operating System :: OS Independent",
    ]
)

