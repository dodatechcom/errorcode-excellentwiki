---
title: "[Solution] Elasticsearch Node Error"
description: "Fix Elasticsearch node errors. Learn why this happens and how to resolve it quickly."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Elasticsearch Node Error

Elasticsearch node errors occur when nodes fail to join the cluster, run out of resources, or crash.

## Why This Happens

- Node not discovered
- Disk watermark exceeded
- OOM error
- Node leaving cluster

## Common Error Messages

- `node_not_found`
- `node_disk_watermark`
- `node_oom_error`
- `node_leaving`

## How to Fix It

### Solution 1: Check node status

View node information:

```bash
curl -X GET "localhost:9200/_cat/nodes?v"
```

### Solution 2: Fix disk watermarks

Increase disk watermarks or free up space:

```yaml
cluster.routing.allocation.disk.watermark.low: 85%
cluster.routing.allocation.disk.watermark.high: 90%
```

### Solution 3: Monitor heap usage

Check JVM heap usage:

```bash
curl -X GET "localhost:9200/_nodes/stats/jvm?pretty"
```


## Common Scenarios

- **Node not joining:** Check network connectivity and cluster name.
- **Disk watermark:** Free up disk space or increase watermarks.

## Prevent It

- Monitor node health
- Set disk watermarks
- Plan capacity
