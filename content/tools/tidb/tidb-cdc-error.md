---
title: "[Solution] TiDB CDC Error — How to Fix"
description: "Fix TiDB CDC errors by resolving TiCDC capture failures, fixing changefeed issues, and handling downstream sink problems"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB CDC Error

TiDB CDC (Change Data Capture) errors occur when TiCDC fails to capture and replicate data changes. TiCDC is used for real-time data replication.

## Why It Happens

- TiCDC capture process is down
- Changefeed is in error state
- Downstream sink is not accessible
- CDC encounters unsupported DDL
- CDC falls too far behind
- CDC memory is exhausted

## Common Error Messages

```
ERROR: TiCDC capture not running
```

```
ERROR: changefeed failed
```

```
ERROR: sink connection failed
```

```
ERROR: CDC memory exceeded
```

## How to Fix It

### 1. Check TiCDC Status

```bash
# Check TiCDC status
curl http://cdc1:8301/api/v1/changefeeds

# Check capture status
curl http://cdc1:8301/api/v1/captures

# Check TiCDC logs
tail -50 /var/log/ticdc/ticdc.log
```

### 2. Fix Changefeed

```sql
-- Create changefeed
CREATE CHANGEFEED FOR TABLE mydb.users INTO 'kafka://broker:9092?topic=users';

-- Check changefeed status
SHOW CHANGEFEED STATUS;

-- Pause/resume changefeed
PAUSE CHANGEFEED FOR <changefeed-id>;
RESUME CHANGEFEED FOR <changefeed-id>;
```

### 3. Fix Sink Issues

```bash
# Test sink connectivity
# For Kafka:
kafka-console-producer --broker-list broker:9092 --topic test

# For MySQL:
mysql -h mysql1 -P 3306 -u root

# Check TiCDC metrics
curl http://cdc1:8301/metrics
```

### 4. Monitor TiCDC

```bash
# Check changefeed lag
curl http://cdc1:8301/api/v1/changefeeds | jq '.[].status'

# Monitor replication progress
curl http://cdc1:8301/metrics | grep cdc
```

## Common Scenarios

- **Changefeed in error state**: Check downstream sink and restart changefeed.
- **CDC falls behind**: Add more TiCDC nodes or optimize downstream.
- **Unsupported DDL**: Update TiCDC or skip problematic DDL.

## Prevent It

- Monitor changefeed status regularly
- Set up alerts for changefeed lag
- Test CDC with production-like load

## Related Pages

- [TiDB Backup Error](/tools/tidb/tidb-backup-error)
- [TiDB TiKV Error](/tools/tidb/tidb-tikv-error)
- [TiDB Config Error](/tools/tidb/tidb-gflag-error)
