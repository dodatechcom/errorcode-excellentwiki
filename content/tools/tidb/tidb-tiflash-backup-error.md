---
title: "[Solution] TiDB TiFlash Backup Error"
description: "How to fix TiDB TiFlash backup errors"
tools: ["tidb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Backup failing on TiFlash
- TiFlash data not included in backup
- Backup timeout

## How to Fix

```bash
br backup full --pd pd-host:2379 --storage local:///backup
```

## Examples

```bash
br backup full --pd pd-host:2379 --storage s3://bucket/path
```
