---
title: "[Solution] Redis Pub/Sub Pattern Mismatch Error"
description: "How to fix Redis Pub/Sub pattern mismatch when PSUBSCRIBE patterns don't match expected channels"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Pattern syntax incorrect
- Channel name format changed
- Wildcard placement wrong

## Fix

Test pattern match:

```bash
redis-cli PUBSUB CHANNELS "user:*"
```

Common patterns:

```bash
# Match all channels
redis-cli PSUBSCRIBE *

# Match channels starting with user:
redis-cli PSUBSCRIBE "user:*"

# Match channels ending with :events
redis-cli PSUBSCRIBE "*:events"
```

Check matching channels:

```bash
redis-cli PUBSUB CHANNELS "pattern"
```

## Examples

```bash
# Subscribe with pattern
redis-cli PSUBSCRIBE "notifications:*"

# Check matching channels
redis-cli PUBSUB CHANNELS "notifications:*"

# Publish to matching channel
redis-cli PUBLISH notifications:email "new message"
```
