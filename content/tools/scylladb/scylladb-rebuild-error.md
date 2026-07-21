---
title: "[Solution] ScyllaDB Rebuild Error"
description: "How to fix ScyllaDB node rebuild errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Source node unreachable
- Keyspace replication factor too high
- Network bandwidth saturated

## How to Fix

```bash
nodetool rebuild myks
```

## Examples

```bash
nodetool rebuild myks -dc dc1
```
