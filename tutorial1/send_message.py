import pika, sys

#Establish rabbitMQ connection
connection = pika.BlockingConnection(parameters=pika.ConnectionParameters(host="localhost"))
#wrapper for interacting with rabbitmq
channel = connection.channel()

#make sure queue exists
queue_name = "tutorial1"
channel.queue_declare(queue="tutorial1")

#get input from sys argv else default
message = ' '.join(sys.argv[1:]) if sys.argv[1:] else "Hello World"

#send message to the queue using default/nameless exchange type
channel.basic_publish(exchange='', routing_key=queue_name, body=message)
print("X sent", message)

#close the channel
channel.close()




