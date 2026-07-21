---
title: "[Solution] Vitess Tablet Master Error"
description: "How to fix Vitess tablet master errors"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- No master tablet elected
- Multiple masters in shard
- Master tablet down

## How to Fix

```bash
vtctlclient EmergencyReparentShard myks 0
```

## Examples

```bash
vtctlclient ListTablets myks 0
```
