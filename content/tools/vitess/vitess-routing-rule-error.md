---
title: "[Solution] Vitess Routing Rule Error"
description: "How to fix Vitess routing rule errors"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Routing rule not found
- Routing rule creating loop
- Routing rule not applied

## How to Fix

```bash
vtctlclient GetRoutingRules
```

## Examples

```bash
mysql -h vtgate-host -P 15306 -e "SHOW VSCHEMA RULES"
```
