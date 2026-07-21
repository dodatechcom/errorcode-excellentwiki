---
title: "[Solution] Rails Active Record Connection Error"
description: "ActiveRecord cannot connect."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

ActiveRecord cannot connect.

## Common Causes

Wrong database config.

## How to Fix

Check database.yml.

## Example

```yaml
development:
  adapter: postgresql
  database: myapp
```
