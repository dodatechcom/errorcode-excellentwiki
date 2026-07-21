---
title: "[Solution] Vitess Tablet Backup Error"
description: "How to fix Vitess tablet backup errors"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Backup storage not accessible
- Backup during write traffic
- Backup timeout

## How to Fix

```bash
vtctlclient Backup tablet-alias
```

## Examples

```bash
vtctlclient ListBackups myks 0
```
