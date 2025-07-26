from kafka import KafkaProducer
from faker import Faker
import random
import time
import json

producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))

fake = Faker()
keywords = ['Python', 'AI', 'Elections', 'ChatGPT', 'Climate', 'Sports', 'Tech']

print("📡 Sending fake tweets to Kafka topic 'raw_tweets'...")
while True:
    tweet = {
        'text': f"{fake.sentence()} #{random.choice(keywords)}",
        'timestamp': time.strftime("%Y-%m-%d %H:%M:%S")
    }
    print(f"> Sending: {tweet}")
    producer.send('raw_tweets', value=tweet)
    time.sleep(1)

