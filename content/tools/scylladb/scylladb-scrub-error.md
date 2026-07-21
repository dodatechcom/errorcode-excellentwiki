---
title: "[Solution] ScyllaDB Scrub Error"
description: "How to fix ScyllaDB sstable scrub errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Data corruption in SSTables
- Scrub skipping too many rows
- Scrub failing on corrupt partition

## How to Fix

```bash
nodetool scrub myks mytable
```

## Examples

```bash
nodetool scrub myks mytable --skip-corrupted
```
