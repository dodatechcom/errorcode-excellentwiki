---
title: "[Solution] ScyllaDB CCM Error"
description: "How to fix ScyllaDB CCM (Cassandra Cluster Manager) errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- CCM not installed properly
- Java version incompatible
- Port conflicts between nodes

## How to Fix

```bash
ccm create mycluster -n 3 --scylla
```

## Examples

```bash
ccm list
ccm status
```
