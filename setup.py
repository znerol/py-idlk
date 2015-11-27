from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from setuptools import setup

setup(
    name='idlk',
    version='0.0.9',
    description='idlk lock filename generator',
    author='Lorenz Schori',
    author_email='lo@znerol.ch',
    url='https://github.com/znerol/py-idlk',
    packages=['idlk'],
    test_suite="idlk.test",
    zip_safe=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Multimedia :: Graphics'
    ]
)
