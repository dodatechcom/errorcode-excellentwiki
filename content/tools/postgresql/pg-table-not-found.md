---
title: "[Solution] PostgreSQL Table not found"
description: "Fix PostgreSQL 'relation does not exist' error. Resolve table reference failures."
tools: ["postgresql"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# PostgreSQL Table not found

ERROR: relation '<name>' does not exist

This error occurs when you reference a table that does not exist in the database.

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
