---
title: "[Solution] InfluxDB Bandwidth Limit Exceeded Error — How to Fix"
description: "Fix InfluxDB bandwidth limit exceeded errors by optimizing write batching and connection pooling"
tools: ["influxdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# InfluxDB Bandwidth Limit Exceeded Error

Bandwidth limit errors occur when the rate of incoming write requests exceeds the configured network throughput capacity of the InfluxDB server.

## Why It Happens

- Write requests exceed the per-connection bandwidth cap
- Too many concurrent clients writing simultaneously
- Network interface saturation on the InfluxDB host
- Oversized batch payloads in a single write request
- Rate limiting is enabled with strict thresholds

## Common Error Messages

```
HTTP 429: Too Many Requests -- bandwidth limit exceeded
```

```
error: write rate limit exceeded, retry later
```

```
{"error":"request body too large for bandwidth limit"}
```

```
write failed: connection bandwidth limit reached
```

## How to Fix It

### 1. Adjust Rate Limits in Configuration

```bash
[http]
  max-body-size = 10485760
  write-timeout = "60s"
  max-concurrent-write-limit = 100
```

### 2. Optimize Client Write Batching

```python
from influxdb_client import InfluxDBClient, WriteOptions

client = InfluxDBClient(url="http://localhost:8086", token="mytoken")
write_api = client.write_api(write_options=WriteOptions(
    batch_size=5000,
    flush_interval=10_000,
    retry_interval=5_000
))
```

### 3. Enable Compression

```bash
curl -XPOST 'http://localhost:8086/api/v2/write?org=myorg&bucket=mydb' \
  -H 'Authorization: Token mytoken' \
  -H 'Content-Encoding: gzip' \
  --data-binary @compressed_data.gz
```

### 4. Increase Server Bandwidth Limits

```bash
ethtool eth0 | grep Speed
sudo ethtool -s eth0 speed 10000 duplex full
```

## Examples

```
$ curl -XPOST http://localhost:8086/api/v2/write -d @large_payload.lp
HTTP/1.1 429 Too Many Requests
Retry-After: 30
```

## Prevent It

- Use connection pooling in client applications
- Enable gzip compression for all write operations
- Monitor network utilization with InfluxDB metrics

## Related Pages

- [InfluxDB Write Error](/tools/influxdb/influxdb-write-error)
- [InfluxDB Connection Error](/tools/influxdb/influxdb-connection-error)
- [InfluxDB HTTP Error](/tools/influxdb/influxdb-http-error)
