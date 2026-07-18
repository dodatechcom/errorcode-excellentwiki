---
title: "[Solution] Python FastStream Message Broker Error — How to Fix"
description: "Fix Python FastStream message broker errors. Resolve subscriber, publisher, and serialization issues."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
comments: true
weight: 5
---

# Python FastStream Message Broker Error

A `faststream.exceptions.BrokerException` or `pydantic.ValidationError` occurs when FastStream fails to connect to the message broker, encounters subscriber errors, or when message serialization fails.

## Why It Happens

FastStream is a framework for event-driven applications. Errors arise when the broker connection fails, when subscriber handlers raise exceptions, when message schemas are invalid, or when the message format is incompatible.

## Common Error Messages

- `BrokerException: Connection to broker failed`
- `SubscriberError: Subscriber handler raised exception`
- `ValidationError: Invalid message schema`
- `SerializationError: Cannot serialize message`

## How to Fix It

### Fix 1: Configure broker properly

```python
from faststream import FastStream
from faststream.nats import NATSBroker

# Wrong — no error handling
# broker = NATSBroker("nats://localhost:4222")

# Correct — configure with error handling
broker = NATSBroker(
    "nats://localhost:4222",
    max_reconnect_attempts=5,
)

@app.on_startup
async def on_startup():
    print("Broker connected")

@app.on_shutdown
async def on_shutdown():
    print("Broker disconnected")
```

### Fix 2: Handle subscriber errors

```python
from faststream import FastStream, Context
from faststream.nats import NATSBroker

broker = NATSBroker("nats://localhost:4222")

@broker.subscriber("events")
async def handle_event(msg: str, ctx: Context = Context()):
    try:
        process_event(msg)
    except Exception as e:
        print(f"Event processing failed: {e}")
        await broker.publish(f"Failed: {msg}", subject="events.dlq")

app = FastStream(broker)
```

### Fix 3: Use Pydantic models

```python
from pydantic import BaseModel
from faststream import FastStream
from faststream.nats import NATSBroker

broker = NATSBroker("nats://localhost:4222")

class UserData(BaseModel):
    name: str
    email: str

@broker.subscriber("users")
async def handle_user(msg: UserData):
    print(f"User: {msg.name}")

app = FastStream(broker)
```

## Common Scenarios

- **Broker not running** — NATS, RabbitMQ, or Kafka server not available.
- **Schema mismatch** — Incoming message does not match Pydantic model.
- **Handler exception** — Unhandled exception in subscriber callback.

## Prevent It

- Always declare message schemas using Pydantic models.
- Wrap subscriber handlers in try/except to prevent consumer crashes.
- Use `on_startup` and `on_shutdown` hooks for lifecycle management.

## Related Errors

- [BrokerException](/languages/python/broker-error/) — broker connection failed
- [SubscriberError](/languages/python/subscriber-error/) — handler failed
- [ValidationError](/languages/python/validation-error/) — schema mismatch
