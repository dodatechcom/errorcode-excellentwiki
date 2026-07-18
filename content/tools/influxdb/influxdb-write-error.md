---
title: "[Solution] InfluxDB Write Error — How to Fix"
description: "Fix InfluxDB write errors including partial writes, field type conflicts, retention policy issues, and line protocol parsing failures"
tools: ["influxdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# InfluxDB Write Error

Write errors in InfluxDB occur when data cannot be written via the HTTP API, line protocol, or client libraries. Common causes include malformed line protocol, field type conflicts, and retention policy issues.

## Why It Happens

- The line protocol has syntax errors (missing fields, wrong separators)
- A field type conflicts with existing data (string vs integer)
- The retention policy does not exist or has expired data
- The write request exceeds the maximum batch size
- The database does not exist
- Disk space is full and writes cannot be persisted

## Common Error Messages

```
{"error":"partial write: field type conflict: input field \"value\" on measurement \"cpu\" is type float, already exists as type integer"}
```

```
{"error":"partial write: unable to parse 'cpu value=50': invalid field format at 1:17"}
```

```
{"error":"database not found: mydb"}
```

```
write failed: server returned HTTP status 503 Service Unavailable
```

## How to Fix It

### 1. Fix Line Protocol Syntax

```bash
# BAD: missing space between measurement and field
cpu,host=server01 value=50

# GOOD: proper line protocol format
# measurement,tag_set field_set timestamp
# cpu,host=server01 value=50.0 1234567890

# Write with curl
curl -XPOST 'http://localhost:8086/write?db=mydb' \
  -d 'cpu,host=server01 value=50.0'
```

### 2. Fix Field Type Conflicts

```influxql
-- Check existing field types
SHOW FIELD KEYS FROM cpu

-- If you need to change field type, drop and recreate the measurement
DROP MEASUREMENT cpu
-- Then write with correct field types
```

### 3. Fix Retention Policy Issues

```influxql
-- Check retention policies
SHOW RETENTION POLICIES ON mydb

-- Create a retention policy
CREATE RETENTION POLICY "one_week" ON "mydb" DURATION 7d REPLICATION 1 DEFAULT

-- Write with specific retention policy
curl -XPOST 'http://localhost:8086/write?db=mydb&rp=one_week' \
  -d 'cpu,host=server01 value=50.0'
```

### 4. Increase max-body-size

```bash
# In influxdb.conf
[http]
  max-body-size = "100m"
  max-connection-limit = 0
```

### 5. Fix Partial Writes

```bash
# Check write endpoint for errors
curl -XPOST 'http://localhost:8086/write?db=mydb' \
  -d 'cpu,host=server01 value=50.0' -w '%{http_code}'

# If 400, check the line protocol format
# If 503, server may be overloaded or disk full
```

## Common Scenarios

- **Field type conflict after schema change**: Drop the measurement and rewrite with correct types.
- **Partial write on batch insert**: Some points have wrong format. Validate line protocol before writing.
- **Write fails with 503**: Server is overloaded or disk is full. Check disk space and server resources.

## Prevent It

- Validate line protocol before writing using client libraries
- Monitor write errors with `SHOW DIAGNOSTICS`
- Use consistent field types across all writes to the same measurement

## Related Pages

- [InfluxDB Line Protocol Error](/tools/influxdb/influxdb-line-protocol-error)
- [InfluxDB Retention Error](/tools/influxdb/influxdb-retention-error)
- [InfluxDB Write Error](/tools/influxdb/influxdb-write-error)
