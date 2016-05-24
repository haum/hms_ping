import json
import logging

import coloredlogs

from hms_ping.rabbit import RabbitClient


def get_logger():
    return logging.getLogger(__name__)


def main():
    coloredlogs.install(level='INFO')

    client = RabbitClient(exchange='haum', routing_keys=['irc_command', 'ping'])

    def callback(ch, method, properties, body):
        message = json.loads(body.decode('utf-8'))

        if method.routing_key == 'irc_command':

            # If we receive !ping from IRC we broadcast a PING request
            if message['command'] == 'ping':

                resp = {'source': 'irc', 'type': 'request'}

                get_logger().info('Sending ping {}'.format(resp))
                client.publish(routing_key='ping', dct=resp)

    client.listeners.append(callback)

    client.connect('localhost')

    try:
        client.consume()
    except KeyboardInterrupt:
        get_logger().critical('Got a KeyboardInterrupt in my face!')

    client.stop_consume()
    client.disconnect()
