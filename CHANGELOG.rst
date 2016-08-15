Change Log
==========

All notable changes to this project will be documented in this file.
This project adheres to `Semantic Versioning <http://semver.org/>`__.

[Unreleased]
------------

[2.1] - 2016-08-15
------------------

- Using ``hms_base`` version 2

[2.0] - 2016-08-13
------------------

- Converted old run.py and ping.py to global executables
- Using package ``hms_base`` instead of copying its source code
- Using ``setup.py`` packaging for easier installation, dependency management
  and use
- Added systemd unit
- Added CLI ping command

[1.0] - 2016-05-24
------------------

- Interract with the RabbitMQ server using RabbitClient instead of pika stuff

[0.1] - 2016-05-20
------------------

- Basic ping microservice
