---
title: "[Solution] PostgreSQL Out of Memory - Fix Memory Allocation Errors"
description: "Fix PostgreSQL out of memory errors by tuning work_mem, shared_buffers, and max_connections to prevent memory exhaustion on your server"
tools: ["postgresql"]
error-types: ["database-error"]
severities: ["critical"]
weight: 5
---

# PostgreSQL Out of Memory

An out of memory (OOM) error occurs when PostgreSQL cannot allocate memory for an operation. This is usually triggered by the operating system killing the PostgreSQL process (OOM killer) or by PostgreSQL hitting internal memory limits.

## What This Error Means

PostgreSQL may report:

```
ERROR: could not allocate memory for buffer
FATAL: out of memory
DETAIL: Failed on request of size 1048576.
```

Or the Linux OOM killer may terminate the process:

```
Out of memory: Kill process 12345 (postgres) score 900
```

PostgreSQL does not have a single global memory limit like Oracle's SGA. Instead, memory is allocated per-operation through settings like `work_mem`, `shared_buffers`, and `maintenance_work_mem`. A single query with many hash joins can consume multiple times `work_mem`.

## Why It Happens

- `work_mem` is set too high and multiple concurrent queries each allocate large hash tables
- `shared_buffers` is set too large, leaving insufficient memory for the OS and connection-level allocations
- `max_connections` is too high, with each connection potentially using `work_mem` for sorting
- A large `COPY` or bulk operation loads more data into memory than expected
- `maintenance_work_mem` is too high during `VACUUM`, `CREATE INDEX`, or `ALTER TABLE`
- The server does not have enough physical RAM for the configured memory settings
- Shared memory (PostgreSQL uses System V shared memory by default) cannot be allocated

## How to Fix It

### 1. Check Current Memory Settings

```sql
SHOW shared_buffers;
SHOW work_mem;
SHOW maintenance_work_mem;
SHOW max_connections;
SHOW effective_cache_size;
```

### 2. Calculate Safe Memory Limits

```bash
# Total memory available
free -g

# Rule of thumb for shared_buffers: 25% of RAM (max 8GB for most workloads)
# Rule of thumb for work_mem: (RAM - shared_buffers) / max_connections / 4
```

### 3. Reduce work_mem

```sql
-- Default is 4MB. Reduce if you have many concurrent connections
ALTER SYSTEM SET work_mem = '16MB';
SELECT pg_reload_conf();
```

### 4. Set max_connections Appropriately

```sql
-- Check current connection count
SHOW max_connections;
SELECT count(*) FROM pg_stat_activity;

-- Reduce if connections exceed available memory
ALTER SYSTEM SET max_connections = 100;
```

### 5. Use Connection Pooling

```bash
# Use PgBouncer to reduce actual PostgreSQL connections
# In pgbouncer.ini
[pgbouncer]
pool_mode = transaction
max_client_conn = 1000
default_pool_size = 20
```

### 6. Limit Memory for Specific Operations

```sql
-- Reduce work_mem for complex queries
SET LOCAL work_mem = '4MB';
SELECT * FROM large_table JOIN another_table ON ...;
```

### 7. Configure Huge Pages for Large shared_buffers

```bash
# In /etc/sysctl.conf
vm.nr_hugepages = 4096

# Check if huge pages are in use
grep HugePages /proc/meminfo
```

## Common Mistakes

- Setting `shared_buffers` to more than 50% of RAM -- this starves the OS page cache and connection-level allocations
- Using the default `work_mem` without considering that each query can use it multiple times (once per sort/hash operation)
- Not using a connection pooler -- each PostgreSQL connection uses approximately 10MB of memory regardless of workload
- Ignoring the OOM killer logs in `/var/log/syslog` or `dmesg`
- Setting `work_mem` too high on a server with 200+ connections -- the worst case memory is `work_mem * max_connections * sort_operations`

## Related Pages

- [PostgreSQL Connection Limit](/tools/postgresql/pg-connection-limit)
- [PostgreSQL Disk Full](/tools/postgresql/pg-disk-full)
- [PostgreSQL Config Error](/tools/postgresql/pg-config-error)
- [MySQL OOM](/tools/mysql/mysql-oom)
