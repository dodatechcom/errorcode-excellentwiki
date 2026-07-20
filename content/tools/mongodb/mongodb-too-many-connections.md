---
title: "[Solution] MongoDB Too Many Connections Error"
description: "Fix MongoDB connection limit exceeded errors"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Too Many Connections Error

```
MongoServerError: Connection pool was cleared
```

```
MongoServerError: too many connections
```

## Common Causes

- The connection pool size is too small for the workload
- Connections are not being released back to the pool
- Each request creates a new client instance
- The maxIncomingConnections setting is too low

## How to Fix

### 1. Increase max incoming connections

```yaml
# /etc/mongod.conf
net:
  maxIncomingConnections: 5000
```

### 2. Reuse the client instance

```javascript
// Wrong: creating a new client for each operation
async function getUser(id) {
  const client = new MongoClient(uri);
  await client.connect();
  const db = client.db("mydb");
  const result = await db.users.findOne({ _id: id });
  await client.close();
  return result;
}

// Right: reuse a single client
const client = new MongoClient(uri);
await client.connect();

async function getUser(id) {
  return client.db("mydb").users.findOne({ _id: id });
}
```

### 3. Configure connection pool size

```javascript
const client = new MongoClient(uri, {
  maxPoolSize: 100,
  minPoolSize: 10,
  maxIdleTimeMS: 30000
});
```

### 4. Monitor connection usage

```javascript
db.serverStatus().connections
```

## Examples

```bash
# Check current connections
mongosh --eval "db.serverStatus().connections"

# Check connection pool stats
mongosh --eval "db.serverStatus().network"

# Increase max connections
mongosh --eval "db.adminCommand({setParameter:1, maxIncomingConnections:5000})"
```