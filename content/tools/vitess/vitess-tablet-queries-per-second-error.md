---
title: "[Solution] Vitess Tablet QPS Error"
description: "How to fix Vitess tablet QPS errors"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- QPS too high for tablet
- QPS limit exceeded
- QPS monitoring not configured

## How to Fix

```bash
vtctlclient QueryServiceStats tablet-alias | grep -i qps
```

## Examples

```bash
curl http://tablet-host:15100/debug/status | grep -i qps
```
