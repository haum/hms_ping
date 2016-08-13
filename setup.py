from distutils.core import setup

from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='hms_ping',
    version='2.0',
    packages=['hms_ping'],
    scripts=['bin/hms_ping', 'bin/hms_ping_send'],

    url='https://github.com/haum/hms_ping',
    license='MIT',

    author='Romain Porte (MicroJoe)',
    author_email='microjoe@microjoe.org',

    description='HAUM’s ping microservice',
    long_description=long_description,

    classifiers = [
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',

        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    install_requires=['pika', 'hms_base>1.0,<2', 'coloredlogs']
)
