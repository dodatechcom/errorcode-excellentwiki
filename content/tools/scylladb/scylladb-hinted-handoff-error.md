---
title: "[Solution] ScyllaDB Hinted Handoff Error"
description: "How to fix ScyllaDB hinted handoff errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Hint directory full
- Target node unreachable
- Hint window expired

## How to Fix

```yaml
max_hint_window_in_ms: 10800000
hinted_handoff_throttle_in_kb: 1024
```

## Examples

```bash
ls /var/lib/scylla/hints/
```
