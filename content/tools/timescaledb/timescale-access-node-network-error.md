---
title: "[Solution] TimescaleDB Access Node Network Error"
description: "How to fix TimescaleDB access node network errors"
tools: ["timescaledb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Network between access and data nodes blocked
- Firewall blocking connection
- DNS resolution failing

## How to Fix

```bash
psql -h data-node-host -p 5432 -U postgres
```

## Examples

```bash
nc -zv data-node-host 5432
```
