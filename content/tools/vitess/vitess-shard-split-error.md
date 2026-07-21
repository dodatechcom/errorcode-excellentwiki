---
title: "[Solution] Vitess Shard Split Error"
description: "How to fix Vitess shard split errors"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Shard split failing
- Target shard not created
- Source shard not split

## How to Fix

```bash
vtctlclient SplitShard myks 0 myks 0-80
```

## Examples

```bash
vtctlclient ListShards myks
```
