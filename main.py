import random
import time
import generator
import os
from google.cloud import pubsub_v1

project_id = os.environ.get("PROJECT_ID")
topic_id = os.getenv("TOPIC_ID")

topic_path = f"projects/{project_id}/topics/{topic_id}"
publisher = pubsub_v1.PublisherClient()

if __name__ == '__main__':
    while True:
        data = (generator.generate_a_message())
        future = publisher.publish(topic_path, data, timeout=10)
        future.result()

        time.sleep(random.randint(1,10))
