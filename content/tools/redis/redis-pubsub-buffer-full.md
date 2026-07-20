---
title: "[Solution] Redis Pub/Sub Client Buffer Full Error"
description: "How to fix Redis Pub/Sub client output buffer full errors"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Subscriber consuming messages too slowly
- Buffer limit exceeded for subscriber
- Network congestion causing message buildup

## Fix

Check buffer configuration:

```bash
redis-cli CONFIG GET client-output-buffer-limit
```

Increase buffer for pub/sub clients:

```bash
redis-cli CONFIG SET client-output-buffer-limit "pubsub 0 0 0"
```

Monitor client buffer:

```bash
redis-cli CLIENT LIST
```

Speed up subscriber processing:

```python
pubsub = r.pubsub()
pubsub.subscribe('channel')
for message in pubsub.listen():
    process(message)  # Fast processing
```

## Examples

```bash
# Check buffer config
redis-cli CONFIG GET client-output-buffer-limit

# Monitor client output
redis-cli CLIENT LIST | grep pubsub

# Check buffer usage
redis-cli INFO clients | grep client_recent_max_output_buffer_size
```
