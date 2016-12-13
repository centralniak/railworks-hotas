#!/usr/bin/env python

import os
import setuptools


CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Environment :: Win32 (MS Windows)',
    'Intended Audience :: End Users/Desktop',
    'License :: OSI Approved :: MIT License',
    'Operating System :: Microsoft :: Windows',
    'Programming Language :: Python',
    'Topic :: Games/Entertainment :: Simulation',
]


setuptools.setup(
    author='Piotr Kilczuk',
    author_email='piotr@tymaszweb.pl',
    name='railworks-hotas',
    version='0.1.0',
    description='A Thrustmaster T-Flight Hotas X driver for Train Simulator 2017',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    url='https://github.com/centralniak/railworks-hotas',
    license='MIT License',
    platforms=['Windows'],
    classifiers=CLASSIFIERS,
    entry_points={
        'console_scripts': [
            'railworkshotas = hotas:__main__'
        ]
    },
    install_requires=open('requirements.txt').read(),
    packages=setuptools.find_packages(),
    include_package_data=False,
    zip_safe=False,
)
