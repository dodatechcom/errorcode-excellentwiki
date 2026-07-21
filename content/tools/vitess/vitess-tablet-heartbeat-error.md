---
title: "[Solution] Vitess Tablet Heartbeat Error"
description: "How to fix Vitess tablet heartbeat errors"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Heartbeat not sent
- Heartbeat timeout
- Heartbeat lag too high

## How to Fix

```bash
vtctlclient ListTablets | grep -i heartbeat
```

## Examples

```bash
curl http://tablet-host:15100/debug/status | grep -i heartbeat
```
