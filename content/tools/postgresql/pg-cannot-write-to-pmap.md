---
title: "[Solution] PostgreSQL Cannot write to pg_stat error"
description: "Fix PostgreSQL 'cannot write to pg_stat' error. Resolve statistics file system issues."
tools: ["postgresql"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# PostgreSQL Cannot write to pg_stat error

ERROR: could not open statistics file: Permission denied

This error occurs when PostgreSQL cannot write to the statistics directory.

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
