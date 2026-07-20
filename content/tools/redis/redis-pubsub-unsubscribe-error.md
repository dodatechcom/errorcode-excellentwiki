---
title: "[Solution] Redis Pub/Sub Unsubscribe Error"
description: "How to fix Redis Pub/Sub unsubscribe errors"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Trying to unsubscribe from channel not subscribed to
- Connection closed before unsubscribe
- Protocol error in unsubscribe command

## Fix

Check subscriptions:

```bash
redis-cli SUBSCRIBE  # enters subscribe mode, shows active channels
```

Unsubscribe cleanly:

```bash
redis-cli UNSUBSCRIBE channel1 channel2
```

Use PUNSUBSCRIBE for pattern:

```bash
redis-cli PUNSUBSCRIBE "pattern*"
```

## Examples

```bash
# Subscribe to channels
redis-cli SUBSCRIBE ch1 ch2 ch3

# Unsubscribe from specific channels
redis-cli UNSUBSCRIBE ch1

# Unsubscribe from all
redis-cli UNSUBSCRIBE
```
