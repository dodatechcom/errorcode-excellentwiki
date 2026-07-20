---
title: "[Solution] MongoDB Replica Set Connection String Error"
description: "Fix replica set connection string issues in MongoDB"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Replica Set Connection String Error

When connecting to a replica set with an incorrect connection string, you may see:

```
MongoTopologyClosedError: Topology was destroyed
```

```
MongoServerSelectionError: No replica set primary found
```

## Common Causes

- The connection string does not include all replica set members
- The replica set name in the connection string is wrong
- Using a direct connection (`directConnection=true`) when you need replica set mode
- The replica set has not been initialized yet
- The members listed in the connection string are unreachable
- The client driver version is incompatible with the replica set configuration

## How to Fix

### 1. Use the correct connection string format

```
mongodb://user:password@mongo1:27017,mongo2:27017,mongo3:27017/?replicaSet=rs0
```

### 2. Include the replica set name

```javascript
const client = new MongoClient(
  'mongodb://mongo1:27017,mongo2:27017,mongo3:27017/?replicaSet=rs0&authSource=admin'
);
```

### 3. Use the seedlist (SRV) format

```
mongodb+srv://user:password@mongo.example.com/?replicaSet=rs0
```

### 4. Verify replica set status

```javascript
rs.status()
rs.conf()
rs.isMaster()
```

### 5. Ensure all members are running

```bash
# On each member
mongosh --port 27017 --eval "rs.status().members.forEach(m => print(m.name, m.stateStr))"
```

## Examples

```bash
# Connect to the replica set
mongosh "mongodb://mongo1:27017,mongo2:27017,mongo3:27017/?replicaSet=rs0"

# Check replica set status
mongosh --eval "rs.status()"

# Initialize replica set (if not yet initialized)
mongosh --eval "rs.initiate({_id:'rs0', members:[{_id:0, host:'mongo1:27017'},{_id:1, host:'mongo2:27017'},{_id:2, host:'mongo3:27017'}]})"

# Verify the replica set configuration
mongosh --eval "rs.conf()"
```