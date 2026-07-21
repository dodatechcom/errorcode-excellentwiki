---
title: "[Solution] FastAPI Broker Error -- How to Fix"
description: "Fix FastAPI message broker errors. Resolve Redis/RabbitMQ connection and message handling issues."
frameworks: ["fastapi"]
error-types: ["infrastructure-error"]
severities: ["error"]
weight: 5
comments: true
---

A FastAPI broker error occurs when the message broker (Redis, RabbitMQ, etc.) cannot be reached or process messages correctly.

## Why It Happens

Broker errors happen due to connection failures, authentication issues, memory limits, or message format problems.

## Common Error Messages

```
ConnectionRefusedError: [Errno 111] Connection refused
```

```
AMQPConnectionError: Could not connect to broker
```

```
redis.exceptions.AuthenticationError: invalid password
```

```
kombu.exceptions.EncodeError: Object not JSON serializable
```

## How to Fix It

### 1. Configure Broker Connection

Set up broker with proper settings.

```python
from kombu import Connection, Exchange, Queue

# Redis broker
broker_url = 'redis://localhost:6379/0'

# RabbitMQ broker
broker_url = 'amqp://guest:guest@localhost:5672//'

broker = Connection(broker_url)
broker.connect()
```

### 2. Handle Broker Failures

Add connection retry logic.

```python
import time
from kombu.exceptions import OperationalError

def connect_with_retry(broker_url, max_retries=10, delay=5):
    for attempt in range(max_retries):
        try:
            conn = Connection(broker_url)
            conn.connect()
            return conn
        except OperationalError as e:
            logger.warning(f'Connection failed (attempt {attempt + 1}): {e}')
            time.sleep(delay)
    raise Exception('Could not connect to broker')
```

### 3. Monitor Broker Health

Track broker status and queue depths.

```python
# Redis monitoring
import redis
r = redis.Redis()
info = r.info('memory')
queue_length = r.llen('celery')

# RabbitMQ monitoring
import requests
response = requests.get('http://localhost:15672/api/queues', auth=('guest', 'guest'))
```

### 4. Implement Dead Letter Queue

Handle failed messages.

```python
from kombu import Exchange, Queue

exchange = Exchange('tasks', type='direct')
dlx_exchange = Exchange('tasks_dlx', type='direct')

task_queue = Queue(
    'tasks',
    exchange,
    routing_key='task',
    queue_arguments={
        'x-dead-letter-exchange': 'tasks_dlx',
        'x-dead-letter-routing-key': 'failed'
    }
)
```

## Common Scenarios

**Scenario 1: Broker connection refused.**
Check broker server is running.

**Scenario 2: Authentication failed.**
Verify credentials in broker URL.

**Scenario 3: Messages piling up.**
Check consumer processing speed.

## Prevent It

1. **Monitor broker metrics.**
Track queue depth and memory.

2. **Use connection pooling.**
Limit concurrent connections.

3. **Implement health checks.**
Add broker health endpoint.

