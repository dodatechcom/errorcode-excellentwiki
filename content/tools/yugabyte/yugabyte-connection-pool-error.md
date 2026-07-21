---
title: "YugabyteDB Connection Pool Error"
description: "Connection pool exhaustion"
tools:
  - yugabyte
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
YugabyteDB connection pool is exhausted.

## Common Causes
- Too many concurrent connections
- Connection leak
- Pool size too small

## How to Fix
```bash
# Check connection count
psql -c "SELECT count(*) FROM pg_stat_activity;"

# Kill idle connections
psql -c "SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE state = 'idle';"
```

## Examples
```sql
-- Check active connections
SELECT count(*), state FROM pg_stat_activity GROUP BY state;
-- Check connection limit
SHOW max_connections;
```

