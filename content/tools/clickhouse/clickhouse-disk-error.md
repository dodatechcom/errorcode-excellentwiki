---
title: "[Solution] ClickHouse Disk Error — How to Fix"
description: "Fix ClickHouse disk errors including storage policy issues, disk full situations, volume configuration problems, and data movement failures"
tools: ["clickhouse"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ClickHouse Disk Error

Disk errors in ClickHouse occur when storage policies, disk configurations, or file system issues prevent the database from reading or writing data.

## Why It Happens

- The disk is full and new data parts cannot be written
- A disk in the storage policy is unavailable or corrupted
- The `storage_configuration` is misconfigured
- File system permissions are wrong on the ClickHouse data directory
- A disk moved to a different mount point after restart
- The disk has I/O errors reported by the OS

## Common Error Messages

```
Code: 225. DB::Exception: All attempts to insert into replicated table failed
```

```
Code: 243. DB::Exception: Cannot create directory
```

```
Code: 3. DB::Exception: File size exceeds configured limit
```

```
Code: 252. DB::Exception: Too many parts
```

## How to Fix It

### 1. Fix Disk Full Issues

```bash
# Check disk usage
df -h /var/lib/clickhouse

# Find largest tables
clickhouse-client --query "
SELECT database, table, formatReadableSize(sum(bytes_on_disk)) AS size
FROM system.parts WHERE active = 1
GROUP BY database, table ORDER BY sum(bytes_on_disk) DESC"

# Drop old data
ALTER TABLE mydb.events DELETE WHERE event_time < now() - INTERVAL 90 DAY;

# Or drop old partitions
ALTER TABLE mydb.events DROP PARTITION '202401';
```

### 2. Fix Storage Policy Configuration

```yaml
# In /etc/clickhouse-server/config.d/storage.xml
<storage_configuration>
  <disks>
    <disk_ssd>
      <path>/data1/clickhouse/</path>
    </disk_ssd>
    <disk_hdd>
      <path>/data2/clickhouse/</path>
    </disk_hdd>
  </disks>
  <policies>
    <tiered>
      <volumes>
        <hot>
          <disk>disk_ssd</disk>
          <max_data_part_size_bytes>1073741824</max_data_part_size_bytes>
        </hot>
        <cold>
          <disk>disk_hdd</disk>
        </cold>
      </volumes>
      <move_factor>0.1</move_factor>
    </tiered>
  </policies>
</storage_configuration>
```

### 3. Fix File Permissions

```bash
sudo chown -R clickhouse:clickhouse /var/lib/clickhouse
sudo chmod 755 /var/lib/clickhouse
```

### 4. Check Disk Health

```bash
# Check for I/O errors
dmesg | grep -i error

# Check SMART status
sudo smartctl -a /dev/sda

# Check filesystem
sudo fsck -n /dev/sda1
```

## Common Scenarios

- **Disk full after large insert**: Drop old partitions or add a new disk to the storage policy.
- **Storage policy misconfigured**: Verify disk paths and restart ClickHouse.
- **Disk failure causes readonly replica**: Replace the disk and resync from other replicas.

## Prevent It

- Monitor disk usage and alert at 70% capacity
- Use tiered storage policies to automatically move old data to cheaper disks
- Configure `max_data_part_size_bytes` to control part placement across disks

## Related Pages

- [ClickHouse Table Error](/tools/clickhouse/clickhouse-table-error)
- [ClickHouse Backup Error](/tools/clickhouse/clickhouse-backup-error)
- [ClickHouse Merge Error](/tools/clickhouse/clickhouse-merge-error)
