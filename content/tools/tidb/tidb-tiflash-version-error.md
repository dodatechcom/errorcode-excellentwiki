---
title: "[Solution] TiDB TiFlash Version Error"
description: "How to fix TiDB TiFlash version mismatch errors"
tools: ["tidb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- TiFlash version too old
- TiFlash version mismatch with TiDB
- TiFlash upgrade failed

## How to Fix

```bash
tiflash-server --version
```

## Examples

```sql
SELECT tidb_version();
```
