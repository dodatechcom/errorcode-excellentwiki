---
title: "[Solution] PostgreSQL Locale error"
description: "Fix PostgreSQL 'locale' error. Resolve locale configuration issues during database creation."
tools: ["postgresql"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# PostgreSQL Locale error

ERROR: invalid locale name: '<locale>'

This error occurs when the specified locale is not available on the system.

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
