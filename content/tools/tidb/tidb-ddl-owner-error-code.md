---
title: "TiDB DDL Owner Error Code"
description: "DDL owner error with specific code"
tools:
  - tidb
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
DDL owner returning specific error code.

## Common Causes
- DDL owner crashed
- etcd cluster unhealthy
- DDL job stuck

## How to Fix
```bash
# Check DDL owner
SELECT * FROM information_schema.tidb_ddl_owner;

# Restart TiDB
systemctl restart tidb
```

## Examples
```bash
# Check DDL jobs
SHOW DDL JOBS;
# Check DDL owner
SELECT * FROM information_schema.tidb_ddl_owner;
```

