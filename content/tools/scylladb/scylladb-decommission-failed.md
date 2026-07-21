---
title: "[Solution] ScyllaDB Decommission Failed Error"
description: "How to fix ScyllaDB node decommission failures"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Node has too much data to stream
- Network timeout during streaming
- Other nodes unreachable
- Node is the last in rack

## How to Fix

Check streaming status:

```bash
nodetool netstats
nodetool status
```

## Examples

```bash
nodetool status
nodetool decommission  # Execute on node being removed
nodetool netstats
```
