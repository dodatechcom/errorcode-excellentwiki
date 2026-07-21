---
title: "[Solution] ClickHouse Disk Error"
description: "Fix ClickHouse disk errors when storage volumes encounter IO failures"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse Disk Error

Disk errors occur when ClickHouse encounters IO failures on its data storage volumes.

## Common Causes

- Disk hardware failure
- Filesystem corruption
- IO scheduler overloaded
- Read-only filesystem mount

## How to Fix

Check disk health:

```bash
smartctl -a /dev/sda
```

Check ClickHouse disk config:

```xml
<storage_configuration>
    <disks>
        <disk1>
            <path>/var/lib/clickhouse/</path>
        </disk1>
    </disks>
</storage_configuration>
```

Check for IO errors:

```bash
dmesg | grep -i "io error\|disk"
```

## Examples

```sql
SELECT database, table, disk_name, formatReadableSize(sum(bytes_on_disk))
FROM system.parts GROUP BY database, table, disk_name ORDER BY sum(bytes_on_disk) DESC;
```
