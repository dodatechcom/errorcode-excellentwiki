---
title: "[Solution] ScyllaDB Rebuild Failed Error"
description: "How to fix ScyllaDB node rebuild failures"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Source nodes unreachable
- Insufficient disk space
- Network timeout during streaming
- Too many concurrent rebuilds

## How to Fix

Check rebuild status:

```bash
nodetool netstats
nodetool status
```

## Examples

```bash
nodetool rebuild --inDC dc1 --sourceCdc2 datacenter1
nodetool netstats
```
