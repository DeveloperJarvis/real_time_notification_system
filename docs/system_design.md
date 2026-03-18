# System Design – Real-Time Notification System (Pub/Sub Model)

This document explains the **system design** of a scalable **Real-Time Notification System** that delivers push notifications to users using a **Publish–Subscribe (Pub/Sub) architecture** and **asynchronous event processing**.

---

# 1. Problem Statement

Design a system that can send **real-time notifications** to millions of users when specific events occur in the system.

Example events:

- New chat message
- Order status update
- Friend request
- Payment confirmation

The system must support:

- Real-time delivery
- High scalability
- Fault tolerance
- Asynchronous processing
- Multi-channel notifications (Push, Email, SMS)

---

# 2. Functional Requirements

1. Send push notifications instantly.
2. Support multiple notification channels:
   - Push
   - Email
   - SMS

3. Allow multiple services to generate events.
4. Ensure reliable delivery.
5. Track notification status.

---

# 3. Non-Functional Requirements

- **Low latency** (near real-time)
- **High availability**
- **Horizontal scalability**
- **Fault tolerance**
- **Message durability**
- **Observability**

---

# 4. High-Level Architecture

```id="r1kx21"
+-------------------+
|  Producer Services|
|-------------------|
| Chat Service      |
| Order Service     |
| Payment Service   |
+---------+---------+
          |
          v
+-------------------+
| Notification API  |
+---------+---------+
          |
          v
+-------------------+
|  Message Broker   |
|   (Pub/Sub)       |
+----+--------+-----+
     |        |
     v        v
+--------+  +--------+
|Workers |  |Workers |
+----+---+  +---+----+
     |          |
     v          v
+-------------------+
| Delivery Service  |
+---------+---------+
          |
          v
+-------------------+
| Push Gateways     |
| Email Providers   |
| SMS Providers     |
+---------+---------+
          |
          v
+-------------------+
|    User Devices   |
+-------------------+
```

---

# 5. Core Components

## 5.1 Producer Services

These services generate notification events.

Examples:

- Chat service → new message
- Order service → order shipped
- Payment service → payment success

Responsibilities:

- Detect events
- Send notification event to Notification API

Example event structure:

```id="qayydj"
{
  "event_type": "NEW_MESSAGE",
  "user_id": "123",
  "payload": {
      "sender": "user456",
      "message_preview": "Hello!"
  },
  "timestamp": "2026-03-15T10:00:00Z"
}
```

---

# 6. Notification API

Acts as the **central entry point** for notification requests.

Responsibilities:

- Validate event payload
- Authenticate requests
- Enrich metadata
- Publish message to broker

Key features:

- Async request handling
- Rate limiting
- Logging and monitoring

---

# 7. Message Broker (Pub/Sub)

The broker decouples **producers** from **consumers**.

Responsibilities:

- Message queuing
- Event streaming
- Load balancing
- Message durability

Example topics:

```id="pcf3qt"
notifications.push
notifications.email
notifications.sms
```

Benefits of Pub/Sub:

- Loose coupling
- Horizontal scalability
- Fault isolation
- Parallel processing

---

# 8. Notification Workers

Workers subscribe to broker topics and process notifications.

Responsibilities:

- Consume messages
- Determine notification channel
- Enrich payload
- Send to Delivery Service

Workers can scale horizontally depending on message load.

Worker flow:

```id="oylxf2"
Consume Event
     ↓
Validate Notification
     ↓
Choose Channel
     ↓
Send to Delivery Service
```

---

# 9. Delivery Service

Responsible for sending notifications through external providers.

Channels supported:

1. Push Notifications
2. Email Notifications
3. SMS Notifications

Responsibilities:

- Send notification request
- Handle delivery failures
- Retry failed attempts
- Update notification logs

---

# 10. WebSocket Gateway

For **real-time browser notifications**.

Responsibilities:

- Maintain persistent client connections
- Identify active users
- Push notifications instantly

Connection flow:

```id="auiz9s"
User Login
   ↓
Open WebSocket Connection
   ↓
Register User Session
   ↓
Receive Notifications
```

---

# 11. Database Design

## User Devices Table

Stores device tokens required for push notifications.

```id="vm6mhe"
UserDevice
----------
user_id
device_id
push_token
platform
last_active
```

---

## Notification Logs Table

Tracks notification delivery status.

```id="qqglhi"
NotificationLog
---------------
notification_id
user_id
channel
status
timestamp
retry_count
```

---

# 12. Retry Strategy

Failures can occur due to:

- Network issues
- Provider downtime
- Invalid device tokens

Retry policy:

```id="bh6wkj"
Retry 1 → 5 seconds
Retry 2 → 30 seconds
Retry 3 → 5 minutes
```

After retries fail:

```id="hoxr3j"
Message → Dead Letter Queue
```

Dead messages can be inspected later.

---

# 13. Scalability Strategy

The system scales horizontally at several layers:

| Layer             | Scaling Method     |
| ----------------- | ------------------ |
| Notification API  | Add more instances |
| Message Broker    | Partition topics   |
| Workers           | Add more consumers |
| WebSocket Gateway | Add nodes          |

This ensures the system supports **millions of notifications per minute**.

---

# 14. Ordering Guarantee

Some notifications must maintain order.

Example:

- Chat messages
- Payment events

Solution:

```id="nhtq7n"
Partition Key = user_id
```

This ensures all notifications for a user are processed sequentially.

---

# 15. Rate Limiting

Prevents spam notifications.

Strategies:

- Per-user limit
- Per-service limit
- Token bucket algorithm

Benefits:

- Protects system resources
- Prevents notification flooding

---

# 16. Observability

Monitoring is required to maintain reliability.

Important metrics:

- Notification latency
- Queue lag
- Worker throughput
- Failure rate
- Delivery success rate

Monitoring tools track system performance and detect failures early.

---

# 17. Security

Security measures include:

- API authentication
- TLS encryption
- Secure storage of device tokens
- Rate limiting and abuse prevention

---

# 18. Example Notification Flow

```id="i2d64c"
User sends message
      ↓
Chat Service detects event
      ↓
Notification API receives event
      ↓
Event published to broker topic
      ↓
Worker consumes event
      ↓
Delivery Service sends push notification
      ↓
User device receives notification
```

---

# 19. Potential Bottlenecks

Possible bottlenecks include:

- Broker overload
- Worker processing limits
- Push provider rate limits
- Too many WebSocket connections

Solutions:

- Partitioning topics
- Autoscaling workers
- Notification batching
- Connection sharding

---

# 20. Key Design Principles

The system follows these core design principles:

- **Event-driven architecture**
- **Asynchronous processing**
- **Loose coupling via Pub/Sub**
- **Horizontal scalability**
- **Fault tolerance with retries and DLQ**

These principles allow the system to support **large-scale real-time notifications reliably**.

---

# Author

**Developer Jarvis** _(Pen Name)_
GitHub: https://github.com/DeveloperJarvis
