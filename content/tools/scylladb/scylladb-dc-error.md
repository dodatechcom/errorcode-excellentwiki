---
title: "[Solution] ScyllaDB Data Center Error"
description: "How to fix ScyllaDB data center configuration errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Node placed in wrong DC
- DC not defined in topology
- Snitch configuration wrong

## How to Fix

```bash
nodetool status
```

## Examples

```bash
cat /etc/scylla/cassandra-rackdc.properties
```
