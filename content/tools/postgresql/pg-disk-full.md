---
title: "[Solution] PostgreSQL No Space Left on Device - Fix Disk Full Errors"
description: "Fix PostgreSQL could not extend file errors by freeing disk space, configuring tablespace limits, and monitoring WAL directory growth"
tools: ["postgresql"]
error-types: ["database-error"]
severities: ["critical"]
weight: 5
---

# PostgreSQL No Space Left on Device

This error occurs when PostgreSQL cannot write to disk because the filesystem has run out of space. PostgreSQL needs disk space for data files, WAL segments, temporary files, and log files. When any of these cannot be written, operations fail.

## What This Error Means

PostgreSQL reports:

```
ERROR: could not extend file "base/16384/12345": No space left on device
HINT: Check free disk space.
```

Or for WAL:

```
FATAL: could not open file "pg_wal/000000010000000000000016": No space left on device
```

PostgreSQL data files are stored in the `base` directory, one subdirectory per database. Each table and index is a separate file within that directory. When a file cannot be extended, the operation that triggered the extension fails.

## Why It Happens

- The data directory filesystem is full
- WAL segments are accumulating faster than they can be recycled
- A replication slot is preventing WAL cleanup (see Replication Slots page)
- Log files have grown large in `log_directory`
- Temporary files from large sorts or hash joins consume disk space
- The `pg_stat_tmp` or `pgsql_tmp` directories are full
- The tablespace volume is full

## How to Fix It

### 1. Identify What Is Using Disk Space

```bash
# Check filesystem usage
df -h /var/lib/postgresql/data/

# Find the largest files
find /var/lib/postgresql/data/ -type f -exec du -sh {} + | sort -rh | head -20

# Check WAL directory size
du -sh /var/lib/postgresql/data/pg_wal/
```

### 2. Remove Old WAL Segments

```bash
# If archiving is enabled, check archive directory
du -sh /var/lib/postgresql/archive/

# Remove archived WAL that is no longer needed
# WARNING: only do this if you have backups and no standbys need them
rm /var/lib/postgresql/archive/00000001000000000000000*
```

### 3. Clean Up Inactive Replication Slots

```sql
-- Find inactive slots that are holding WAL
SELECT slot_name, active, restart_lsn
FROM pg_replication_slots
WHERE active = false;

-- Drop stale slots
SELECT pg_drop_replication_slot('stale_slot');
```

### 4. VACUUM and Reclaim Space

```sql
-- VACUUM returns dead tuple space to the operating system
VACUUM FULL mytable;

-- For less disruptive space reclamation
VACUUM (VERBOSE) mytable;
```

### 5. Add Disk Space or Move Data

```bash
# Add a new tablespace on a different volume
mkdir -p /mnt/newdisk/pg_tablespace
sudo chown postgres:postgres /mnt/newdisk/pg_tablespace

# In PostgreSQL
CREATE TABLESPACE newdisk LOCATION '/mnt/newdisk/pg_tablespace';

-- Move tables to the new tablespace
ALTER TABLE large_table SET TABLESPACE newdisk;
```

### 6. Configure Log Rotation

```bash
# In postgresql.conf
log_destination = 'stderr'
logging_collector = on
log_directory = 'log'
log_filename = 'postgresql-%Y-%m-%d.log'
log_rotation_age = 1d
log_rotation_size = 100MB
```

## Common Mistakes

- Not monitoring disk space proactively -- by the time PostgreSQL reports the error, writes are already failing
- Ignoring the `pg_wal` directory growth during replication or archiving issues
- Running `VACUUM FULL` in production without considering the exclusive lock it requires
- Not setting up log rotation for PostgreSQL log files
- Allocating all disk space to the data partition without leaving room for WAL and logs

## Related Pages

- [PostgreSQL Replication Slots](/tools/postgresql/pg-replication-slots)
- [PostgreSQL WAL Segment Error](/tools/postgresql/pg-wal-segment-error)
- [PostgreSQL OOM](/tools/postgresql/pg-oom)
- [MySQL InnoDB Error](/tools/mysql/mysql-innodb-error)
