import pika, sys

#Establish rabbitMQ connection
connection = pika.BlockingConnection(parameters=pika.ConnectionParameters(host="localhost"))
#wrapper for interacting with rabbitmq
channel = connection.channel()

#make sure queue exists
queue_name = "tutorial2"
#durable flag helps queue should persist even rabbitmq server fails/shutdowns
channel.queue_declare(queue="tutorial2", durable=True)

#insted of sending real task mock the task time in seconds
task_time = ''.join(sys.argv[1:]) if sys.argv[1:] else 2

#send task to the queue using default/nameless exchange type
#delivery_mode2 make sure that message will be persist even if rabbitmq server fails/shutdowns
channel.basic_publish(exchange='', routing_key=queue_name, body=task_time, properties=pika.BasicProperties(delivery_mode=2))
print("X sent", task_time)

#close the channel
channel.close()
