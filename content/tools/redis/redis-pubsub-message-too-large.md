---
title: "[Solution] Redis Pub/Sub Message Too Large Error"
description: "How to fix Redis Pub/Sub message too large errors"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Message exceeds max message size
- Client buffer overflow
- Memory pressure on subscribers

## Fix

Check max message size:

```bash
redis-cli CONFIG GET maxmemory
```

Split large messages:

```python
import json
data = {"large_payload": "..." * 10000}
chunks = [data[i:i+1000] for i in range(0, len(data), 1000)]
for chunk in chunks:
    r.publish('channel', json.dumps(chunk))
```

Monitor message size:

```bash
redis-cli MEMORY USAGE channel
```

## Examples

```bash
# Check memory usage of channel
redis-cli MEMORY USAGE channel

# Publish small message
redis-cli PUBLISH channel "small message"

# Monitor pubsub memory
redis-cli INFO memory | grep used_memory_human
```
