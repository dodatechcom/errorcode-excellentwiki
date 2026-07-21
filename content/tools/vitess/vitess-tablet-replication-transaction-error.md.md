---
title: "Vitess Tablet Replication Transaction Error"
description: "Tablet replication transaction failure"
tools:
  - vitess
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Tablet replication transaction is failing.

## Common Causes
- Transaction conflict
- Lock timeout
- Deadlock detected

## How to Fix
```bash
# Check transaction status
mysql -e "SELECT * FROM information_schema.innodb_trx;"

# Kill stuck transaction
mysql -e "KILL <thread_id>;"
```

## Examples
```bash
# Check transaction logs
tail -100 /var/log/mysql/mysql.log | grep transaction
# Monitor transaction metrics
curl http://localhost:15100/debug/vars | jq '.TransactionCount'
```

