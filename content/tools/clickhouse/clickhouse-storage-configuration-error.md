---
title: "[Solution] ClickHouse Storage Configuration Error"
description: "Fix ClickHouse storage configuration errors when multi-disk or volume setup fails"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse Storage Configuration Error

Storage configuration errors occur when ClickHouse cannot use configured storage volumes or disks.

## Common Causes

- Disk path does not exist or is not writable
- Storage policy references non-existent disk
- Volume order mismatch in storage policy
- Disk space check failing

## How to Fix

Check storage config:

```sql
SELECT * FROM system.storage_policies;
```

Check disk usage:

```sql
SELECT path, free_space, total_space FROM system.disks;
```

Fix storage configuration:

```xml
<storage_configuration>
    <disks>
        <disk1><path>/data1/clickhouse/</path></disk1>
        <disk2><path>/data2/clickhouse/</path></disk2>
    </disks>
    <policies>
        <my_policy>
            <volumes>
                <hot><disk>disk1</disk></hot>
                <cold><disk>disk2</disk></cold>
            </volumes>
        </my_policy>
    </policies>
</storage_configuration>
```

## Examples

```sql
SELECT name, policy, disk_name, free_space FROM system.disks;
```
