import pika, sys

#establish the connection
connection = pika.BlockingConnection(parameters=pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

#declare direct type exchange 
channel.exchange_declare(exchange="tutorial5", exchange_type="topic")

severity  = sys.argv[1] if len(sys.argv) > 2 else 'anonymous.info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'

channel.basic_publish(exchange="tutorial5", routing_key=severity, body=message)
print(" [x] Sent %r:%r" % (severity, message))
channel.close()