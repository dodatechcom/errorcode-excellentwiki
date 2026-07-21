---
title: "[Solution] Vitess Shard Merge Error"
description: "How to fix Vitess shard merge errors"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Shard merge failing
- Source shards not found
- Data inconsistency during merge

## How to Fix

```bash
vtctlclient MergeShards myks 0-80 myks 0
```

## Examples

```bash
vtctlclient ListShards myks
```
