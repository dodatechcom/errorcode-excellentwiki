---
title: "[Solution] InfluxDB Data Ingestion Rate Error — How to Fix"
description: "Fix InfluxDB data ingestion rate errors when the incoming write throughput exceeds the server processing capacity"
tools: ["influxdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# InfluxDB Data Ingestion Rate Error

Data ingestion rate errors occur when the volume of incoming writes exceeds InfluxDB's ability to process and persist them, leading to write rejections or data loss.

## Why It Happens

- Too many Telegraf agents reporting simultaneously
- Burst traffic patterns overwhelm the write pipeline
- Disk I/O cannot keep up with write throughput
- Compaction consumes resources needed for writes
- Network buffers fill up before data is processed

## Common Error Messages

```
partial write: write rate exceeded, retry after 30s
```

```
error: too many concurrent writes, server overloaded
```

```
WARN: ingestion queue is full, incoming writes will be dropped
```

## How to Fix It

### 1. Enable Write Backpressure

```bash
[http]
  write-timeout = "60s"
  max-concurrent-write-limit = 100
```

### 2. Use Client-Side Rate Limiting

```python
from influxdb_client.client.write_api import SYNCHRONOUS, WriteOptions

write_api = client.write_api(write_options=WriteOptions(
    batch_size=5000,
    flush_interval=10_000,
    retry_interval=5_000,
    max_retries=5
))
```

### 3. Scale Horizontally

```bash
# Add data nodes to distribute write load
influxd-ctl add-data node3:8088
```

### 4. Monitor Ingestion Rate

```bash
curl -s 'http://localhost:8086/debug/vars' | jq '.rx'
```

## Examples

```
WARN: ingestion dropped 2500 points due to rate limit
INFO: ingestion rate stabilized at 50000 points/sec
```

## Prevent It

- Rate-limit clients at the application level
- Use write batching to smooth out bursts
- Monitor write throughput and set alerts

## Related Pages

- [InfluxDB Write Error](/tools/influxdb/influxdb-write-error)
- [InfluxDB Write Buffer Full](/tools/influxdb/influxdb-write-buffer-full)
- [InfluxDB Bandwidth Error](/tools/influxdb/influxdb-bandwidth-error)
