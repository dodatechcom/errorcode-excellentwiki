---
title: "[Solution] PostgreSQL Exclusion constraint violation"
description: "Fix PostgreSQL 'exclusion constraint violation' error. Resolve exclusion constraint failures."
tools: ["postgresql"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# PostgreSQL Exclusion constraint violation

ERROR: conflicting key value violates exclusion constraint '<constraint>'

This error occurs when a new row conflicts with an existing row under an exclusion constraint.

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
