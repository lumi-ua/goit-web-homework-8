from hw2.models import Contacts
import pika

from faker import Faker


credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()


channel.queue_declare(queue="email_queue", durable=True)

fake = Faker()


contacts = []
for i in range(10):
    contacts.append({
        "fullname": fake.name(),
        "email": fake.email(), 
        "sent_email": False,    
    })

for contact_data in contacts:
    contact = Contacts(**contact_data)
    contact.save()

    
    channel.basic_publish(
    exchange='',
    routing_key='email_queue',
    body=str(contact.id).encode(), #здесь записываем либо в джсон либо в монго бд или постгрес іd объекта
    properties=pika.BasicProperties(
        delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
    ))
 

print("10 контактів було створено та відправлено у чергу")

connection.close()