hms_ping, simple ping micro-service
########

This service is, ATM, listenning for IRC commands and send a "Quoi !?! >_<" PRIVMSG if
the command is a ping.

The code is simple and can be used as an example of listenning/publishing
service for making other ones.

Using
-----

Create a Python 3 virtualenv and install dependencies::

    $ virtualenv -ppython3 venv
    $ source venv/bin/activate
    (venv) $ pip install -r requirements.txt

Then start the bot when you are in the repository root folder::

    $ python pong.py

License
-------

This project is brought to you under MIT license. For further information,
please read the provided LICENSE file.
