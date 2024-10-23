# -*- coding: utf-8 -*-

# Learn more: https://github.com/XMed07/pyMultiwii.git

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pyMultiwii',
    version='0.1.0',
    description='MultiWii Serial Protocol package for Python3',
    long_description=readme,
    author='',
    author_email='',
    url='https://github.com/XMed07/pyMultiwii.git',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

