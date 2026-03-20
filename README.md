# Real-Time Notification System (Pub/Sub Model)

A scalable **Real-Time Push Notification System** built using a **Publish–Subscribe (Pub/Sub) architecture** with **asynchronous processing**. This project focuses on system design principles such as **event-driven architecture, messaging systems, and async I/O**, making it suitable for large-scale distributed applications.

---

# How to Run the Project

## Docker compose build

```bash
docker compose up --build
# up: starts all services
# --build: rebuilds your images (important after code changes)
docker compose up -d --build
# -d: run in background (detached mode)

# Stop everything
docker compose down
```

### 1️⃣ Setup

```bash
# setup.py
pip install -e .
# install dependencies
pip install -r requirements.txt
```

### 2️⃣ Start infrastructure

```bash
docker-compose up
# This starts
# - Kafka
# - PostgreSQL
# - Redis
```

### 3️⃣ Run the notification system

```bash
python main.py
```

## API Example

```bash
POST /notifications/send
```

Headers

```bash
x-api-key: super-secret-key
```

Body

```json
{
  "user_id": "123",
  "event_type": "NEW_MESSAGE",
  "channel": "push",
  "payload": {
    "sender": "user456",
    "message": "Hello!"
  }
}
```

---

## ✨ Overview

This project demonstrates the **Low-Level Design (LLD)** of a notification system capable of delivering real-time push notifications to millions of users. It uses a **decoupled microservice architecture** where producers publish events and consumers process and deliver notifications asynchronously.

Typical use cases include:

- 💬 New chat message notifications
- 🛒 Order status updates
- 👥 Friend request alerts
- 💳 Payment confirmations

The system ensures **high throughput, scalability, and fault tolerance** while maintaining real-time delivery guarantees.

---

## 🏗 System Architecture

```
Producers (Services)
      │
      ▼
Notification API
      │
      ▼
Message Broker (Pub/Sub)
      │
 ┌────┴───────────────┐
 ▼                    ▼
Notification        Workers
      │
      ▼
Delivery Service
      │
      ▼
Push Gateway (FCM / APNS / WebSockets)
      │
      ▼
User Devices
```

---

# Final Architecture

```
Producers Services
      │
      ▼
Notification API
      │
      ▼
Kafka Topics
      │
      ▼
    Workers
      │
      ▼
Delivery Services
      │
      ▼
Push / Email / SMS
      │
      ▼
User Devices
```

---

## ⚙ Core Components

### 1. Producer Services

Services that generate notification events.

Examples:

- Chat Service
- Order Service
- Payment Service

These services publish events to the **Notification API**, which forwards them to the messaging layer.

---

### 2. Notification API

Acts as the **entry point for all notification events**.

Responsibilities:

- Validate incoming requests
- Enrich event metadata
- Publish messages to the broker
- Handle authentication and rate limiting

---

### 3. Message Broker

Responsible for **decoupling producers and consumers** using the Pub/Sub pattern.

Features:

- Message durability
- Event streaming
- Horizontal scalability
- Fan-out delivery

Example topics:

```
notifications.push
notifications.email
notifications.sms
```

---

### 4. Notification Workers

Consumers that subscribe to broker topics and process notifications.

Responsibilities:

- Consume events
- Determine notification channel
- Enrich message payload
- Send notifications to the Delivery Service

Workers can scale horizontally to process large volumes of messages.

---

### 5. Delivery Service

Handles communication with external notification providers.

Responsibilities:

- Send push notifications
- Handle delivery failures
- Retry failed messages
- Maintain delivery status

---

### 6. Device Connection Layer

For web-based real-time notifications.

Possible technologies:

- WebSockets
- Server-Sent Events (SSE)

This layer maintains active connections with client devices to push notifications instantly.

---

## 🗄 Data Storage

### User Device Tokens

Stores device information for sending push notifications.

Example fields:

```
user_id
device_id
push_token
platform
last_active
```

---

### Notification Logs

Used for monitoring, analytics, and retries.

Example fields:

```
notification_id
user_id
status
channel
timestamp
```

---

## 🔁 Retry & Failure Handling

Failures can occur due to:

- Network issues
- Provider downtime
- Invalid device tokens

Retry strategy example:

```
1st Retry → 5 seconds
2nd Retry → 30 seconds
3rd Retry → 5 minutes
```

Failed messages are sent to a **Dead Letter Queue (DLQ)** for further inspection.

---

## ⚡ Async Processing

The system relies heavily on **asynchronous I/O** to achieve high concurrency and efficient resource utilization.

Event flow:

```
API receives event
     ↓
Publish message asynchronously
     ↓
Worker consumes event
     ↓
Send push notification asynchronously
```

Benefits:

- Non-blocking processing
- High throughput
- Efficient CPU utilization

---

## 📈 Scalability

The system supports horizontal scaling at multiple layers:

- Notification API instances
- Message broker partitions
- Worker services
- WebSocket gateway nodes

Load balancing ensures even distribution of requests across instances.

---

## 📊 Observability

Monitoring and metrics are essential for reliability.

Key metrics to track:

- Notification delivery latency
- Queue lag
- Failure rate
- Delivery success rate

These metrics help maintain system performance and identify bottlenecks.

---

## 🔐 Security

Security considerations include:

- API authentication (API keys / OAuth)
- TLS encryption for communication
- Secure storage of device tokens
- Rate limiting to prevent abuse

---

## 🚧 Potential Bottlenecks

Possible bottlenecks in the system include:

- Broker overload
- Push provider rate limits
- Worker CPU exhaustion
- High WebSocket connection counts

Mitigation strategies:

- Broker partitioning
- Worker autoscaling
- Message batching
- Connection sharding

---

## 📌 Example Event Flow

```
User receives new chat message
        ↓
Chat Service publishes event
        ↓
Notification API
        ↓
Broker topic: notifications.push
        ↓
Notification Worker consumes event
        ↓
Delivery Service
        ↓
Push Gateway
        ↓
User device receives notification
```

---

## 🎯 Key Design Principles

- Event-driven architecture
- Asynchronous processing
- Loose coupling via Pub/Sub
- Fault tolerance with retries and DLQ
- Horizontal scalability

---

## 👨💻 Author

**Developer Jarvis**
_Pen Name_

🔗 GitHub: https://github.com/DeveloperJarvis

---

⭐ If you found this project helpful, consider giving it a **star on GitHub**!
