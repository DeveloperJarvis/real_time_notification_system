# Sequence Diagrams – Real-Time Notification System

This document describes the **sequence flows** for a **Real-Time Notification System** using a **Pub/Sub architecture**. Sequence diagrams illustrate how different components interact to deliver notifications to users.

---

# 1. Push Notification Flow

This sequence describes how a **push notification** is generated and delivered to a user device.

```id="seq01"
Producer Service      Notification API      Message Broker      Worker        Delivery Service      Push Gateway      User Device
       |                     |                    |                 |                 |                   |                |
       |  Event Triggered    |                    |                 |                 |                   |                |
       |-------------------->|                    |                 |                 |                   |                |
       |                     | Validate Request   |                 |                 |                   |                |
       |                     |------------------->| Publish Event   |                 |                   |                |
       |                     |                    |---------------->| Consume Event   |                   |                |
       |                     |                    |                 |---------------->| Send Notification |                |
       |                     |                    |                 |                 |------------------>| Deliver Push   |
       |                     |                    |                 |                 |                   |--------------->|
       |                     |                    |                 |                 |                   | Notification   |
```

---

# 2. WebSocket Real-Time Notification Flow

This sequence shows how notifications are delivered **instantly to web clients using WebSockets**.

```id="seq02"
User Device      WebSocket Gateway      Worker        Message Broker      Notification API      Producer Service
     |                  |                  |               |                   |                    |
     | Open Connection  |                  |               |                   |                    |
     |----------------->| Register User    |               |                   |                    |
     |                  |----------------->|               |                   |                    |
     |                  |                  |               |                   |                    |
     |                  |                  |               |                   | Event Triggered    |
     |                  |                  |               |<------------------|--------------------|
     |                  |                  | Consume Event |                   |                    |
     |                  |<-----------------|---------------|                   |                    |
     | Receive Push     | Send Notification|               |                   |                    |
     |<-----------------|                  |               |                   |                    |
```

---

# 3. Notification Retry Flow

This sequence shows what happens when notification delivery fails.

```id="seq03"
Worker      Delivery Service      Push Provider      Retry Scheduler      Dead Letter Queue
  |               |                     |                    |                    |
  | Send Request  |                     |                    |                    |
  |-------------->|                     |                    |                    |
  |               | Send Push           |                    |                    |
  |               |-------------------->|                    |                    |
  |               |   Failure           |                    |                    |
  |               |<--------------------|                    |                    |
  | Retry Logic   |                     |                    |                    |
  |-------------->| Schedule Retry      |                    |                    |
  |               |-------------------->| Wait Interval      |                    |
  |               |                     | Retry Notification |                    |
  |               |----------------------------------------->|                    |
  |               |                     |                    | After max retries  |
  |               |----------------------------------------->|------------------->|
```

---

# 4. Device Registration Flow

Before receiving notifications, a device must register its **push token**.

```id="seq04"
User Device      Mobile App      Notification API      Database
     |                |                 |                 |
     | Login          |                 |                 |
     |--------------->|                 |                 |
     | Generate Token |                 |                 |
     |--------------->| Send Token      |                 |
     |                |---------------->| Store Token     |
     |                |                 |---------------->|
     |                |                 | Success         |
     |                |<----------------|                 |
     | Registration Complete            |                 |
```

---

# 5. Multi-Channel Notification Flow

Some notifications may be sent through **multiple channels**.

Example:

- Push
- Email
- SMS

```id="seq05"
Worker        Channel Router        Push Service        Email Service        SMS Service
  |                  |                    |                   |                   |
  | Receive Event    |                    |                   |                   |
  |----------------->| Determine Channel  |                   |                   |
  |                  |------------------->| Send Push         |                   |
  |                  |------------------------------->| Send Email              |
  |                  |---------------------------------------------->| Send SMS  |
  |                  |                    |                   |                   |
```

---

# 6. Event Publishing Flow

This sequence shows how producer services publish notification events.

```id="seq06"
Producer Service      Notification API      Message Broker
       |                     |                    |
       | Event Generated     |                    |
       |-------------------->| Validate Event     |
       |                     |------------------->|
       |                     | Publish to Topic   |
       |                     |                    |
```

---

# 7. Complete End-to-End Flow

A full system flow from event generation to user notification.

```id="seq07"
Producer → Notification API → Broker → Worker → Delivery Service → Push Gateway → User Device
```

Steps:

1. Producer generates event.
2. Notification API validates event.
3. Event published to broker topic.
4. Worker consumes event.
5. Worker sends notification to delivery service.
6. Delivery service calls push provider.
7. User device receives notification.

---

# Key Benefits of This Flow

- **Loose coupling** between services
- **Asynchronous event processing**
- **High scalability**
- **Fault tolerance through retries**
- **Support for multiple notification channels**

---

# Author

**Developer Jarvis** _(Pen Name)_
GitHub: https://github.com/DeveloperJarvis
