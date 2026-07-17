---
title: "MongoDB Replica Set Error"
description: "MongoDB replica set encounters issues with elections, sync, or member health."
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
tags: ["mongodb", "replica-set", "election", "sync", "high-availability"]
weight: 5
---

# MongoDB Replica Set Error

A MongoDB replica set error occurs when the replica set encounters issues with member elections, data synchronization, or member health. This affects high availability and data redundancy.

## Common Causes

- Primary node unavailable or crashed
- Network partition between members
- Insufficient replica set members for quorum
- Member lagging too far behind in replication

## How to Fix

### Check Replica Set Status

```javascript
rs.status()
rs.printReplicationInfo()
rs.printSecondaryReplicationInfo()
```

### Check Member Health

```javascript
rs.status().members.forEach(m => {
  print(m.name, m.stateStr, m.optimeDate)
})
```

### Force Election

```javascript
rs.stepDown()
// Or on a secondary
rs.syncFrom('primary:27017')
```

### Add Missing Member

```javascript
rs.add('newmember:27017')
```

### Fix Network Connectivity

```bash
# Ensure all members can communicate
mongo --host member1:27017 --eval "rs.status()"
```

### Configure Replica Set

```javascript
rs.initiate({
  _id: 'rs0',
  members: [
    { _id: 0, host: 'member1:27017' },
    { _id: 1, host: 'member2:27017' },
    { _id: 2, host: 'member3:27017' }
  ]
})
```

## Examples

```javascript
// No primary
rs.status().myState  // 2 (secondary)
MongoError: no primary found in replica set

// Fix: check member health and force election
rs.status().members
```

## Related Errors

- [Connection Error]({{< relref "/tools/mongodb/mongodb-connection-error" >}}) — connection failure
- [Write Error]({{< relref "/tools/mongodb/write-concern" >}}) — write concern error
