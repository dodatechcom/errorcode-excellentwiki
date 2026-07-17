---
title: "PubSub subscription error"
description: "Redis PubSub encounters an error when a subscriber or publisher fails to communicate on a channel"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

This error occurs when a PubSub operation fails in Redis, typically when the connection drops, the client disconnects during a subscription, or channel operations encounter protocol issues.

## Common Causes

- Subscriber connection dropped and reconnects with duplicate subscriptions
- Publishing to a channel while in subscriber mode (not allowed)
- Using a connection in both blocking and non-blocking modes simultaneously
- Subscription count mismatch after connection reset

## How to Fix

1. Handle reconnection properly in the subscriber:

```python
import redis

r = redis.Redis()
pubsub = r.pubsub()

def listen():
    while True:
        try:
            for message in pubsub.listen():
                process(message)
        except redis.ConnectionError:
            time.sleep(1)
            pubsub.subscribe("my_channel")
```

2. Never call commands on a subscribed connection — use a separate connection:

```python
import redis

r_sub = redis.Redis()
r_pub = redis.Redis()

r_sub.subscribe("my_channel")
r_pub.publish("my_channel", "hello")
```

3. Use `punsubscribe` to clean up pattern subscriptions:

```python
pubsub.punsubscribe("user:*")
```

## Examples

```python
import redis
r = redis.Redis()
r.subscribe("channel1")
r.set("foo", "bar")  # Error: can't call set from subscribed client
```

```text
redis.exceptions.ResponseError: Connection lost.
```

## Related Errors

- [WRONGTYPE Operation against a key](/tools/redis/wrong-type)
