---
title: "[Solution] ScyllaDB Memtable Flush Error"
description: "How to fix ScyllaDB memtable flush errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Disk I/O bottleneck during flush
- Too many memtables pending flush
- Disk full preventing flush

## How to Fix

Check flush status:

```bash
nodetool tablestats my_keyspace.my_table | grep -i memtable
```

## Examples

```bash
nodetool tablestats my_keyspace.my_table | grep -E '(MemTable|Flush)'
df -h /var/lib/scylla/
```
