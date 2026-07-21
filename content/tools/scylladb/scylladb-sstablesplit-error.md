---
title: "[Solution] ScyllaDB SSTable Split Error"
description: "How to fix ScyllaDB sstable split errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- SSTable too large to compact
- Split producing too many files
- Disk space insufficient

## How to Fix

```bash
nodetool sstablesplit /var/lib/scylla/data/myks/mytable/
```

## Examples

```bash
ls -la /var/lib/scylla/data/myks/mytable/
```
