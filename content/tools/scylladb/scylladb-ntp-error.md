---
title: "[Solution] ScyllaDB NTP Error"
description: "How to fix ScyllaDB NTP time synchronization errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- NTP not synchronized
- Clock skew between nodes
- Time source unreachable

## How to Fix

```bash
ntpq -p
```

## Examples

```bash
timedatectl status
```
