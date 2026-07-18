---
title: "[Solution] Cassandra SSTable Error - Fix SSTable Corruption Detected"
description: "Fix Cassandra SSTable corruption errors. Recover from corrupted SSTables using repair, rebuild, and data recovery strategies."
tools: ["cassandra"]
error-types: ["sstable-error"]
severities: ["critical"]
weight: 5
---

This error means a Cassandra SSTable file is corrupted and cannot be read. SSTables are immutable on-disk storage files, and corruption can cause read failures and data loss.

## What This Error Means

When SSTable corruption is detected, you see:

```
CorruptSSTableException: Encountering corruptions in table
# or
CorruptSSTableException: Checksum mismatch
# or
IOException: Could not read SSTable
```

SSTables store data on disk in immutable format. Corruption can occur from hardware failures, disk errors, or software bugs.

## Why It Happens

- Disk failure or bad sectors on the storage device
- Power loss during an flush or compaction operation
- Filesystem corruption from a kernel bug
- Data corruption during network transfer in multi-datacenter setups
- Cassandra bug causing incorrect SSTable writes
- Hardware memory errors (bit flips) during write operations

## How to Fix It

### Identify the corrupted SSTable

```bash
nodetool verify keyspace_name.table_name
```

This checks all SSTables for corruption.

### Recover using scrub

```bash
nodetool scrub keyspace_name table_name
```

Scrub reads all SSTables and rebuilds them without corrupted data.

### Use sstableupgrade

```bash
sstableupgrade /path/to/cassandra/data/keyspace/table /path/to/recovery/
```

Extract readable data from corrupted SSTables.

### Repair after removing corrupted files

```bash
# Remove the corrupted SSTable (backup first)
cp /path/to/corrupted-*.db /backup/
rm /path/to/corrupted-*.db

# Repair to rebuild missing data
nodetool repair keyspace_name table_name
```

### Use sstableloader to reimport data

```bash
sstableloader -d node1:/path/to/cassandra/data/keyspace/table
```

Load SSTables back into the cluster.

### Check disk health

```bash
sudo smartctl -a /dev/sda
dmesg | grep -i error
```

Hardware issues are the most common cause of corruption.

### Enable data integrity checks

```yaml
# cassandra.yaml
integrity_check_enabled: true
```

Cassandra can verify data integrity on reads.

### Restore from backup

```bash
# If available, restore from a backup
nodetool snapshot keyspace_name table_name -t backup-tag
```

## Common Mistakes

- Not monitoring disk health proactively
- Running nodetool repair without first addressing the corrupted SSTable
- Assuming scrub will recover all data (corrupted rows are dropped)
- Not backing up SSTables before attempting repair
- Not investigating the root cause of corruption

## Related Pages

- [Cassandra Compaction Error]({{< relref "/tools/cassandra/cassandra-compaction-error" >}}) -- compaction issues
- [Cassandra Read Timeout]({{< relref "/tools/cassandra/cassandra-read-timeout" >}}) -- read failures
- [Cassandra Unavailable]({{< relref "/tools/cassandra/cassandra-unavailable" >}}) -- availability issues
