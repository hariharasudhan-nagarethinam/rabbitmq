import pika

#Establish rabbitMQ connection
connection = pika.BlockingConnection(parameters=pika.ConnectionParameters(host="localhost"))
#wrapper for interacting with rabbitmq
channel = connection.channel()

#make sure queue exists
queue_name = "tutorial1"
channel.queue_declare(queue="tutorial1")

def callback(ch, method, properties, body):
    print("x receieved", body)

#register consumer with callback using no_ack=False
channel.basic_consume(callback, queue=queue_name, no_ack=True)
print("x waiting for incoming messages, press CTNL+C to exit")

#start consuming
channel.start_consuming()