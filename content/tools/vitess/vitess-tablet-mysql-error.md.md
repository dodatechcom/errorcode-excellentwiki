---
title: "Vitess Tablet MySQL Error"
description: "Tablet MySQL connection failure"
tools:
  - vitess
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Tablet cannot connect to MySQL.

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

