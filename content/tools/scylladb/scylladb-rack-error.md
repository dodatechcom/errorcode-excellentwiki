---
title: "[Solution] ScyllaDB Rack Error"
description: "How to fix ScyllaDB rack configuration errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- All nodes in same rack (no fault tolerance)
- Rack name mismatch
- Gossip info inconsistent

## How to Fix

```properties
dc=dc1
rack=rack1
```

## Examples

```bash
nodetool describecluster | grep -i rack
```
