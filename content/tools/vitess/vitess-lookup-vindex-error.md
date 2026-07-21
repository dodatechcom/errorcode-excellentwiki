---
title: "[Solution] Vitess Lookup Vindex Error"
description: "How to fix Vitess lookup vindex errors"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Lookup table not created
- Vindex column mismatch
- Lookup write failing

## How to Fix

```json
{
  "vindexes": {
    "email_vdx": {"type": "consistent_lookup_unique", "params": {"table": "email_lookup", "from": "email", "to": "user_id"}}
  }
}
```

## Examples

```bash
vtctlclient GetVSchema myks
```
