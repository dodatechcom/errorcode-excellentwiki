---
title: "[Solution] ClickHouse HTTP Interface Error — How to Fix"
description: "Fix ClickHouse HTTP interface errors including request failures, timeout issues, and HTTP API configuration problems"
tools: ["clickhouse"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ClickHouse HTTP Interface Error

HTTP interface errors in ClickHouse occur when clients cannot communicate via the HTTP API (port 8123). This includes request failures, timeouts, and configuration issues.

## Why It Happens

- The HTTP port is not enabled in the configuration
- The request is too large for `max_http_buffer_size`
- The HTTP timeout is too short for long-running queries
- CORS headers are not configured for browser access
- The HTTP handler is overwhelmed by concurrent requests
- The response exceeds `max_http_field_size`

## Common Error Messages

```
Code: 210. DB::Exception: Connection refused (localhost:8123)
```

```
Code: 241. DB::Exception: Memory limit exceeded for HTTP handler
```

```
Code: 33. DB::Exception: Cannot read all data in HTTP request
```

```
Code: 192. DB::Exception: Unknown method in HTTP request
```

## How to Fix It

### 1. Enable HTTP Interface

```xml
<!-- In config.xml -->
<http_port>8123</http_port>
<https_port>8443</https_port>

<!-- Enable CORS for browser access -->
<access_control_allow_origin>*</access_control_allow_origin>
```

### 2. Fix HTTP Timeout Issues

```bash
# Increase timeout for long queries
curl --max-time 300 'http://localhost:8123/' --data "SELECT count() FROM large_table"

# Or set in the query
curl 'http://localhost:8123/?query=SELECT%20sleep(10)&max_execution_time=30'
```

### 3. Fix HTTP Buffer Size

```xml
<max_http_buffer_size>104857600</max_http_buffer_size>  <!-- 100MB -->
```

### 4. Fix Concurrent Request Issues

```xml
<!-- Increase max concurrent queries -->
<max_concurrent_queries>200</max_concurrent_queries>

<!-- Use connection pooling in the client -->
```

## Common Scenarios

- **Browser CORS error**: Configure `access_control_allow_origin` in config.xml.
- **Long query times out**: Increase `max_execution_time` or client timeout.
- **Large upload fails**: Increase `max_http_buffer_size`.

## Prevent It

- Use the native TCP protocol (port 9000) for high-throughput applications
- Configure appropriate timeouts for long-running queries
- Monitor HTTP request metrics in `system.metrics`

## Related Pages

- [ClickHouse Connection Error](/tools/clickhouse/clickhouse-connection-error)
- [ClickHouse TCP Error](/tools/clickhouse/clickhouse-tcp-error)
- [ClickHouse User Error](/tools/clickhouse/clickhouse-user-error)
