---
title: "[Solution] ScyllaDB Prepared Statement Error"
description: "How to fix ScyllaDB prepared statement errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Wrong number of bind variables
- Prepared statement ID not found
- Bound value type mismatch

## How to Fix

Prepare correctly:

```python
prepared = session.prepare('SELECT * FROM my_table WHERE id = ?')
result = session.execute(prepared, [1])
```

## Examples

```bash
cqlsh -e "PREPARE SELECT * FROM my_table WHERE id = ?;"
```
