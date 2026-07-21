---
title: "[Solution] Rails Multiple Database Error"
description: "Multiple DB not working."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Multiple DB not working.

## Common Causes

Not configured.

## How to Fix

Configure databases.

## Example

```yaml
primary:
  database: myapp_primary
secondary:
  database: myapp_secondary
```
