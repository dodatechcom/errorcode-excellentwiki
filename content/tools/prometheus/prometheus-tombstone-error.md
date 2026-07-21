---
title: "[Solution] Prometheus Tombstone Error"
description: "How to fix Prometheus tombstone errors during data deletion"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Tombstone file corrupted
- Tombstone count exceeds limit
- Delete operation creating invalid tombstones
- Tombstone file not properly flushed

## How to Fix

Check tombstone file:

```bash
ls -la prometheus-data/tombstones
```

Validate tombstones:

```bash
promtool tsdb check-tombstones prometheus-data/
```

If corrupted, remove and rebuild:

```bash
sudo systemctl stop prometheus
mv prometheus-data/tombstones prometheus-data/tombstones.bak
sudo systemctl start prometheus
```

## Examples

```bash
# Check tombstone count
wc -l prometheus-data/tombstones

# Monitor deletion operations
curl -s 'http://localhost:9090/api/v1/query?query=prometheus_tsdb_head_series'

# Validate tombstones
promtool tsdb check-tombstones prometheus-data/
```
