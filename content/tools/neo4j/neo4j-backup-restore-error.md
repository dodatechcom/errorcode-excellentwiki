---
title: "[Solution] Neo4j Backup Restore Error"
description: "How to fix Neo4j backup and restore errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Backup corrupted
- Version mismatch between backup and restore
- Disk space insufficient

## How to Fix

```bash
neo4j-admin database backup mydb --to-path=/backup/
neo4j-admin database restore mydb --from-path=/backup/mydb/
```

## Examples

```bash
ls -la /backup/
```
