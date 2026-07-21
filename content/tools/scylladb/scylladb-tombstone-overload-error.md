---
title: "[Solution] ScyllaDB Tombstone Overload Error"
description: "How to fix ScyllaDB tombstone overload errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Large range scan hitting many tombstones
- Delete pattern creating excessive tombstones
- GC grace seconds too long

## How to Fix

```yaml
tombstone_failure_threshold: 100000
tombstone_warn_threshold: 1000
```

## Examples

```cql
TRACING ON; SELECT * FROM mytable WHERE status = 'deleted';
```
