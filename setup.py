"""
A setuptools based setup module's Nextpay.ir
See:
https://nextpay.ir
https://nextpay.ir/plugins
https://github.com/nextpay-ir/nextpay-python-sample-code
"""

import os
from os import path
from setuptools import find_packages, setup
from codecs import open

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name='nextpay',
    version='0.1.1',
    packages=find_packages(),
    test_suite='nextpay.tests',
    include_package_data=True,
    author='Nextpay Groups',
    author_email='info@nextpay.ir',
    license='MIT',
    description='Python library for nextpay payment gateway.',
    long_description=long_description,
    url='https://nextpay.ir',
    classifiers=[
        'Environment :: Console',
        'Environment :: Web Environment',
        'Operating System :: Microsoft',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',

    ],
    keywords='nextpay payment gateway nextpay.ir library',
)
