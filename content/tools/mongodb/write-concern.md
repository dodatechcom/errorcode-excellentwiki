---
title: "MongoDB WriteConcernError: not enough data-bearing nodes"
description: "MongoDB rejects a write operation because fewer data-bearing nodes are available than the write concern requires"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
tags: ["write-concern", "replica-set", "write", "availability"]
weight: 5
---

This error occurs when a write operation specifies a write concern (e.g. `w: 3` or `w: "majority"`) but not enough data-bearing replica set members are available to satisfy it.

## Common Causes

- A replica set member has gone down or is lagging behind
- The write concern level is set higher than the number of healthy data-bearing nodes
- Network partition between the application and replica set members
- Misconfigured write concern in connection options

## How to Fix

1. Check replica set status:

```javascript
rs.status()
```

2. Use a more lenient write concern for non-critical writes:

```javascript
db.collection.insertOne({ name: "Alice" }, { writeConcern: { w: 1 } })
```

3. Adjust the connection string write concern:

```javascript
const client = new MongoClient(uri, {
  writeConcern: { w: "majority", wtimeoutMS: 5000 }
})
```

4. Add `wtimeout` to avoid indefinite blocking:

```javascript
db.collection.insertOne(
  { name: "Alice" },
  { writeConcern: { w: "majority", wtimeout: 5000 } }
)
```

## Examples

```javascript
// Replicaset with 2 members, write concern w: 3
db.users.insertOne({ name: "Alice" }, { writeConcern: { w: 3 } })
// WriteConcernError: not enough data-bearing nodes
```

## Related Errors

- [E11000 duplicate key error collection](/tools/mongodb/duplicate-key)
