---
title: "[Solution] ScyllaDB Hints Not Enabled Error"
description: "How to fix ScyllaDB hint replay errors when hints are disabled"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Hinted handoff disabled
- hint_window_in_ms too short
- Too many hints stored
- Hint directory full

## How to Fix

Enable hints:

```yaml
hinted_handoff_enabled: true
hint_window_in_ms: 10800000
```

## Examples

```bash
grep hinted_handoff /etc/scylla/scylla.yaml
nodetool describecluster | grep -i hint
```
