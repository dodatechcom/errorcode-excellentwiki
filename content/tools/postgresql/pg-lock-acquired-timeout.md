---
title: "[Solution] PostgreSQL Lock Acquired Timeout"
description: "Fix PostgreSQL lock acquired timeout errors. Resolve long-running transactions holding exclusive locks."
tools: ["postgresql"]
error-types: ["tool-error"]
severities: ["error"]
---

# PostgreSQL Lock Acquired Timeout

ERROR: lock acquired timeout

This error occurs when a session cannot acquire a lock within the configured timeout because another session holds a conflicting lock.

## Common Causes

- Long-running transaction holding an exclusive lock on the target table
- Idle in transaction session blocking DDL operations
- Migration scripts attempting to acquire locks on busy tables

## How to Fix

1. Identify blocking queries using pg_locks:

```sql
SELECT blocked.pid AS blocked_pid,
       blocked.query AS blocked_query,
       blocking.pid AS blocking_pid,
       blocking.query AS blocking_query
FROM pg_catalog.pg_locks blocked
JOIN pg_catalog.pg_stat_activity blocking ON blocked.pid = blocking.pid
WHERE NOT blocked.granted;
```

2. Terminate the blocking session:

```sql
SELECT pg_terminate_backend(<blocking_pid>);
```

3. Increase lock timeout for migration scripts:

```sql
SET lock_timeout = '30s';
```

## Examples

```bash
# Monitor lock waits in real time
watch -n 1 "psql -c \"SELECT pid, state, wait_event_type, query FROM pg_stat_activity WHERE wait_event_type = 'Lock';\""
```
