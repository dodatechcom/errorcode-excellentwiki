---
title: "[Solution] TiDB HTTP API Error — How to Fix"
description: "Fix TiDB HTTP API errors by resolving connection failures, correcting request parameters, and handling component API timeouts"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB HTTP API Error

TiDB HTTP API errors occur when the status API, PD API, or TiKV API endpoints return errors or become unreachable. These APIs are used for monitoring, diagnostics, and cluster management.

## Why It Happens

- Status port is not enabled on the TiDB node
- API request uses an unsupported HTTP method
- Request body contains invalid JSON
- Component is not running or the port is blocked by a firewall
- API request times out due to high server load
- Authentication is required but not provided

## Common Error Messages

```
ERROR: connection refused to status API
```

```
{"error": "invalid request"}
```

```
ERROR: HTTP 500 Internal Server Error
```

```
ERROR: context deadline exceeded
```

## How to Fix It

### 1. Verify API Endpoint Accessibility

```bash
# Check TiDB status port
curl -s http://tidb1:10080/status | jq .

# Check PD API
curl -s http://pd1:2379/pd/api/v1/cluster | jq .

# Check TiKV status
curl -s http://tikv1:20180/status | jq .

# Test with verbose output for debugging
curl -v http://tidb1:10080/status
```

### 2. Fix Common API Request Issues

```bash
# Correct HTTP method for PD API
curl -X POST http://pd:2379/pd/api/v1/config -d '{"key": "value"}'

# Send JSON with correct content type
curl -X PUT http://pd:2379/pd/api/v1/config \
  -H "Content-Type: application/json" \
  -d '{"replication": {"max-replicas": 3}}'

# Query TiDB hot regions
curl -s http://pd:2379/pd/api/v1/hotspot | jq '.stores | length'
```

### 3. Handle Timeouts and Retries

```bash
# Increase timeout for long operations
curl --connect-timeout 10 --max-time 30 \
  http://tidb:10080/tables/db/table/schema

# Retry on transient failures
for i in {1..3}; do
  curl -s http://pd:2379/pd/api/v1/health && break
  sleep 2
done
```

### 4. Access Protected APIs

```bash
# TiDB status API with token
curl -H "Authorization: Bearer <token>" \
  http://tidb:10080/debug/pprof/heap

# PD API with authentication
curl -u root:password http://pd:2379/pd/api/v1/stores
```

## Common Scenarios

- **curl returns connection refused**: Check that the status port is open and the service is running.
- **API returns 500**: Check component logs for the underlying error.
- **Monitoring shows no data**: Verify that the status port is accessible from the monitoring server.

## Prevent It

- Ensure status ports are open in firewall rules
- Use connection pooling for frequent API calls
- Monitor API latency and set appropriate timeouts

## Related Pages

- [TiDB Metrics Error](/tools/tidb/tidb-metrics-error)
- [TiDB PD Error](/tools/tidb/tidb-pd-error)
- [TiDB Connection Error](/tools/tidb/tidb-connection-error)
