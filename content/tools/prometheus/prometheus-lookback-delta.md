---
title: "[Solution] Prometheus Lookback Delta Error"
description: "How to fix Prometheus lookback delta configuration issues"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Lookback delta too short causing missing data points
- Lookback delta too long causing stale data inclusion
- Query returning unexpected results due to lookback window
- Metric with long gaps between samples

## How to Fix

Configure lookback delta:

```bash
prometheus --query.lookback-delta=5m
```

Check current setting:

```bash
curl -s http://localhost:9090/api/v1/status/runtimeinfo | jq '.data.lookbackDelta'
```

Adjust based on scrape interval:

```bash
# Lookback should be at least 4x scrape interval
# For 15s scrape interval: 5m lookback (default)
# For 60s scrape interval: 5m lookback (still fine)
```

## Examples

```bash
# Check lookback delta
curl -s http://localhost:9090/api/v1/status/runtimeinfo | jq '.data.lookbackDelta'

# Test query with different lookback
curl -s 'http://localhost:9090/api/v1/query?query=up&time=now'
```
