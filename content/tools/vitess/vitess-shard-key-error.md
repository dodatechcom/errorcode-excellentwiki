---
title: "[Solution] Vitess Shard Key Error"
description: "How to fix Vitess shard key and routing errors"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Shard key not in VSchema
- Query missing shard key in WHERE
- Cross-shard query not supported

## How to Fix

```json
{
  "sharded": true,
  "vindexes": {
    "hash": {"type": "hash"}
  },
  "tables": {
    "users": {"column_vindexes": [{"column": "id", "name": "hash"}]}
  }
}
```

## Examples

```bash
vtctlclient VSchemaInfo myks
```
