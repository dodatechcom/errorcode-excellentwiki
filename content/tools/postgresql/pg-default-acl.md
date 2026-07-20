---
title: "[Solution] PostgreSQL Default privileges error"
description: "Fix PostgreSQL 'default privileges' error. Resolve ALTER DEFAULT PRIVILEGES issues."
tools: ["postgresql"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# PostgreSQL Default privileges error

ERROR: cannot use IN SCHEMA clause when using FOR ROLE

This error occurs when the FOR ROLE and IN SCHEMA combination is invalid.

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
