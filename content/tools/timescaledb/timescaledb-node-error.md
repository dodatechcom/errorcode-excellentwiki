---
title: "TimescaleDB Node Error"
description: "Access or data node error"
tools:
  - timescaledb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
TimescaleDB access or data node operation failure.

## Common Causes
- Node process crash
- Disk failure
- Memory exhaustion

## How to Fix
```bash
# Check PostgreSQL status
systemctl status postgresql

# Check TimescaleDB extension
SELECT * FROM pg_extension WHERE extname = 'timescaledb';
```

## Examples
```bash
# Restart PostgreSQL
systemctl restart postgresql
# Check node logs
tail -100 /var/log/postgresql/timescaledb.log
```

