---
title: "Vitess Tablet MySQL Replication Error"
description: "Tablet MySQL replication failure"
tools:
  - vitess
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Tablet MySQL replication is failing.

## Common Causes
- MySQL process down
- Connection refused
- Authentication failure

## How to Fix
```bash
# Check MySQL status
mysql -u root -p -e "SELECT 1;"

# Check MySQL logs
tail -100 /var/log/mysql/mysql.log
```

## Examples
```bash
# Test MySQL connection
mysql -h localhost -u vt_app -p
# Check MySQL process
ps aux | grep mysql
```

