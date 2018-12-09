import pika, sys

#establish the connection
connection = pika.BlockingConnection(parameters=pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

#declare direct type exchange 
channel.exchange_declare(exchange="tutorial4", exchange_type="direct")

#basically getting log type want to receive
severities  = sys.argv[1:]
if not severities:
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
    sys.exit(1)

#declare and get the name of queue
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

#create bind for each log type it want to listen
for severity in severities:
    channel.queue_bind(exchange="tutorial4", queue=queue_name, routing_key=severity)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))

channel.basic_consume(callback, queue=queue_name, no_ack=True)
channel.start_consuming()

