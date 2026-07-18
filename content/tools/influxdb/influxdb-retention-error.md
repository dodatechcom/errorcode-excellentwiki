---
title: "[Solution] InfluxDB Retention Policy Error — How to Fix"
description: "Fix InfluxDB retention policy errors including data expiry, policy creation, and database retention configuration issues"
tools: ["influxdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# InfluxDB Retention Policy Error

Retention policy errors occur when data expires unexpectedly, retention policies are misconfigured, or the default retention policy does not match requirements.

## Why It Happens

- The retention policy duration is set too short
- The DEFAULT retention policy was accidentally changed
- Data was written to a non-existent retention policy
- The shard duration is too large for the retention period
- Multiple retention policies overlap and cause confusion

## Common Error Messages

```
database not found: mydb
```

```
retention policy not found: one_week
```

```
partial write: retention policy mismatch
```

```
error: shard group duration must be less than or equal to the retention policy duration
```

## How to Fix It

### 1. Check Current Retention Policies

```influxql
SHOW RETENTION POLICIES ON mydb
```

### 2. Create or Modify Retention Policies

```influxql
-- Create a retention policy
CREATE RETENTION POLICY "one_year" ON "mydb"
  DURATION 52w REPLICATION 1 DEFAULT

-- Modify existing retention policy
ALTER RETENTION POLICY "one_year" ON "mydb"
  DURATION 104w SHARD DURATION 4w
```

### 3. Fix Default Retention Policy

```influxql
-- Check which is DEFAULT
SHOW RETENTION POLICIES ON mydb

-- Change DEFAULT
ALTER RETENTION POLICY "one_year" ON "mydb" DEFAULT
```

### 4. Fix Shard Duration

```influxql
-- Shard duration should be 1/2 to 1/6 of retention duration
-- For 1 year retention: 4w to 12w shard duration
ALTER RETENTION POLICY "one_year" ON "mydb" SHARD DURATION 4w
```

## Common Scenarios

- **Data disappears after 7 days**: Default retention policy was set to 7d. Change to a longer duration.
- **Cannot write to non-existent retention policy**: Create the retention policy first.
- **Shard duration too large**: Reduce shard duration to improve query performance.

## Prevent It

- Set explicit retention policies for each database during initial setup
- Monitor retention policy duration with `SHOW RETENTION POLICIES`
- Document retention requirements and verify policies match them

## Related Pages

- [InfluxDB Write Error](/tools/influxdb/influxdb-write-error)
- [InfluxDB Bucket Error](/tools/influxdb/influxdb-bucket-error)
- [InfluxDB Query Error](/tools/influxdb/influxdb-query-error)
