---
title: "[Solution] TimescaleDB Access Node SSL Error"
description: "How to fix TimescaleDB access node SSL errors"
tools: ["timescaledb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- SSL not enabled between access and data nodes
- Certificate not trusted
- SSL mode mismatch

## How to Fix

```ini
ssl = on
ssl_cert_file = /path/to/server.crt
ssl_key_file = /path/to/server.key
```

## Examples

```bash
psql -h data-node-host -p 5432 -U postgres "sslmode=require"
```
