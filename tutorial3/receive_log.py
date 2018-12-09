import pika
"""
this tutorial for sending and receiving messages to all the 
available queue bind to the fallout exchange type
"""

#Establish rabbitMQ connection
connection = pika.BlockingConnection(parameters=pika.ConnectionParameters(host="localhost"))
#wrapper for interacting with rabbitmq
channel = connection.channel()

#make sure exchange exists
channel.exchange_declare(exchange='tutorial3', exchange_type='fanout')

"""
since exchange will send message to all the queue lets rabbitmq create queue for us
as long as the receiver gets connected, exclusive gets deleted as soon as consumer disconnected
"""
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

#bind the queue with exchange then only exchange will send messages to this queue
channel.queue_bind(exchange='tutorial3', queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()