import json
import time
import requests
from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable

API_KEY = "28b0c11cba934ebcaac44641262101"
CITY = "Erode"
URL = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}&aqi=no"

while True:
    try:
        producer = KafkaProducer(
            bootstrap_servers=['kafka:9092'],
            value_serializer=lambda v : json.dumps(v).encode('utf-8')
        )
        print("Producer connected to kafka")
        break
    except NoBrokersAvailable:
        print("Kafka not ready for producer, retrying...")
        time.sleep(5)
while True:
    try:
        response = requests.get(URL)
        data = response.json()
        producer.send('weather', data)
        producer.flush()
        print(f"Sent weather data:", data['current']['temp_c'], "°C")
        time.sleep(10)
    except Exception as e:
        print(f"Producer Error: {e}")