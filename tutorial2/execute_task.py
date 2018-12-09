import pika, time

#Establish rabbitMQ connection
connection = pika.BlockingConnection(parameters=pika.ConnectionParameters(host="localhost"))
#wrapper for interacting with rabbitmq
channel = connection.channel()

#make sure queue exists
queue_name = "tutorial2"
#durable flag helps queue should persist even rabbitmq server fails/shutdowns
channel.queue_declare(queue="tutorial2", durable=True)

def callback(ch, method, properties, body):
    print("X received the task")
    time.sleep(int(body))
    print("X completed the task in", body, "seconds" )
    #this below line make sure that rabbitmq won't send another task while its executing the current task
    return channel.basic_ack(delivery_tag=method.delivery_tag)

#consume tasks
channel.basic_consume(callback, queue=queue_name)
print("X waiting to receive tasks")
channel.start_consuming()

