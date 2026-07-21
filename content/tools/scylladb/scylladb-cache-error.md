---
title: "[Solution] ScyllaDB Key Cache Error"
description: "How to fix ScyllaDB key cache errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Key cache size too small
- Key cache hit rate low
- Key cache eviction rate high

## How to Fix

```yaml
key_cache_size_in_mb: 0
```

## Examples

```bash
nodetool info | grep -i cache
```
