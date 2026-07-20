---
title: "[Solution] Redis Latency Tracking Configuration Error"
description: "How to fix Redis latency tracking and percentile calculation errors"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- latency-tracking disabled
- Percentile list too large consuming memory
- Invalid percentile values

## Fix

Check latency tracking config:

```bash
redis-cli CONFIG GET latency-tracking
redis-cli CONFIG GET latency-tracking-info-percentiles
```

Enable latency tracking:

```bash
redis-cli CONFIG SET latency-tracking yes
```

Set percentile list:

```bash
redis-cli CONFIG SET latency-tracking-info-percentiles "50 99 99.9"
```

View latency data:

```bash
redis-cli LATENCY LATEST
redis-cli LATENCY HISTORY command
```

## Examples

```bash
# Check latency
redis-cli LATENCY LATEST

# Set percentiles
redis-cli CONFIG SET latency-tracking-info-percentiles "50 95 99"

# Reset latency data
redis-cli LATENCY RESET
```
