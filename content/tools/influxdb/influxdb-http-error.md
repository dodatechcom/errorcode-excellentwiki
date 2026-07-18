---
title: "[Solution] InfluxDB HTTP API Error — How to Fix"
description: "Fix InfluxDB HTTP API errors including request failures, timeout issues, and HTTP interface configuration problems"
tools: ["influxdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# InfluxDB HTTP API Error

HTTP API errors in InfluxDB occur when clients cannot communicate via the HTTP interface. This includes request failures, timeouts, and configuration issues.

## Why It Happens

- The HTTP API is disabled in the configuration
- The request body exceeds the maximum allowed size
- The HTTP timeout is too short for the operation
- CORS headers are not configured for browser access
- The HTTP handler is overwhelmed by concurrent requests

## Common Error Messages

```
{"error":"http: server closed connection before response was ready"}
```

```
write failed: timeout after 10s
```

```
{"error":"unauthorized access"}
```

```
HTTP 413: Request Entity Too Large
```

## How to Fix It

### 1. Enable HTTP API

```bash
# In influxdb.conf
[http]
  enabled = true
  bind-address = ":8086"
```

### 2. Fix HTTP Timeout

```bash
# In influxdb.conf
[http]
  write-timeout = "10s"
  read-timeout = "10s"
```

### 3. Fix Max Body Size

```bash
[http]
  max-body-size = "100m"
```

### 4. Fix CORS Configuration

```bash
[http]
  auth-enabled = false
  cors-allowed-origins = ["*"]
  cors-allow-methods = ["GET", "POST"]
```

## Common Scenarios

- **Browser requests fail with CORS error**: Configure `cors-allowed-origins` in influxdb.conf.
- **Write timeout during bulk insert**: Increase `write-timeout`.
- **HTTP request too large**: Increase `max-body-size` or batch writes.

## Prevent It

- Configure appropriate timeouts for your workload
- Set up health checks on the HTTP API
- Monitor HTTP request metrics and error rates

## Related Pages

- [InfluxDB Connection Error](/tools/influxdb/influxdb-connection-error)
- [InfluxDB Auth Error](/tools/influxdb/influxdb-auth-error)
- [InfluxDB Token Error](/tools/influxdb/influxdb-token-error)
