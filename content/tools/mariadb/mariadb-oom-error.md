---
title: "[Solution] MariaDB Out of Memory Error — How to Fix"
description: "Fix MariaDB OOM errors by tuning buffer pool size, sort buffers, connection limits, and OS-level memory settings to prevent crashes"
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# MariaDB Out of Memory Error

An OOM error occurs when MariaDB or the operating system runs out of available memory. MariaDB allocates memory per-connection for sort buffers, join buffers, and the shared InnoDB buffer pool.

## Why It Happens

- `innodb_buffer_pool_size` is too high, leaving insufficient memory for connections
- `max_connections` is too high and each connection allocates large buffers
- Large `join_buffer_size`, `sort_buffer_size`, or `read_buffer_size` per session
- A single query uses a huge temporary table that spills to memory
- The OOM killer targets mysqld as the largest memory consumer

## Common Error Messages

```
[ERROR] mysqld: Out of memory (Needed 268435456 bytes)
[ERROR] InnoDB: Unable to allocate 262144 bytes of memory
```

```
[ERROR] InnoDB: Memory allocation of 268435456 bytes failed
[ERROR] InnoDB: Check that the OS has enough free memory
```

```
fatal error: out of memory
Killed process 12345 (mysqld)
oom-kill: process 12345 (mysqld) ... total-vm:8388608kB
```

```
ERROR 1135 (HY000): Out of memory
Check that you have enough memory available for this query
```

## How to Fix It

### 1. Tune innodb_buffer_pool_size

```sql
SHOW VARIABLES LIKE 'innodb_buffer_pool_size';
SET GLOBAL innodb_buffer_pool_size = 8589934592; -- 8GB
```

```ini
[mysqld]
innodb_buffer_pool_size = 8G
innodb_buffer_pool_instances = 8
```

### 2. Reduce Per-Connection Buffer Sizes

```sql
SET GLOBAL sort_buffer_size = 131072;    -- 128K
SET GLOBAL join_buffer_size = 131072;    -- 128K
SET GLOBAL read_buffer_size = 65536;     -- 64K
SET GLOBAL read_rnd_buffer_size = 65536;
```

### 3. Limit max_connections

```sql
SHOW STATUS LIKE 'Threads_connected';
SET GLOBAL max_connections = 200;
```

### 4. Configure OS OOM Protection

```bash
echo -1000 > /proc/$(pgrep mysqld)/oom_score_adj

# Or via systemd
sudo systemctl edit mariadb
# [Service]
# OOMScoreAdjust=-1000
# MemoryLimit=12G
```

### 5. Monitor Memory Usage

```sql
SELECT * FROM sys.memory_global_total;
SELECT * FROM sys.memory_by_thread_by_current_bytes LIMIT 10;
SHOW ENGINE INNODB STATUS\G
```

## Common Scenarios

- **Sudden traffic spike**: Hundreds of connections each allocating 4MB buffers. Reduce limits.
- **Large JOIN on unindexed column**: Huge join_buffer_size allocated. Add index instead.
- **Multiple services on one VM**: MariaDB, Redis, and app compete for 4GB RAM. Scale up.

## Prevent It

- Set `innodb_buffer_pool_size` explicitly based on available RAM
- Monitor `Threads_connected` for memory pressure
- Benchmark after config changes to validate memory usage

## Related Pages

- [MariaDB InnoDB Error](/tools/mariadb/mariadb-innodb-error)
- [MariaDB Connection Error](/tools/mariadb/mariadb-connection-error)
- [MySQL OOM](/tools/mysql/mysql-oom)
