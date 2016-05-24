import json
import logging

from hms_ping.rabbit import RabbitClient


def get_logger():
    return logging.getLogger(__name__)


client = RabbitClient(exchange='haum', routing_keys=['ping'])


def callback(ch, method, properties, body):
    if method.routing_key == 'ping':
        msg = json.loads(body.decode('utf-8'))

        if msg['type'] == 'answer' and msg['source']['source'] == 'cli':
            print('Le service `{}` a répondu présent !'.format(msg['name']))


client.listeners.append(callback)


client.connect('localhost')

print('Envoi d’une demande de ping…')
client.publish('ping', {'type': 'request', 'source': 'cli'})

try:
    print('Attente des réponses… (^C pour terminer)')
    client.consume()
except KeyboardInterrupt:
    client.stop_consume()
    client.disconnect()
