---
title: "MongoDB Connection Error"
description: "MongoDB client cannot establish a connection to the database server."
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

# MongoDB Connection Error

A MongoDB connection error occurs when the client cannot connect to the MongoDB server. This is typically caused by the server not running, incorrect connection details, or network issues.

## Common Causes

- MongoDB server is not running or crashed
- Incorrect hostname or port in connection string
- Firewall blocking port 27017
- MongoDB bound to `127.0.0.1` only

## How to Fix

### Check if MongoDB is Running

```bash
systemctl status mongod
```

### Start the Service

```bash
sudo systemctl start mongod
```

### Verify Port

```bash
ss -tlnp | grep 27017
```

### Configure Bind Address

```yaml
# /etc/mongod.conf
net:
  port: 27017
  bindIp: 0.0.0.0
```

### Test Connection

```bash
mongosh "mongodb://localhost:27017"
```

### Check Firewall

```bash
sudo ufw allow 27017/tcp
```

## Examples

```javascript
// Node.js connection attempt
const { MongoClient } = require('mongodb');
const client = new MongoClient('mongodb://localhost:27017');
await client.connect();
// MongoNetworkError: connect ECONNREFUSED 127.0.0.1:27017
```

## Related Errors

- [Auth Error]({{< relref "/tools/mongodb/auth-error" >}}) — authentication failure
- [Timeout Error]({{< relref "/tools/mongodb/timeout-error" >}}) — operation timeout
