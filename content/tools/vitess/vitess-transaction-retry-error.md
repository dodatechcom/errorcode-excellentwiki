---
title: "[Solution] Vitess Transaction Retry Error"
description: "How to fix Vitess transaction retry errors"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Transient transaction error
- Deadlock detected
- Shard-level conflict

## How to Fix

```bash
mysql -h vtgate-host -P 15306 -u user -e "SELECT 1"
```

## Examples

```bash
vtctlclient ShardInfo myks 0
```
