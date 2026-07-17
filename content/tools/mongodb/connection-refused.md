---
title: "MongoNetworkError: connect ECONNREFUSED"
description: "MongoDB client cannot establish a connection to the database server"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

This error occurs when the MongoDB client fails to connect to the database server, typically because the server is not running, the hostname or port is wrong, or a firewall is blocking the connection.

## Common Causes

- MongoDB server is not running or crashed
- Incorrect hostname or port in connection string
- Firewall blocking port 27017
- MongoDB bound to `127.0.0.1` only (not accessible remotely)

## How to Fix

1. Check if MongoDB is running:

```bash
systemctl status mongod
```

2. Start the service if it's stopped:

```bash
sudo systemctl start mongod
```

3. Verify MongoDB is listening on the expected port:

```bash
ss -tlnp | grep 27017
```

4. Ensure `mongod.conf` allows connections from your host:

```yaml
net:
  port: 27017
  bindIp: 0.0.0.0
```

## Examples

```javascript
// Node.js connection attempt
const { MongoClient } = require('mongodb');
const client = new MongoClient('mongodb://localhost:27017');
await client.connect();
// MongoNetworkError: connect ECONNREFUSED 127.0.0.1:27017
```

```bash
# Testing connection from command line
mongosh "mongodb://localhost:27017"
# MongoNetworkError: connect ECONNREFUSED 127.0.0.1:27017
```

## Related Errors

- [Duplicate Key Error](/tools/mongodb/duplicate-key)
