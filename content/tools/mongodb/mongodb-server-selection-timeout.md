---
title: "[Solution] MongoDB Server Selection Timeout Error"
description: "Fix MongoDB server selection timeout when no server is available"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Server Selection Timeout Error

The server selection timeout means no suitable server was found within the timeout window:

```
MongoServerSelectionError: Server selection timed out after 30000 ms
```

In a replica set context:

```
MongoServerSelectionError: No suitable server found
```

## Common Causes

- All members of the replica set are down
- The client cannot reach any member due to network issues
- Read preference settings exclude all available servers
- The replica set is in a split-brain state with no majority
- Max staleness settings are too restrictive
- The server is in maintenance mode or shutting down

## How to Fix

### 1. Increase server selection timeout

```javascript
const client = new MongoClient(uri, {
  serverSelectionTimeoutMS: 60000
});
```

### 2. Verify replica set members are running

```bash
for host in mongo1 mongo2 mongo3; do
  echo "Checking $host..."
  ssh $host "systemctl is-active mongod"
done
```

### 3. Check read preference settings

```javascript
// Ensure read preference allows reading from available members
const client = new MongoClient(uri, {
  readPreference: 'secondaryPreferred'
});
```

### 4. Verify maxStalenessSeconds

```javascript
// Don't set too restrictive a staleness value
const options = {
  readPreference: new ReadPreference('secondary', { maxStalenessSeconds: 120 })
};
```

## Examples

```bash
# Check which members are available
mongosh --eval "rs.status().members.forEach(m => print(m.name, m.stateStr, m.health))"

# Test connection to each member individually
mongosh --host mongo1 --eval "db.runCommand({ping:1})"
mongosh --host mongo2 --eval "db.runCommand({ping:1})"

# Check the replica set configuration
mongosh --eval "rs.conf().members.forEach(m => print(m.host, m.priority, m.votes))"
```