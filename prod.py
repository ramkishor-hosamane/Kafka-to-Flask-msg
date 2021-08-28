  
from kafka import KafkaProducer
from datetime import datetime
import time
from json import dumps
import random

# pip install kafka-python

KAFKA_TOPIC_NAME_CONS = "stackbox"
KAFKA_BOOTSTRAP_SERVERS_CONS = 'localhost:9092'

if __name__ == "__main__":
    print("Kafka Producer Application Started ... ")

    kafka_producer_obj = KafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS_CONS,
                                       value_serializer=lambda x: x.encode('utf-8'))

    message = None
    for i in range(500):
        i = i + 1
        message = "My number is "+str(i)
        print("Preparing message: " + str(i))
        print("Message: ", message)
        kafka_producer_obj.send(KAFKA_TOPIC_NAME_CONS, message)
        time.sleep(2)

    # print(message_list)

    print("Kafka Producer Application Completed. ")