---
title: "[Solution] ScyllaDB Schema Agreement Error"
description: "How to fix ScyllaDB schema agreement timeout errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Schema change not propagated to all nodes
- Node down preventing agreement
- Schema agreement timeout too short

## How to Fix

Force schema agreement:

```bash
nodetool describecluster
cqlsh -e "DESCRIBE KEYSPACE my_keyspace;"
```

## Examples

```bash
nodetool describecluster | grep -i schema
curl http://localhost:10000/schema_versions
```
