---
title: "[Solution] MongoDB Downstream Member Error"
description: "Fix MongoDB replica set downstream member communication errors"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Downstream Member Error

```
ReplSet info: member mongo2:27017 is now in state DOWN
```

```
MongoServerError: member is not reachable
```

## Common Causes

- The downstream member has crashed or been shut down
- Network connectivity is lost between members
- The member's data directory is corrupted
- Disk full on the downstream member
- Firewall rules changed

## How to Fix

### 1. Check the member's status

```bash
ssh mongo2 "sudo systemctl status mongod"
ssh mongo2 "df -h"
ssh mongo2 "free -h"
```

### 2. Restart the member

```bash
ssh mongo2 "sudo systemctl restart mongod"
```

### 3. Check for corruption

```bash
ssh mongo2 "mongosh --eval 'db.adminCommand({repairDatabase: 1})'"
```

### 4. Monitor heartbeat status

```javascript
rs.status().members.forEach(m => {
  print(m.name, m.stateStr, "lastHeartbeat:", m.lastHeartbeat);
});
```

## Examples

```bash
# Check member connectivity
mongosh --eval '
  rs.status().members.forEach(m => {
    print(m.name, m.stateStr, "health:", m.health,
          "lastHeartbeat:", m.lastHeartbeat);
  });
'
```