---
title: "[Solution] Rails Schema Load Error"
description: "Schema load fails."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Schema load fails.

## Common Causes

Corrupted schema.

## How to Fix

Reset schema.

## Example

```bash
bin/rails db:drop db:create db:schema:load
```
