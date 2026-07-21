---
title: "TimescaleDB Scheduler Error"
description: "TimescaleDB scheduler failure"
tools:
  - timescaledb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
TimescaleDB scheduler is not running or is stuck.

## Common Causes
- Scheduler process crashed
- Database connection issue
- Scheduler configuration error

## How to Fix
```bash
# Check scheduler status
SELECT * FROM _timescaledb_internal.bgw_job_stat;

# Restart scheduler
SELECT alter_job(<job_id>, scheduled => true);
```

## Examples
```bash
# Check scheduler logs
tail -100 /var/log/postgresql/timescaledb-scheduler.log
# Monitor scheduler
curl -s http://localhost:8080/stats | jq '.scheduler'
```

