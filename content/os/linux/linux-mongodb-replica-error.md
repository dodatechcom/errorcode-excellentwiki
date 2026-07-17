---
title: "[Solution] Linux MongoDB Replica Set Not Primary"
description: "Fix Linux MongoDB 'replica set not primary' errors. Resolve replica set election issues, primary election failures, and write concern errors."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["mongodb", "replica-set", "not-primary", "election", "database"]
weight: 5
---

# Linux: MongoDB — replica set not primary

The `not primary` or `not master` error in MongoDB means the client attempted a write operation (insert, update, delete) against a secondary node or a node that has not been elected primary in the replica set. Only the primary node accepts writes in a standard MongoDB replica set.

## What This Error Means

MongoDB replica sets use the Raft consensus protocol to elect a primary node. All writes must go to the primary, which then replicates to secondaries. When a client connects to a secondary for writes, or during an election when no primary exists, the server returns `notPrimary` or `not master`. This is by design — data consistency requires writes to go through the primary.

## Common Causes

- Client connecting to a secondary node instead of the primary
- Replica set election in progress (no primary exists)
- Primary stepped down or crashed
- Network partition isolating the primary
- Replica set has too few healthy members to elect a primary
- `rs.stepDown()` was called for maintenance
- Client driver not configured with the correct replica set name

## How to Fix

### 1. Identify the Current Primary

```bash
# Check replica set status
mongosh --eval "rs.status()"

# Find the primary
mongosh --eval "rs.status().members.map(m => ({name: m.name, state: m.stateStr}))"

# Quick check
mongosh --eval "db.isMaster()"
```

### 2. Configure Driver to Read from Primary

```bash
# In the connection string, use the replica set name
# This allows the driver to automatically find the primary

# MongoDB connection string:
mongodb://user:password@host1:27017,host2:27017,host3:27017/?replicaSet=myrs

# With read preference for primary
mongodb://user:password@host1:27017,host2:27017,host3:27017/?replicaSet=myrs&readPreference=primary
```

### 3. Check Replica Set Health

```bash
# View full replica set status
mongosh --eval "rs.status()" --pretty

# Check member states
mongosh --eval "
  rs.status().members.forEach(function(m) {
    print(m.name + ': ' + m.stateStr + ' (optime: ' + m.optimeDate + ')');
  })
"

# Look for:
# - PRIMARY: the node accepting writes
# - SECONDARY: read-only replica
# - DOWN/UNREACHABLE: member is unreachable
# - STARTING: member is starting up
```

### 4. Fix Election Issues

```bash
# Check if a majority of members are available
mongosh --eval "
  var status = rs.status();
  var members = status.members.length;
  var alive = status.members.filter(m => m.stateStr !== 'DOWN').length;
  print('Members: ' + alive + '/' + members + ' alive');
  print('Majority needed: ' + Math.floor(members/2 + 1));
"

# If majority is not met, start the downed members
sudo systemctl start mongod

# Force a reconfig if needed (dangerous)
mongosh --eval "rs.reconfig(rs.conf(), {force: true})"
```

### 5. Step Down the Primary for Maintenance

```bash
# Gracefully step down primary (triggers election)
mongosh --eval "rs.stepDown(60)"

# Wait for a secondary to catch up before stepping down
mongosh --eval "rs.syncFrom('primary-host:27017')"

# Check new primary
mongosh --eval "rs.status().members.filter(m => m.stateStr === 'PRIMARY')"
```

### 6. Fix Network Issues

```bash
# Check connectivity between replica set members
mongosh --host host1 --eval "db.adminCommand({ping: 1})"
mongosh --host host2 --eval "db.adminCommand({ping: 1})"
mongosh --host host3 --eval "db.adminCommand({ping: 1})"

# Check if members can reach each other
# MongoDB uses the port in the replica set config
ss -tlnp | grep 27017
```

### 7. Reconfigure Replica Set

```bash
# If members are misconfigured
mongosh --eval "rs.conf()"

# Reconfigure with updated member list
mongosh --eval "
  var config = rs.conf();
  config.members[1].host = 'new-host:27017';
  rs.reconfig(config);
"

# Add a new member
mongosh --eval "rs.add('new-host:27017')"

# Remove a problematic member
mongosh --eval "rs.remove('bad-host:27017')"
```

## Examples

```bash
$ mongosh --eval "db.users.insertOne({name: 'test'})"
MongoServerError: not primary and ok=false

$ mongosh --eval "rs.status().members.map(m => m.name + ': ' + m.stateStr)"
[ 'host1:27017: PRIMARY', 'host2:27017: SECONDARY', 'host3:27017: DOWN' ]

$ mongosh --host host2:27017 --eval "db.adminCommand({replSetGetStatus: 1})"
# host2 is secondary — cannot accept writes

# Connect to primary instead
$ mongosh --host host1:27017 --eval "db.users.insertOne({name: 'test'})"
{ acknowledged: true, insertedId: ObjectId(...) }

# Or use the connection string with replicaSet
$ mongosh "mongodb://host1:27017,host2:27017,host3:27017/?replicaSet=rs0"
```

## Related Errors

- [MongoDB replica set error]({{< relref "/os/linux/linux-mongodb-replica-error" >}}) — General replica set issues
- [PostgreSQL connection refused]({{< relref "/os/linux/linux-postgres-connection-refused" >}}) — PostgreSQL connection issues
- [MySQL connection refused]({{< relref "/os/linux/linux-mysql-connection-refused" >}}) — MySQL connection issues
