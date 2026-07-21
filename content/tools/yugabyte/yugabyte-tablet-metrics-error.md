---
title: "[Solution] YugabyteDB Tablet Metrics Error"
description: "How to fix YugabyteDB tablet metrics errors"
tools: ["yugabyte"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Metrics endpoint not accessible
- Metrics not showing data
- Metrics scrape failing

## How to Fix

```bash
curl http://tikv-host:20180/metrics
```

## Examples

```bash
curl http://yugabyte-host:9000/metrics | head -20
```
