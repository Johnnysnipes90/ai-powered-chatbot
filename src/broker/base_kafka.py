from confluent_kafka import Producer, Consumer
import logging
from src.config.settings import settings

logging.basicConfig(level=logging.INFO)

class KafkaProducer:
    def __init__(self):
        self.producer = Producer({"bootstrap.servers": settings.kafka_broker})

    def send_message(self, key: str, message: str):
        self.producer.produce(settings.kafka_topic, key=key, value=message)
        self.producer.flush()
        logging.info(f"Message sent to {settings.kafka_topic}: {message}")

class KafkaConsumer:
    def __init__(self, group_id="chat-consumer"):
        self.consumer = Consumer({
            "bootstrap.servers": settings.kafka_broker,
            "group.id": group_id,
            "auto.offset.reset": "earliest",
        })
        self.consumer.subscribe([settings.kafka_topic])

    def consume_messages(self):
        while True:
            msg = self.consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                logging.error(f"Kafka error: {msg.error()}")
                continue
            logging.info(f"Received message: {msg.value().decode('utf-8')}")