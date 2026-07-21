---
title: "[Solution] TiDB TiFlash Restore Error"
description: "How to fix TiDB TiFlash restore errors"
tools: ["tidb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Restore failing on TiFlash
- TiFlash data not restored
- Restore timeout

## How to Fix

```bash
br restore full --pd pd-host:2379 --storage local:///backup
```

## Examples

```bash
br restore full --pd pd-host:2379 --storage s3://bucket/path
```
