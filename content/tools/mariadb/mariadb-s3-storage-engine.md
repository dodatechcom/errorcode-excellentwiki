---
title: "[Solution] MariaDB S3 Storage Engine Error"
description: "Fix MariaDB S3 storage engine error. Resolve S3-backed table issues."
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
---

# MariaDB S3 Storage Engine Error

The S3 storage engine encounters errors. S3-backed tables are not accessible.

## Common Causes

- S3 plugin is not installed
- AWS credentials are wrong
- S3 bucket is not accessible

## How to Fix

### Solution 1

```bash
mysql -e "SHOW PLUGINS;"
```

## Related Pages

- [MariaDB Connection Error]({{< relref "/tools/mariadb/mariadb-connection-error" >}})
- [MariaDB InnoDB Error]({{< relref "/tools/mariadb/mariadb-innodb-error" >}})
- [MariaDB Galera Error]({{< relref "/tools/mariadb/mariadb-galera-error" >}})
