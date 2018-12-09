import pika, sys

#establish the connection
connection = pika.BlockingConnection(parameters=pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

#declare direct type exchange 
channel.exchange_declare(exchange="tutorial4", exchange_type="direct")

severity  = ''.join(sys.argv[1:]) or "info"
message = ''.join(sys.argv[2:]) or "b'Hello World'!"

channel.basic_publish(exchange="tutorial4", routing_key=severity, body=message)
print(" [x] Sent %r:%r" % (severity, message))
channel.close()