---
title: "[Solution] MongoDB No Primary Available"
description: "Fix MongoDB replica set no primary available errors"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB No Primary Available Error

```
MongoServerError: not primary and secondaryOk=false
```

```
MongoServerSelectionError: No replica set primary available
```

## Common Causes

- The replica set is in the process of electing a new primary
- All eligible nodes are down or unreachable
- A network partition has isolated the primary
- The primary has stepped down
- There are not enough voting members to elect a primary

## How to Fix

### 1. Check replica set status

```javascript
rs.status()
rs.isMaster()
```

### 2. Wait for election to complete

Elections typically take 10-15 seconds. Wait and retry.

### 3. Read from secondaries if allowed

```javascript
const client = new MongoClient(uri, {
  readPreference: 'secondaryPreferred'
});
```

Or with mongosh:

```bash
mongosh --readPreference secondaryPreferred
```

### 4. Check network connectivity between members

```bash
mongosh --eval "rs.status().members.forEach(m => print(m.name, m.stateStr, m.optimeDate))"
```

## Examples

```bash
# Check who is primary
mongosh --eval "rs.isMaster().primary"

# Check member states
mongosh --eval '
  rs.status().members.forEach(m => {
    print(m.name, m.stateStr, "votes:", m.votes, "priority:", m.priority);
  });
'

# Read from secondary
mongosh --readPreference secondaryPreferred --eval "db.users.find().limit(5).toArray()"
```