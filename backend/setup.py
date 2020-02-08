#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

import os
from setuptools import setup, find_packages

version = os.environ.get("WEBPI_VERSION", "0.0.1")

try:
    with open("README.md") as readme_file:
        README = readme_file.read()
except FileNotFoundError:
    README = ""

REQUIREMENTS = ["flask>=1", "Flask-Login>=0.4.1", "pyyaml>=5.3"]

SETUP_REQUIREMENTS = ["pytest-runner"]

TEST_REQUIREMENTS = ["pytest"]

setup(
    author="Matej Urbas",
    author_email="matej.urbas@gmail.com",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    description="Deep release notes helps you manage release notes for your project.",
    entry_points={"console_scripts": ["webpi=webpi.app:main"]},
    install_requires=REQUIREMENTS,
    license="MIT license",
    long_description=README,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="webpi",
    name="webpi",
    packages=find_packages(include=["webpi"]),
    setup_requires=SETUP_REQUIREMENTS,
    test_suite="tests",
    tests_require=TEST_REQUIREMENTS,
    url="https://github.com/urbas/webpi",
    version=version,
    zip_safe=False,
)
