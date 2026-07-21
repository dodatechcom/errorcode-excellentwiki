---
title: "[Solution] Vitess Tablet Queries Error"
description: "How to fix Vitess tablet query serving errors"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Query serving not enabled
- Query service failed
- Query plan not available

## How to Fix

```bash
vtctlclient QueryServiceStats tablet-alias
```

## Examples

```bash
curl http://tablet-host:15100/debug/query_stats
```
