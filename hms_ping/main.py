import logging

import coloredlogs

from hms_base.client import Client
from hms_base.decorators import topic


def get_logger():
    return logging.getLogger(__name__)


def main():
    coloredlogs.install(level='INFO')

    client = Client('hms_ping', 'haum', topics=['irc_command'])

    @topic('irc_command')
    def irc_callback(client, topic, dct):
        """Callback used when we receive a !ping commad from IRC.

        When called, we broadcast a PING request specifying that the request
        comes from IRC and user's nickname in order to send him all the ping
        responses and avoid spamming main IRC channel.

        """
        if dct['command'] == 'ping':

            ping_request = {
                'source': 'irc',
                'type': 'request',
                'nick': dct['nick']
            }

            get_logger().info('Sending ping {}'.format(ping_request))
            client.publish('ping', dct=ping_request)

    client.listeners.append(irc_callback)
    client.connect()

    try:
        client.start_consuming()
    except KeyboardInterrupt:
        get_logger().critical('Got a KeyboardInterrupt in my face!')

    client.stop_consuming()
    client.disconnect()
