import json
import logging

import coloredlogs

from hms_base.client import Client
from hms_base.decorators import topic


def get_logger():
    return logging.getLogger(__name__)


def main():
    coloredlogs.install(level='INFO')

    client = Client('hms_ping', 'haum', ['irc_command', 'ping'])

    @topic('irc_command')
    def callback(client, topic, dct):
        # If we receive !ping from IRC we broadcast a PING request
        if dct['command'] == 'ping':

            resp = {
                'source': 'irc',
                'type': 'request',
                'nick': dct['nick']
            }

            get_logger().info('Sending ping {}'.format(resp))
            client.publish('ping', resp)

    client.listeners.append(callback)
    client.connect()

    try:
        client.start_consuming()
    except KeyboardInterrupt:
        get_logger().critical('Got a KeyboardInterrupt in my face!')

    client.stop_consuming()
    client.disconnect()
