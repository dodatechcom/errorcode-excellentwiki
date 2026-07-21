---
title: "[Solution] RabbitMQ Dead Letter Cycle Error"
description: "Fix RabbitMQ dead letter cycle errors. Resolve infinite message loops between dead letter exchanges."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Dead Letter Cycle Error

RabbitMQ dead letter cycle errors occur when messages are routed between two or more dead letter exchanges in an infinite loop, consuming resources without resolution.

## Common Causes

- Queue A dead-letters to Queue B and vice versa
- Dead letter routing key routes back to the originating queue
- Missing message count limit on dead letter queues

## How to Fix It

### Solution 1: Add a dead letter hop count header

Track dead letter hops in the message header:

```python
# Producer sets initial header
properties = pika.BasicProperties(
    headers={"x-death-count": 0}
)
```

### Solution 2: Set max-length on dead letter queues

Prevent infinite growth:

```bash
rabbitmqadmin declare queue name=dlq max-length=10000 durable=true
```

### Solution 3: Use a message TTL on the DLQ

Discard messages that cannot be processed:

```bash
rabbitmqadmin declare queue name=dlq arguments='{"x-message-ttl": 86400000}'
```

## Prevent It

- Always include a dead letter hop counter header
- Set max-length on dead letter queues
- Monitor dead letter queue depth for anomalies
