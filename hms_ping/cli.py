import logging

from hms_base.client import Client
from hms_base.decorators import topic


def main():

    # We have to create a client to ask other clients if they are alive, but we
    # do not want our client to appear in the list, so we disable ping, but
    # we still listen to the 'ping' topic.
    client = Client('hms_ping_send', 'haum', topics=['ping'], enable_ping=False)

    @topic('ping')
    def ping_callback(client, topic, dct):
        """Callback that will react to CLI ping responses only."""

        if dct['type'] == 'answer' and dct['source']['source'] == 'cli':
            print('Le service `{}` a répondu présent !'.format(dct['name']))


    client.listeners.append(ping_callback)
    client.connect()


    try:
        print('Envoi d’une demande de ping…')

        # We send a ping request and specify the source is CLI so
        # we can then catch answers from our CLI request.
        client.publish('ping', {'type': 'request', 'source': 'cli'})

        print('Attente des réponses… (^C pour terminer)')

        # Infinite wait for answers till user decides to exit.
        # TODO: start to consume before in a thread and join here to be sure to not miss any answer.
        client.start_consuming()

    except KeyboardInterrupt:
        client.stop_consuming()
        client.disconnect()