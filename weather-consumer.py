import json
import time
import requests
import psycopg2
from kafka import KafkaConsumer
from kafka.errors import NoBrokersAvailable
 
while True:
    try:
        consumer = KafkaConsumer(
            'weather',
            bootstrap_servers=['kafka:9092'],
            value_deserializer=lambda x : json.loads(x.decode('utf-8')),
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='weather-group'
        )
        print("Consumer connected to kafka")
        break
    except NoBrokersAvailable:
        print("Kafka not ready for consumer, retrying in 5 seconds...")
        time.sleep(5)
while True:
    try:
        conn = psycopg2.connect(
            dbname="bsdb",
            user="user",
            password="password",
            host="postgres",
            port="5432"
        )
        cursor = conn.cursor()
        break
    except Exception as e:
        print("PostgreSQL not ready, retrying in 5 seconds...")
        time.sleep(5)

cursor.execute("""
CREATE TABLE IF NOT EXISTS weather_data (
        id SERIAL PRIMARY KEY,
        city TEXT,
        temperature FLOAT,
        condition TEXT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")
conn.commit()

#consume messages
for message in consumer:
    data = message.value
    try:
        city = data['location']['name']
        temp= data['current']['temp_c']
        condition = data['current']['condition']['text']
        
        cursor.execute("""
            INSERT INTO weather_data (city, temperature, condition)
            VALUES (%s, %s, %s)
        """, (city, temp, condition))
        conn.commit()

        print(f"Inserted: {city}, {temp}, {condition}")
    except Exception as e:
        print(f"Consumer Error: {e}")