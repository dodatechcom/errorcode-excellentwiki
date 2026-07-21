---
title: "[Solution] YugabyteDB Tablet Network Error"
description: "How to fix YugabyteDB tablet network errors"
tools: ["yugabyte"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Network latency too high
- Network packet loss
- Network interface saturated

## How to Fix

```bash
ping tikv-host
```

## Examples

```bash
iperf3 -c tikv-host
```
