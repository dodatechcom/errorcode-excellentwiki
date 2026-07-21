---
title: "[Solution] YugabyteDB Tablet Debug Error"
description: "How to fix YugabyteDB tablet debug errors"
tools: ["yugabyte"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Debug endpoint not accessible
- Debug info not available
- Debug query failing

## How to Fix

```bash
curl http://tikv-host:20180/debug/pprof
```

## Examples

```bash
curl http://tikv-host:20180/debug/status
```
