from src.broker.base_kafka import KafkaProducer, KafkaConsumer
import threading
import time

# Start consumer in a separate thread
def start_consumer():
    consumer = KafkaConsumer()
    consumer.consume_messages()

threading.Thread(target=start_consumer, daemon=True).start()

# Send test message
producer = KafkaProducer()
producer.send_message("test-key", "Hello, Kafka!")

time.sleep(5)