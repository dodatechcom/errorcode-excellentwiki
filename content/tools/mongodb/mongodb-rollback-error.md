---
title: "[Solution] MongoDB Rollback Error"
description: "Fix MongoDB replica set rollback errors"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Rollback Error

```
MongoServerError: rollback is needed
```

## Common Causes

- The primary was isolated and writes went to a different node
- The old primary rejoins and must roll back uncommitted changes
- Network partition caused split-brain
- The oplog on the new primary does not contain the old primary's writes

## How to Fix

### 1. Prevent unnecessary rollbacks

- Use `w: "majority"` write concern for critical writes
- This ensures writes are on a majority of members before acknowledging

### 2. Check rollback data

```bash
# Look for rollback files
ls -la /var/lib/mongodb/*.bson

# Rollback files are saved in the data directory
mongodump --db local --collection rollback
```

### 3. Apply rollback data manually

```bash
sudo systemctl stop mongod
mongorestore --db local --collection <collection> /var/lib/mongodb/rollback/<file>.bson
sudo systemctl start mongod
```

### 4. Monitor for rollback events

```javascript
db.serverStatus().repl
```

```bash
grep -i "rollback" /var/log/mongodb/mongod.log
```

## Examples

```bash
# Check for rollback files
find /var/log/mongodb/ -name "*.bson" -o -name "rollback" 2>/dev/null

# Monitor rollback status
mongosh --eval '
  let status = db.serverStatus().repl;
  print("Replication state:", status.ismaster);
  print("Sync source:", status.syncSourceHost);
'

# Check oplog freshness
mongosh --eval "rs.printReplicationInfo()"
```