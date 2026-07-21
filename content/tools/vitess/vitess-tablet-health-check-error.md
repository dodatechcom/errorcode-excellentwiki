---
title: "[Solution] Vitess Tablet Health Check Error"
description: "How to fix Vitess tablet health check errors"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Health check not responding
- Health check timeout
- Health check failed

## How to Fix

```bash
vtctlclient ListTablets | grep -i health
```

## Examples

```bash
curl http://tablet-host:15100/debug/status | grep -i health
```
