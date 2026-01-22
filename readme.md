# 🌐 Real-Time Weather Streaming System with Kafka & PostgreSQL

This repository showcases a real-time weather data ingestion system built using Apache Kafka, PostgreSQL, and Python, fully containerized with Docker Compose.
The pipeline continuously collects live weather data, streams it through Kafka, and persists it into a relational database for analytics and machine learning use cases.

**📌 Project Summary**

Weather data is collected at regular 5-second intervals

Kafka is used for high-throughput message streaming

A consumer service processes and stores data reliably

PostgreSQL acts as a persistent analytical datastore

Entire system runs in isolated Docker containers

**🏗️ System Flow**

Weather API
→ Kafka Producer
→ Kafka Topic
→ Kafka Consumer
→ PostgreSQL Database

**⚙️ Technology Stack**

Python 3.10

Apache Kafka (Confluent Image)

PostgreSQL 14

Docker & Docker Compose

kafka-python

psycopg2

pandas (for downstream analysis)

**🧩 Microservices Breakdown**

Zookeeper – Manages Kafka metadata

Kafka Broker – Handles real-time messaging

Weather Producer – Publishes API data to Kafka

Weather Consumer – Reads messages and inserts into DB

PostgreSQL – Stores structured weather records

**✨ Core Highlights**

Controlled producer–consumer execution using timers

Kafka poll()-based consumption for reliability

Automatic database table initialization

Docker-network-friendly service communication

Scalable foundation for analytics & ML pipelines

**▶️ Running the Project**

Step 1: Launch all services
docker-compose up --build -d

Step 2: Check container status
docker ps

Step 3: Query stored weather data
docker exec -it postgres psql -U user -d nrdb
SELECT * FROM weather_data;

**🗄️ Database Schema**
weather_data (
  id SERIAL PRIMARY KEY,
  city TEXT,
  temperature FLOAT,
  condition TEXT,
  timestamp TIMESTAMP
)

**📚 What This Project Demonstrates**

End-to-end real-time data streaming

Kafka-based event-driven architecture

Dockerized microservice design

Python integration with distributed systems

Practical groundwork for ML models & dashboards

**🚀 Possible Extensions**

Include humidity, wind speed, and pressure

Time-window aggregation using Kafka Streams

Streamlit or Power BI dashboard

Kafka KRaft (Zookeeper-free) migration

Predictive weather modeling using stored data

**👨‍🎓 About Me**

Sharvesh
B.Tech – Artificial Intelligence & Data Science

Interested in Data Engineering, ML Systems & Distributed Computing
