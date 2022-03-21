from kafka import KafkaProducer
from kq import Queue
from config import get_settings

# Set up a Kafka producer.
producer = KafkaProducer(bootstrap_servers=get_settings().KAFKA_SERVER)

# Set up a queue.
queue = Queue(topic="topic", producer=producer)

# Enqueue a function call.
def enqueue_func(func,*args):
    job = queue.enqueue(func, *args)
    return job

