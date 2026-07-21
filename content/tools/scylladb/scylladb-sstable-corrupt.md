---
title: "[Solution] ScyllaDB SSTable Corruption Error"
description: "How to fix ScyllaDB SSTable corruption errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Disk I/O error during write
- Power failure during flush
- Filesystem corruption
- Bad disk sector

## How to Fix

Verify SSTable integrity:

```bash
sstablemetadata /var/lib/scylla/data/my_keyspace/my_table-*
```

## Examples

```bash
nodetool verify my_keyspace my_table
ls -la /var/lib/scylla/data/my_keyspace/my_table-*/
```
