---
title: "[Solution] Redis Pub/Sub No Subscribers Error"
description: "How to handle Redis Pub/Sub messages sent to channels with no subscribers"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- All subscribers disconnected
- Publishing before subscribing
- Channel name mismatch

## Fix

Check subscriber count:

```bash
redis-cli PUBSUB NUMSUB mychannel
```

Ensure subscriber connects first:

```python
# Subscriber must connect first
pubsub = r.pubsub()
pubsub.subscribe('mychannel')
# Then publisher sends
r.publish('mychannel', 'message')
```

Monitor subscriber count:

```bash
watch -n 1 'redis-cli PUBSUB NUMSUB mychannel'
```

## Examples

```bash
# Check subscribers
redis-cli PUBSUB NUMSUB mychannel

# List all channels with subscribers
redis-cli PUBSUB NUMSUB

# Publish and check result (returns 0 if no subscribers)
redis-cli PUBLISH mychannel "test"
```
