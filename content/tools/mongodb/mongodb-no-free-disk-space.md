---
title: "[Solution] MongoDB No Free Disk Space Error"
description: "Fix MongoDB out of disk space errors"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB No Free Disk Space Error

```
MongoServerError: Insufficient free disk space
```

```
WiredTiger error: No space left on device
```

## Common Causes

- The data directory is full
- The journal directory is full
- The log directory is full
- Large uncleaned temp files
- The oplog has grown too large

## How to Fix

### 1. Check disk usage

```bash
df -h /var/lib/mongodb
df -h /var/log/mongodb
```

### 2. Clean up old files

```bash
# Remove old logs
sudo find /var/log/mongodb -name "*.log.*" -mtime +30 -delete

# Compact the database
mongosh --eval "db.runCommand({compact: 'users'})"
```

### 3. Move data to a larger disk

```bash
# Stop MongoDB
sudo systemctl stop mongod

# Move data directory
sudo rsync -av /var/lib/mongodb /new/path/mongodb

# Update mongod.conf
# net:
#   dbPath: /new/path/mongodb

# Start MongoDB
sudo systemctl start mongod
```

### 4. Enable WiredTiger compression

```javascript
db.runCommand({
  collMod: "users",
  storageEngine: { wiredTiger: { configString: "block_compressor=snappy" } }
});
```

## Examples

```bash
# Check disk usage
df -h

# Check data directory size
du -sh /var/lib/mongodb

# Check for large files
find /var/lib/mongodb -size +1G -ls
```