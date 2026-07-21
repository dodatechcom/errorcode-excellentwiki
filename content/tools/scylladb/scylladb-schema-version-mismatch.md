---
title: "[Solution] ScyllaDB Schema Version Mismatch"
description: "How to fix ScyllaDB schema version mismatch errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Schema agreement not reached
- Node joined with different schema
- Gossip protocol inconsistency

## How to Fix

```bash
nodetool describecluster
```

## Examples

```bash
nodetool status
```
