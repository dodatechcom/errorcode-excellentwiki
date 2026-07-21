---
title: "[Solution] Vitess Tablet XA Error"
description: "How to fix Vitess tablet XA transaction errors"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- XA transaction not prepared
- XA transaction timeout
- XA transaction not committed

## How to Fix

```bash
mysql -h vtgate-host -P 15306 -e "XA START 'xid1'"
```

## Examples

```bash
mysql -h vtgate-host -P 15306 -e "XA PREPARE 'xid1'"
```
