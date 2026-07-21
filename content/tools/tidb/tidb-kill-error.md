---
title: "[Solution] TiDB Kill Error — How to Fix"
description: "Fix TiDB kill errors by resolving KILL command failures, terminating stuck connections, and handling process cancellation issues"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB Kill Error

TiDB kill errors occur when attempting to terminate running queries or connections fails, or when the KILL command does not properly cancel the target operation.

## Why It Happens

- Process ID belongs to a different TiDB node
- Connection was already closed before KILL executed
- KILL command is blocked by permission restrictions
- Long-running transaction ignores the kill signal
- Connection is in a state that cannot be interrupted
- TiDB node is too overloaded to process the KILL

## Common Error Messages

```
ERROR: invalid connection id
```

```
ERROR: Query was killed
```

```
ERROR: kill process by id is not supported
```

```
ERROR: connection not found
```

## How to Fix It

### 1. Find and Kill the Correct Process

```sql
-- List all running queries
SHOW PROCESSLIST;

-- Get detailed process information
SELECT ID, USER, HOST, DB, COMMAND, TIME, STATE, INFO
FROM information_schema.PROCESSLIST
WHERE COMMAND != 'Sleep'
ORDER BY TIME DESC;

-- Kill a specific query
KILL <process_id>;
```

### 2. Handle Cross-Node Kill

```bash
# If the process is on a different TiDB node
# Connect to the specific node and run KILL there

# Find the TiDB node for the connection
mysql -h tidb_node_2 -P 4000 -u root -e "SHOW PROCESSLIST"

# Kill from the correct node
mysql -h tidb_node_2 -P 4000 -u root -e "KILL <id>"
```

### 3. Kill Stuck Transactions

```sql
-- Find long-running transactions
SELECT
  t.trx_id,
  t.trx_started,
  t.trx_query,
  t.trx_mysql_thread_id
FROM information_schema.INNODB_TRX t
WHERE TIMESTAMPDIFF(SECOND, t.trx_started, NOW()) > 60;

-- Kill the connection holding the transaction
KILL <trx_mysql_thread_id>;
```

### 4. Enable Force Kill

```sql
-- Enable kill for specific IDs
SET GLOBAL tidb_enable_slow_log = 1;

-- Check if KILL is allowed
SHOW VARIABLES LIKE 'tidb_force_kill%';

-- Use KILL TIDB to force kill on distributed cluster
KILL TIDB <process_id>;
```

## Common Scenarios

- **SHOW PROCESSLIST shows query but KILL fails**: The process may be on a different TiDB node; connect to that node directly.
- **Connection stuck after KILL**: The server-side resources have not been fully released; wait or restart the TiDB node.
- **KILL does not cancel a DDL job**: Use `CANCEL DDL JOBS` instead.

## Prevent It

- Set query timeouts to automatically cancel long-running operations
- Use `max_execution_time` for individual statements
- Monitor slow queries before they require manual kill

## Related Pages

- [TiDB Connection Error](/tools/tidb/tidb-connection-error)
- [TiDB Statement Error](/tools/tidb/tidb-statement-error)
- [TiDB Transaction Error](/tools/tidb/tidb-transaction-error)
