---
title: "[Solution] MongoDB Write Concern Majority Unreachable"
description: "Fix write concern majority errors when majority cannot be reached"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Write Concern Majority Unreachable

When write concern `w: "majority"` cannot be satisfied:

```
WriteConcernError: Not enough data-bearing nodes (1/3) to satisfy write concern majority
```

## Common Causes

- More than half of the replica set members are down
- A network partition prevents the primary from reaching a majority
- Members are in recovery state and not yet synchronized
- The replica set was reconfigured with fewer data-bearing members
- An arbiter is included but does not count toward majority

## How to Fix

### 1. Ensure enough members are online

```javascript
// Check replica set status
rs.status().members.forEach(m => {
  print(m.name, m.stateStr, m.health);
});
```

### 2. Restart downed members

```bash
ssh mongo2 "sudo systemctl start mongod"
ssh mongo3 "sudo systemctl start mongod"
```

### 3. Temporarily use a lower write concern

```javascript
// If you must write and cannot restore the majority
await db.users.insertOne(
  { name: "test" },
  { writeConcern: { w: 1, wtimeout: 5000 } }
);
```

### 4. Check for network partitions

```bash
# From the primary
ping mongo2
ping mongo3
traceroute mongo2
```

## Examples

```bash
# Check how many members are in the replica set
mongosh --eval "rs.status().members.length"

# Check the replica set config for voting members
mongosh --eval "rs.conf().members.map(m => ({host: m.host, votes: m.votes}))"

# Force a member to rejoin (if healthy)
mongosh --eval "rs.syncFrom('mongo1:27017')" --host mongo2
```