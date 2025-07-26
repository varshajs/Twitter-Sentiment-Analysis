# tweet_streamer.py
import socket
import time
from faker import Faker
import random

fake = Faker()
keywords = ['Python', 'AI', 'Elections', 'ChatGPT', 'Climate', 'Sports', 'Tech']

host = 'localhost'
port = 5555

# Create and bind socket
server_socket = socket.socket()
server_socket.bind((host, port))
server_socket.listen(5)
print(f"📡 Streaming fake tweets on {host}:{port}...")

# Accept connection from sentiment_analysis.py
client_socket, address = server_socket.accept()
print(f"✅ Connection from: {address}")

# Start sending fake tweets
while True:
    tweet = f"{fake.sentence()} #{random.choice(keywords)}"
    print(f"> Sending: {tweet}")
    # 🔥 FIX: Add newline so Spark reads each tweet properly
    client_socket.send((tweet + "t_end\n").encode('utf-8'))
    time.sleep(1)  # Simulate real-time tweet delay

