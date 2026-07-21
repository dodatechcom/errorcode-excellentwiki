---
title: "[Solution] ScyllaDB Commitlog Archive Error"
description: "How to fix ScyllaDB commitlog archival errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Archive directory not writable
- Archive command failing
- Disk full in archive location

## How to Fix

```yaml
commitlog_archive_command: /usr/bin/cp %c /archive/%f
```

## Examples

```bash
ls -la /var/lib/scylla/commitlog/
```
