---
title: "[Solution] MongoDB mongos Connection Error"
description: "Fix MongoDB mongos router connection errors"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB mongos Connection Error

```
MongoServerError: could not find mongos in config servers
```

```
MongoServerError: mongos instance not found
```

## Common Causes

- The mongos process is not running
- The config servers are unreachable from mongos
- The mongos was started with incorrect config server addresses
- Network issues between mongos and config servers
- The mongos process crashed

## How to Fix

### 1. Start or restart mongos

```bash
mongos --configdb configRS/config1:27017,config2:27017,config3:27017 --bind_ip 0.0.0.0 --port 27017
```

### 2. Check mongos logs

```bash
tail -100 /var/log/mongodb/mongos.log
```

### 3. Verify config server connectivity from mongos

```bash
mongosh --host config1:27017 --eval "db.adminCommand({ping:1})"
```

### 4. Check mongos status

```javascript
sh.status()
```

## Examples

```bash
# Start mongos as a service
sudo systemctl start mongos

# Check if mongos is running
ps aux | grep mongos

# Verify connection to config servers
mongosh --host mongos --eval "sh.status()"
```