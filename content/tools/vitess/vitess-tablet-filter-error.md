---
title: "[Solution] Vitess Tablet Filter Error"
description: "How to fix Vitess tablet filter errors"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Tablet filter not matching
- Filter syntax wrong
- No tablets matching filter

## How to Fix

```bash
vtctlclient ListTablets -keyspace myks -type replica
```

## Examples

```bash
vtctlclient ListTablets -cell dc1 -type replica
```
