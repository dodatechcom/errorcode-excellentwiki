---
title: "[Solution] PostgreSQL TOAST tuple overflow error"
description: "Fix PostgreSQL 'TOAST tuple overflow' error. Resolve issues with large column values exceeding row limits."
tools: ["postgresql"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# PostgreSQL TOAST tuple overflow error

ERROR: row is too big: size <n>, maximum size <m>

This error occurs when a single row exceeds the maximum row size limit.

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
