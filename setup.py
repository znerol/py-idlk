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
