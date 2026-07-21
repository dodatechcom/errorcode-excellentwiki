---
title: "[Solution] Vitess Tablet Restore Error"
description: "How to fix Vitess tablet restore errors"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Backup not found
- Restore path wrong
- MySQL not stopped during restore

## How to Fix

```bash
vtctlclient RestoreFromBackup tablet-alias
```

## Examples

```bash
vtctlclient ListBackups myks 0
```
