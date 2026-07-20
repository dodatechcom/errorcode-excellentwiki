---
title: "[Solution] PostgreSQL no pg_hba.conf entry"
description: "Fix PostgreSQL 'no pg_hba.conf entry' error. Resolve host-based authentication configuration issues."
tools: ["postgresql"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# PostgreSQL no pg_hba.conf entry

FATAL: no pg_hba.conf entry for host, database, user

This error occurs when there is no matching rule in pg_hba.conf for the connection.

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
