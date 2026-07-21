---
title: "YugabyteDB YSQL Client Error"
description: "YSQL client connection error"
tools:
  - yugabyte
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
YSQL client cannot connect to YugabyteDB.

## Common Causes
- YSQL port not reachable
- pg_hba.conf misconfigured
- SSL required but not configured

## How to Fix
```bash
# Check YSQL port
nc -zv localhost 5433

# Test connection
ysqlsh -h localhost -U yugabyte
```

## Examples
```bash
# Check YSQL listener
netstat -tlnp | grep 5433
# Test YSQL connection
ysqlsh -c "SELECT version();"
```

