
from hw2.models import Contacts
import time

import pika


credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='email_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


# Функція для імітації відправлення email
def send_email_to_contact(contact_id):
    contact = Contacts.objects.get(id=contact_id)
    print(f"Email відправлено контакту {contact.email}")
    time.sleep(1)
    contact.send_email = True
    contact.save()

    

# Функція для обробки повідомлення з черги
def callback(ch, method, properties, body):
    contact_id = body.decode('utf-8')
    if contact_id:
        send_email_to_contact(contact_id)
    else:
        print("Некоректне повідомлення")

if __name__ == "__main__":
    channel.basic_consume(queue='email_queue', on_message_callback=callback)
    channel.start_consuming()

    