import json
import time
import requests

from confluent_kafka.serialization import SerializationContext, MessageField
from confluent_kafka.schema_registry.json_schema import JSONDeserializer
from confluent_kafka import Consumer

topic = "comanda"

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

##-------------------------

def get_schema():
    schema_str = """
  {
    "$id": "https://example.com/complex-object.schema.json",
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "Complex Object",
    "type": "object",
    "properties": {
      "store": {
        "type": "string"
      },
      "number_store": {
        "type": "integer",
        "minimum": 0
      },
      "id_ticket" : {
        "type":"string"
      },
      "products": {
        "type": "object",
        "properties": {
          "street": {
            "main_product": "string"
          },
          "complement": {
            "type": "string"
          },
          "drinks": {
            "type": "string"
          },
          "dessert": {
            "type": "string"
          }
        },
        "required": ["main_product"]
      },
      "comments": {
        "type": "array",
        "items": {
          "type": "string"
        }
      }
    },
    "required": ["store", "number_store","id_ticket","products"]
  } 
    """
    return schema_str

class User(object):
    def __init__(self, store, number_store,id_ticket,products,comments):
        self.store = store
        self.number_store = number_store
        self.id_ticket = id_ticket
        self.products = products
        self.comments = comments


def dict_to_user(obj, ctx):
    if obj is None:
        return None

    return User(obj["store"], obj["number_store"], obj["id_ticket"], obj["products"], obj["comments"])

##------------

def main():

    consumer = Consumer(conf)
    consumer.subscribe([topic])

    while True:
        try:
            msg = consumer.poll(1.0)

            if msg is None:
                continue
            user = msg.value()

        except Exception as e:
            print("Exception in consumer is ", e)
            break
        else:
            print("The user is ", user)

    consumer.close()


if __name__ == "__main__":
    print("Gonna start listening")
    main() 