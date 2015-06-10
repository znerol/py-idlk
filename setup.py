from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from setuptools import setup

setup(
    name='idlk',
    version='0.0.1',
    description='idlk lock filename generator',
    author='Lorenz Schori',
    author_email='lo@znerol.ch',
    packages=['idlk'],
    test_suite="idlk.test",
    zip_safe=True
)
