import generator
import os
from concurrent import futures
from google.cloud import pubsub_v1

project_id = os.environ.get("PROJECT_ID")
topic_id = os.getenv("TOPIC_ID")

topic_path = f"projects/{project_id}/topics/{topic_id}"

publisher = pubsub_v1.PublisherClient()
future = publisher.publish(topic_path, b'Test', timeout=15)
future.result()

if __name__ == '__main__':
    data = (generator.generate_a_message())
