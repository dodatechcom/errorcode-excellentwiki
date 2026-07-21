---
title: "[Solution] Grafana Dashboard Database Error"
description: "How to fix Grafana database errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Database connection pool exhausted
- Migration failed during upgrade
- SQLite file permissions wrong

## How to Fix

```ini
[database]
type = sqlite3
path = /var/lib/grafana/grafana.db
```

## Examples

```bash
ls -la /var/lib/grafana/grafana.db
```
