---
title: "[Solution] PostgreSQL Requested WAL Segment Has Been Removed - Fix Recovery"
description: "Fix PostgreSQL requested WAL segment has been removed errors by configuring archive settings, replication slots, and wal_keep_size properly"
tools: ["postgresql"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

# PostgreSQL Requested WAL Segment Has Been Removed

This error occurs when a standby server or WAL archiver requests a WAL segment that the primary has already recycled. The primary no longer has the segment, so the standby cannot continue recovery or the archiver cannot archive it.

## What This Error Means

PostgreSQL recycles old WAL segments when they are no longer needed by any replication slot or wal_keep_size setting. If a consumer needs a segment that was already removed, you get:

```
FATAL: requested WAL segment 000000010000000000000015 has already been removed
```

This typically causes the standby to stop and require intervention. The primary continues operating normally, but the standby is now out of sync and may need to be rebuilt from a base backup.

## Why It Happens

- The standby was disconnected for longer than the WAL retention period
- `wal_keep_size` is set too low for the replication lag experienced
- No replication slot exists to protect the WAL segments needed by the standby
- The WAL archiver fell behind and the segments it needed were recycled
- A logical replication slot was inactive and its WAL was cleaned up
- Bulk operations on the primary generated WAL faster than expected

## How to Fix It

### 1. Check Current WAL Retention Settings

```sql
-- How much WAL to keep for standbys without replication slots
SHOW wal_keep_size;

-- Check if archive_command is configured
SHOW archive_mode;
SHOW archive_command;
```

### 2. Increase wal_keep_size

```sql
-- Keep more WAL segments for standbys (e.g., 2GB)
ALTER SYSTEM SET wal_keep_size = '2GB';
SELECT pg_reload_conf();
```

### 3. Create a Replication Slot for the Standby

```sql
-- On the primary, create a slot for the standby
SELECT pg_create_physical_replication_slot('standby_slot');

-- On the standby, use the slot
ALTER SYSTEM SET primary_slot_name = 'standby_slot';
SELECT pg_reload_conf();
```

### 4. Check Archive Command Status

```bash
# Verify archive is working
SELECT * FROM pg_stat_archiver;

# Check archive directory
ls -la /var/lib/postgresql/archive/ | head -20
```

### 5. Rebuild the Standby If WAL Is Lost

```bash
# If the standby cannot recover, rebuild from a base backup
pg_basebackup -h primary_host -D /var/lib/postgresql/data \
    -U replicator -P -R --slot=standby_slot
```

### 6. Configure pg_replication_slot_advance for Long Disconnections

```sql
-- If the standby was disconnected briefly, advance the slot
-- WARNING: this permanently discards WAL data
SELECT pg_replication_slot_advance('standby_slot', '0/15000000');
```

## Common Mistakes

- Setting `wal_keep_size` too low (the default of `0` means no WAL is kept for standbys)
- Not using replication slots for critical standbys that need to survive primary WAL recycling
- Forgetting that `pg_basebackup` generates WAL itself, which can accelerate recycling
- Not monitoring the WAL directory size on the primary after increasing `wal_keep_size`
- Assuming `archive_command` failures will block WAL recycling -- they do not

## Related Pages

- [PostgreSQL Replication Slots](/tools/postgresql/pg-replication-slots)
- [PostgreSQL Disk Full](/tools/postgresql/pg-disk-full)
- [PostgreSQL OOM](/tools/postgresql/pg-oom)
- [MySQL Crash Recovery](/tools/mysql/mysql-crash-recovery)
