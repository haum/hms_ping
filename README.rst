hms_ping, simple ping micro-service
###################################

This service is responsible of sending a ping command to all microservices when
a ping request is published over the different user interfaces (IRC, CLI, HTTP,
…).

The code is simple and can be used as an example of listenning/publishing
service for making other ones.

Using
-----

Create a Python 3 virtualenv and install dependencies::

    $ virtualenv -ppython3 venv
    $ source venv/bin/activate
    (venv) $ pip install -r requirements.txt

Then start the bot when you are in the repository root folder::

    $ python run.py

License
-------

This project is brought to you under MIT license. For further information,
please read the provided LICENSE file.
