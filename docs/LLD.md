# **Low Level Design (LLD) of a Real-Time Push Notification System using a Pub/Sub model**

---

# 1. Problem Statement

Design a **Real-Time Notification System** that sends **push notifications** to users instantly when events occur.

Examples:

- New message
- Order status update
- Friend request
- Payment confirmation

Requirements:

- Real-time delivery
- High throughput
- Fault tolerance
- Horizontal scalability
- Supports millions of users
- Asynchronous processing

---

# 2. High Level Architecture

```
Producers (Services)
     │
     ▼
Notification API
     │
     ▼
Message Broker (Pub/Sub)
     │
 ┌───┴──────────────┐
 ▼                  ▼
Notification Worker(s)
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

# 3. Core Components

## 1. Producer Services

Services that generate events.

Examples:

- Chat Service
- Order Service
- Payment Service

Responsibilities:

- Publish notification events
- Send message to **Notification API**

Example event structure:

```
{
  event_type: "NEW_MESSAGE",
  user_id: 123,
  payload: {...},
  timestamp: ...
}
```

---

# 4. Notification API Service

Entry point for all notifications.

Responsibilities:

- Accept events
- Validate payload
- Add metadata
- Publish to message broker

Key features:

- **Async request handling**
- Rate limiting
- Authentication

Python concept:

- Built using async frameworks like:
  - FastAPI
  - aiohttp

---

# 5. Message Broker (Pub/Sub Layer)

Central messaging system.

Possible technologies:

- Apache Kafka
- RabbitMQ
- Redis Streams
- Google Pub/Sub

Responsibilities:

- Decouple producers and consumers
- Ensure message durability
- Handle retries
- Support fan-out

Topics example:

```
notifications.email
notifications.push
notifications.sms
```

---

# 6. Notification Worker (Consumers)

Workers subscribe to topics and process notifications.

Responsibilities:

- Consume messages
- Determine notification channel
- Enrich data
- Send to delivery service

Design features:

- Async workers
- Horizontal scaling
- Batch processing

Python implementation concept:

- Async workers using:
  - asyncio
  - aiokafka
  - aio-pika

Worker flow:

```
Consume message
    ↓
Process notification
    ↓
Call Delivery Service
```

---

# 7. Delivery Service

Handles communication with external notification providers.

Responsibilities:

- Send push notification
- Handle retries
- Handle provider failures
- Maintain delivery status

Supported providers:

- Firebase Cloud Messaging (Android)
- Apple Push Notification Service (iOS)
- WebSocket for web clients

---

# 8. User Device Connection Layer

For real-time web notifications.

Technologies:

- WebSockets
- Server Sent Events

Architecture:

```
User Device
    │
WebSocket Gateway
    │
Notification Workers
```

Python libraries:

- asyncio
- websockets
- FastAPI WebSockets

---

# 9. Data Storage

Used for persistence and tracking.

### 1. User Device Tokens

Stores push tokens.

Example DB:

- PostgreSQL
- MongoDB

Schema:

```
UserDevice
-----------
user_id
device_id
push_token
platform
last_active
```

---

### 2. Notification Logs

Used for:

- analytics
- retries
- debugging

Fields:

```
notification_id
user_id
status
channel
timestamp
```

---

# 10. Retry & Failure Handling

Failures can happen due to:

- network issues
- provider downtime
- invalid device token

Retry strategy:

```
1st retry: 5 sec
2nd retry: 30 sec
3rd retry: 5 min
Dead letter queue
```

Use:

- DLQ topic in broker.

---

# 11. Async Processing Model (Python)

System heavily uses **async IO**.

Key async tasks:

```
API receives event
     ↓
Publish message asynchronously
     ↓
Worker consumes asynchronously
     ↓
Send push notification asynchronously
```

Benefits:

- Non-blocking IO
- High concurrency
- Efficient resource usage

---

# 12. Scalability Strategy

Horizontal scaling points:

1. Notification API instances
2. Broker partitions
3. Worker instances
4. WebSocket gateway nodes

Load balancing using:

- NGINX
- HAProxy

---

# 13. Rate Limiting

Prevent spam notifications.

Techniques:

- Per user limit
- Per service limit

Use:

- Redis token bucket algorithm.

---

# 14. Ordering Guarantees

Some notifications require ordering.

Solution:

- Partition messages by **user_id** in broker.

Example:

```
Partition Key = user_id
```

Ensures:

```
msg1 -> msg2 -> msg3
```

---

# 15. Observability

Monitoring tools:

- Prometheus
- Grafana

Metrics:

- notification latency
- failure rate
- queue lag
- delivery success rate

---

# 16. Security

Important security layers:

Authentication

- API keys
- OAuth tokens

Encryption

- TLS for all communications

Data protection

- encrypt device tokens

---

# 17. Bottlenecks

Potential bottlenecks:

1. Message broker overload
2. Push provider rate limits
3. Worker CPU usage
4. WebSocket connection limits

Solutions:

- broker partitioning
- autoscaling workers
- batching notifications

---

# 18. Example Flow

```
User receives new chat message
        ↓
Chat Service publishes event
        ↓
Notification API
        ↓
Kafka topic: notifications.push
        ↓
Notification Worker consumes
        ↓
Delivery Service
        ↓
FCM / APNS
        ↓
User device receives push notification
```

---

✅ This design supports:

- millions of users
- async processing
- decoupled microservices
- fault tolerance
