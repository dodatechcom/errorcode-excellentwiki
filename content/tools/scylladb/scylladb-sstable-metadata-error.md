---
title: "[Solution] ScyllaDB SSTable Metadata Error"
description: "How to fix ScyllaDB SSTable metadata errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Metadata file corrupted
- SSTable format version mismatch
- Incomplete SSTable write

## How to Fix

```bash
sstablemetadata /var/lib/scylla/data/myks/mytable/mc-1-big-Data.db
```

## Examples

```bash
ls /var/lib/scylla/data/myks/mytable/
```
