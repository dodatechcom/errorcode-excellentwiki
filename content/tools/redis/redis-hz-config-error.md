---
title: "[Solution] Redis Hz Configuration Error"
description: "How to fix Redis hz (server frequency) configuration errors"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- hz value too low causing slow background tasks
- hz value too high causing CPU overhead
- Invalid hz value

## Fix

Check current hz:

```bash
redis-cli CONFIG GET hz
```

Set appropriate hz (default 10):

```bash
redis-cli CONFIG SET hz 10
```

For high-performance systems:

```bash
redis-cli CONFIG SET hz 50
```

Dynamic hz (Redis 7.0+):

```bash
redis-cli CONFIG SET dynamic-hz yes
```

## Examples

```bash
# Check hz
redis-cli CONFIG GET hz

# Set hz
redis-cli CONFIG SET hz 10

# Check if dynamic-hz is enabled
redis-cli CONFIG GET dynamic-hz
```
