# src/rabbitmq.py
import pika

class RabbitMQ:
  def __init__(self):
    self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    self.channel = self.connection.channel()

  def send_message(self, username, message):
    self.channel.basic_publish(exchange='', routing_key='chat', body=f'{username}: {message}') # Send message using RabbitMQ
