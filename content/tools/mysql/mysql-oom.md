---
title: "[Solution] MySQL Out of Memory - Fix sort_buffer_size and Heap Errors"
description: "Fix MySQL out of memory errors by tuning sort_buffer_size, join_buffer_size, and reducing max_connections to prevent server exhaustion"
tools: ["mysql"]
error-types: ["database-error"]
severities: ["critical"]
weight: 5
---

# MySQL Out of Memory

An out of memory error in MySQL means the server or the operating system ran out of memory while processing a query or operation. This can be caused by per-session buffer settings that are too high, or by too many concurrent connections.

## What This Error Means

MySQL may report:

```
ERROR 3 (HY000): Error writing file '/tmp/MYxxxxx' (Errcode: 28 - No space left on device)
```

Or the Linux OOM killer may terminate the `mysqld` process:

```
Out of memory: Kill process 12345 (mysqld) score 800
```

MySQL allocates memory per-session for various buffers (`sort_buffer_size`, `join_buffer_size`, `read_buffer_size`, etc.). The worst-case memory usage is approximately:

```
max_connections * (sort_buffer_size + join_buffer_size + read_buffer_size + ...) + global_buffers
```

If this exceeds available RAM, the system will run out of memory.

## Why It Happens

- Per-session buffers are set too high for the number of concurrent connections
- `max_connections` is too high relative to available memory
- `tmp_table_size` or `max_heap_table_size` allows large in-memory temporary tables
- A query generates a large result set that is buffered in memory
- The InnoDB buffer pool is too large, leaving insufficient memory for other uses
- Memory fragmentation prevents effective allocation
- The OOM killer targets `mysqld` because it is the largest memory consumer

## How to Fix It

### 1. Check Current Memory Settings

```sql
SHOW VARIABLES LIKE 'sort_buffer_size';
SHOW VARIABLES LIKE 'join_buffer_size';
SHOW VARIABLES LIKE 'read_buffer_size';
SHOW VARIABLES LIKE 'max_connections';
SHOW VARIABLES LIKE 'tmp_table_size';
SHOW VARIABLES LIKE 'innodb_buffer_pool_size';
```

### 2. Calculate Worst-Case Memory Usage

```bash
# Formula for worst-case per-connection memory
# (sort_buffer + join_buffer + read_buffer + read_rnd_buffer + thread_stack)
# multiplied by max_connections, plus global buffers

# Example with 200 connections
echo "scale=2; 200 * (2 + 2 + 1 + 1 + 0.25) / 1024" | bc
# Result in GB
```

### 3. Reduce Per-Session Buffers

```sql
-- Reduce sort buffer (default 256KB)
SET GLOBAL sort_buffer_size = 256 * 1024;

-- Reduce join buffer (default 256KB)
SET GLOBAL join_buffer_size = 256 * 1024;

-- Reduce read buffer (default 128KB)
SET GLOBAL read_buffer_size = 128 * 1024;
```

### 4. Reduce max_connections

```sql
-- Check current usage
SHOW STATUS LIKE 'Threads_connected';

-- Reduce if too high
SET GLOBAL max_connections = 150;
```

### 5. Use a Connection Pooler

```bash
# ProxySQL or MySQL Router reduce the number of actual MySQL connections
# while allowing many application connections
```

### 6. Configure the InnoDB Buffer Pool Appropriately

```sql
-- Rule of thumb: 50-70% of available RAM on a dedicated MySQL server
-- But leave room for per-connection buffers and OS
SET GLOBAL innodb_buffer_pool_size = 4G;
```

### 7. Monitor with Performance Schema

```sql
-- Track memory usage by event
SELECT
    event_name,
    current_number_of_bytes_used,
    high_number_of_bytes_used
FROM performance_schema.memory_summary_global_by_event_name
ORDER BY high_number_of_bytes_used DESC
LIMIT 10;
```

## Common Mistakes

- Setting `sort_buffer_size` to 4MB or higher without considering that every connection gets this allocation
- Not monitoring `Threads_connected` -- if it spikes to 500, each connection uses its own buffers
- Setting `innodb_buffer_pool_size` to more than 80% of RAM, leaving nothing for connections and the OS
- Ignoring OOM killer logs in `/var/log/syslog` or `dmesg`
- Not accounting for replication threads when calculating memory usage

## Related Pages

- [MySQL Too Many Connections](/tools/mysql/mysql-too-many-connections)
- [MySQL InnoDB Error](/tools/mysql/mysql-innodb-error)
- [MySQL Crash Recovery](/tools/mysql/mysql-crash-recovery)
- [PostgreSQL OOM](/tools/postgresql/pg-oom)
