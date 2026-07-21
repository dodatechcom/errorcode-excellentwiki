---
title: "[Solution] ScyllaDB Compaction Failed Error"
description: "How to fix ScyllaDB compaction failure errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Disk space insufficient for compaction
- Too many SSTables pending compaction
- Compaction strategy mismatch
- Memory pressure during compaction

## How to Fix

Check compaction status:

```bash
nodetool compactionstats
```

Trigger manual compaction:

```bash
nodetool compact my_keyspace my_table
```

## Examples

```bash
nodetool compactionstats
nodetool compact my_keyspace
nodetool tablestats my_keyspace.my_table | grep -i sstables
```
