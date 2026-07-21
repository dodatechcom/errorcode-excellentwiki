---
title: "[Solution] ScyllaDB Per Partition Rate Limit Error"
description: "How to fix ScyllaDB per partition rate limit errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Hot partition exceeding rate limit
- Write burst too large
- Rate limit configuration too restrictive

## How to Fix

```yaml
per_partition_rate_limit_bytes: 0
```

## Examples

```bash
nodetool tablestats myks.mytable | grep -i rate
```
