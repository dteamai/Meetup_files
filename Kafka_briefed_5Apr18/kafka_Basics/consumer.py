from kafka import KafkaConsumer

consumer = KafkaConsumer('docker1',bootstrap_servers=['localhost:9092'])

for msg in consumer:
    print (msg)