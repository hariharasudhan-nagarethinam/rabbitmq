import pika, sys
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

#get input from sys argv else default
message = ' '.join(sys.argv[1:]) or "info: Hello World!"

"""
send message to the exchange called tutorial3 which send the message to all the 
connected queues 
"""
channel.basic_publish(exchange='tutorial3',
                      routing_key='',
                      body=message)
                      
print(" [x] Sent %r" % message)




