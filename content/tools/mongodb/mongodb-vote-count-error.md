---
title: "[Solution] MongoDB Replica Set Vote Count Error"
description: "Fix MongoDB replica set voting member count errors"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Replica Set Vote Count Error

```
MongoServerError: ReplSet cfg has members that cast 2 votes, which is invalid
```

## Common Causes

- More than 7 voting members in the replica set
- A member has more than 1 vote configured
- The number of voting members is even

## How to Fix

### 1. Limit voting members to 7 or fewer

```javascript
rs.reconfig({
  _id: "rs0",
  members: [
    { _id: 0, host: "mongo1:27017", votes: 1 },
    { _id: 1, host: "mongo2:27017", votes: 1 },
    { _id: 2, host: "mongo3:27017", votes: 1 },
    { _id: 3, host: "mongo4:27017", votes: 0 }
  ]
});
```

### 2. Ensure an odd number of voting members

```javascript
// Use an arbiter for even-numbered setups
rs.initiate({
  _id: "rs0",
  members: [
    { _id: 0, host: "mongo1:27017" },
    { _id: 1, host: "mongo2:27017" },
    { _id: 2, host: "mongo3:27017" },
    { _id: 3, host: "mongo4:27017" },
    { _id: 4, host: "arbiter:27017", arbiterOnly: true }
  ]
});
```

### 3. Check current vote configuration

```javascript
rs.conf().members.forEach(m => {
  print(m.host, "votes:", m.votes, "priority:", m.priority);
});
```

## Examples

```bash
# Check voting members
mongosh --eval '
  rs.conf().members.forEach(m => {
    print(m.host, "votes:", m.votes);
  });
'

# Change a member to non-voting
mongosh --eval '
  let config = rs.conf();
  config.members[3].votes = 0;
  rs.reconfig(config);
'
```