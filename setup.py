#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
from setuptools import find_packages, setup

version                = '0.0.14'

current_dir            = os.path.abspath(os.path.dirname(__file__))
requirements           = [line.strip() for line in open(os.path.join(current_dir, 'requirements.txt'), 'r').readlines()]
version_file           = os.path.join(current_dir, 'VERSION')
readme_file            = os.path.join(current_dir, 'README.md')
long_desc              = None
long_desc_content_type = None

if os.path.isfile(version_file):
    version = open(version_file, 'r').readline().strip() or version

if os.path.isfile(readme_file):
    long_desc = open(readme_file, 'r').read()
    long_desc_content_type = 'text/markdown'

setup(
    name                          = 'fd-replay',
    version                       = version,
    description                   = 'fd-replay',
    author                        = 'Adrien Delle Cave',
    author_email                  = 'pypi@doowan.net',
    license                       = 'License GPL-2',
    url                           = 'https://github.com/decryptus/fd-replay',
    scripts                       = ['bin/fd-replay'],
    packages                      = find_packages(),
    install_requires              = requirements,
    long_description              = long_desc,
    long_description_content_type = long_desc_content_type
)
