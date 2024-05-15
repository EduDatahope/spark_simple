import json
import time

from confluent_kafka import Producer,Consumer, OFFSET_BEGINNING ,TopicPartition
import socket

conf ={
     'bootstrap.servers': 'pkc-12576z.us-west2.gcp.confluent.cloud:9092',
     'auto.offset.reset': 'latest',
     'group.id' : 'rg1',
     'security.protocol': 'SASL_SSL',
     'sasl.mechanism':   'PLAIN',
     'sasl.username':  'L2PZVBNNWHP4ZQCG',
     'enable.auto.commit': 'false',
     'sasl.password':  'T5KUdgBrqxWuhVTpKfg3RvP3qrKCJDO4uHBH47jxmu/hQRIk77U477SmktCbfr5R',
     
}

topic = "comanda"

consumer = Consumer(conf)
consumer.subscribe([topic])
consumer.list_topics().topics

res = list()

print("Gonna start listening")

while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue
    
    consumed_message = msg.value()
    d = json.loads(consumed_message)
    res.append(d)
    
    print('Received message: key={}, value={}'.format(msg.key(), msg.value()))
    print(f"Total ordenes recibidas {len(res)} :D")
    