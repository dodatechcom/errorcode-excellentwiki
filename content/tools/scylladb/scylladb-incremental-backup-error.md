---
title: "[Solution] ScyllaDB Incremental Backup Error"
description: "How to fix ScyllaDB incremental backup errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Incremental backup not enabled
- Snapshot hardlinks broken
- Backup target not writable

## How to Fix

```yaml
incremental_backups: true
```

## Examples

```bash
nodetool snapshot myks -t mybackup
```
