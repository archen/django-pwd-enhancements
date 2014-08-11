#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import pwdenhancements

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = pwdenhancements.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django-pwd-enhancements',
    version=version,
    description="""Additional hashers and management utilities based on best practices from OWASP's Password Storage
    Cheat Sheet https://www.owasp.org/index.php/Password_Storage_Cheat_Sheet""",
    long_description=readme + '\n\n' + history,
    author='Kevin Glavin',
    author_email='archen.sol@gmail.com',
    url='https://github.com/archen/django-pwd-enhancements',
    packages=[
        'pwdenhancements',
    ],
    include_package_data=True,
    install_requires=['scrypt'
    ],
    license="BSD",
    zip_safe=False,
    keywords='django-pwd-enhancements',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)