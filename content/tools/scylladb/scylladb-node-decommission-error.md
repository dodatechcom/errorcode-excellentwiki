---
title: "[Solution] ScyllaDB Node Decommission Error"
description: "How to fix ScyllaDB node decommission errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Not enough nodes remaining after decommission
- Decommission data streaming stuck
- Gossip not consistent across cluster

## How to Fix

```bash
nodetool decommission
```

## Examples

```bash
nodetool status
```
