---
title: "[Solution] ScyllaDB Bootstrap Failed Error"
description: "How to fix ScyllaDB new node bootstrap failures"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Insufficient disk space on new node
- Network issues during streaming
- Schema agreement timeout
- Too many pending ranges

## How to Fix

Check bootstrap progress:

```bash
nodetool netstats | grep -i streaming
nodetool status
```

## Examples

```bash
nodetool status
df -h /var/lib/scylla/
nodetool netstats
```
