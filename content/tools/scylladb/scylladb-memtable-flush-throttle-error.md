---
title: "[Solution] ScyllaDB Memtable Flush Throttling Error — How to Fix"
description: "Fix ScyllaDB memtable flush throttling errors when memtable writes are blocked waiting for flush to complete"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB Memtable Flush Throttling Error

Memtable flush throttling errors occur when ScyllaDB blocks or slows down writes because memtables are full and waiting for flush to disk.

## Why It Happens

- Write throughput exceeds flush throughput
- Disk I/O is too slow for flush operations
- Too many memtables are pending flush
- Flush concurrency is limited by I/O scheduler
- Large memtable size takes long to flush

## Common Error Messages

```
memtable: flush throttling: writes blocked for 5s
```

```
WARN: Memtable is full, flushing to disk
```

```
error: memtable flush failed, write path blocked
```

## How to Fix It

### 1. Increase Flush Concurrency

```yaml
# In scylla.yaml
memtable_flush_in_progress: true
```

### 2. Monitor Memtable Size

```bash
nodetool tablestats mykeyspace users | grep -i memtable
```

### 3. Tune Memtable Settings

```yaml
# In scylla.yaml
memtable_total_space_in_mb: 4096
commitlog_total_space_in_mb: 8192
```

### 4. Improve Disk I/O

```bash
# Move data to faster disk
sudo systemctl stop scylla-server
sudo rsync -av /var/lib/scylla/data/ /mnt/ssd/scylla/data/
sudo systemctl start scylla-server
```

## Examples

```
$ nodetool tablestats mykeyspace users | grep -i memtable
  Memtable cell count: 5000000
  Memtable data size: 2.5GB
  Memtable flush priority: high
```

## Prevent It

- Use SSD storage for the data directory
- Monitor memtable occupancy and flush rates
- Tune memtable_total_space_in_mb based on available RAM

## Related Pages

- [ScyllaDB Memtable Flush Error](/tools/scylladb/scylladb-memtable-flush-error)
- [ScyllaDB Memtable Full](/tools/scylladb/scylladb-memtable-full)
- [ScyllaDB Write Timeout](/tools/scylladb/scylladb-write-timeout)
