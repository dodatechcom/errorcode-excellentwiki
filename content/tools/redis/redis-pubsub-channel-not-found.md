---
title: "[Solution] Redis Pub/Sub Channel Not Found Error"
description: "How to fix Redis Pub/Sub channel not found when publishing to non-existent channel"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Channel name mismatch (case-sensitive)
- Subscribers disconnected before publish
- Channel was never subscribed to

## Fix

Check active channels:

```bash
redis-cli PUBSUB CHANNELS
```

Verify channel name:

```bash
redis-cli PUBSUB CHANNELS "pattern*"
```

Subscribe before publishing:

```bash
# Terminal 1 (subscriber)
redis-cli SUBSCRIBE mychannel

# Terminal 2 (publisher)
redis-cli PUBLISH mychannel "hello"
```

## Examples

```bash
# List active channels
redis-cli PUBSUB CHANNELS

# Check channel subscriber count
redis-cli PUBSUB NUMSUB mychannel

# Test publish
redis-cli PUBLISH mychannel "test message"
```
