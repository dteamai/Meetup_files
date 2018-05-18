from kafka import KafkaProducer
import time

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

while 1:
  producer.send('docker1', b'https://www.wattpad.com/story/62773139-cannot-share-you')
  time.sleep(5)

producer.flush()

