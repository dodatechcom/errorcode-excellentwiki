---
title: "[Solution] PostgreSQL RAISE exception error"
description: "Fix PostgreSQL 'RAISE' exception error. Resolve PL/pgSQL exception handling issues."
tools: ["postgresql"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# PostgreSQL RAISE exception error

ERROR: <custom error message>

This error occurs when a RAISE statement with EXCEPTION level is executed.

## How to Fix

### Check PostgreSQL Status

```bash
sudo systemctl status postgresql
pg_isready
```

### Check PostgreSQL Logs

```bash
sudo tail -100 /var/log/postgresql/postgresql-*-main.log
```

### Verify pg_hba.conf

```bash
sudo cat /etc/postgresql/*/main/pg_hba.conf
```

## Related Errors

- [Connection Refused]({{< relref "/tools/postgresql/pg-connection-refused" >}}) — server unreachable
- [Database Does Not Exist]({{< relref "/tools/postgresql/pg-database-does-not-exist" >}}) — missing database
