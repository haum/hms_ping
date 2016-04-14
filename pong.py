import pika
import json

conn = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = conn.channel()

# Déclaration de l’échangeur
channel.exchange_declare(exchange='haum',
                         type='direct')

# Création de la queue de réception de messages et récupération du nom généré
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

# Bind entre l’échangeur et notre queue de réception
channel.queue_bind(exchange='haum',
                   queue=queue_name, routing_key='irc_command')

print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    result = json.loads(body.decode('utf-8'))
    print(result)

    if result['command'] == 'ping':
        channel.basic_publish(
            exchange='haum',
            routing_key='irc_debug',
            body=json.dumps({'privmsg': 'Quoi !?! >_<'}))


channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()
