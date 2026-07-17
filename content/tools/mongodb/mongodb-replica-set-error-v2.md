---
title: "MongoDB - not primary - read preference error"
description: "MongoDB read operation fails because it is routed to a secondary node without proper read preference configuration"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
tags: ["mongodb", "replica-set", "primary", "read-preference", "secondary", "not-primary"]
weight: 5
---

A "not primary" read preference error occurs when a read operation is sent to a secondary replica set member that is not configured to accept reads, or when the primary node is unavailable and read preference is not set for secondaries.

## Common Causes

- Default read preference sends reads to primary only
- Primary node is down and no secondary accepts reads
- Secondary node not configured with `readPreference: secondary`
- Operations that require primary (e.g., writes) sent to secondary
- `readConcern` level incompatible with read preference

## How to Fix

1. Set read preference for secondary reads:

```javascript
const collection = db.collection('analytics', {
  readPreference: ReadPreference.SECONDARY_PREFERRED,
});
const results = await collection.find({}).toArray();
```

2. Use read preference tags for data center routing:

```javascript
const secondaryInDC = new ReadPreference('secondary', [
  { region: 'us-east', dc: 'secondary' },
]);
const collection = db.collection('logs', {
  readPreference: secondaryInDC,
});
```

3. Handle primary not available:

```javascript
try {
  const result = await db.collection('users').findOne({ _id: userId });
} catch (error) {
  if (error.code === 10107 || error.message.includes('not primary')) {
    // Fallback to secondary read
    const collection = db.collection('users', {
      readPreference: ReadPreference.SECONDARY_PREFERRED,
    });
    return await collection.findOne({ _id: userId });
  }
  throw error;
}
```

4. Configure read concern with secondaries:

```javascript
const result = await db.collection('events')
  .find({})
  .readConcern('majority')
  .toArray();
```

5. Check replica set status:

```javascript
const status = await db.admin().replSetGetStatus();
console.log('Primary:', status.members.find(m => m.stateStr === 'PRIMARY')?.name);
```

## Examples

```javascript
// Error: not primary and secondaryOk=false
const result = await db.collection('users').findOne({ _id: 1 });
// When connected to secondary without read preference

// Fix: set read preference
const collection = db.collection('users', {
  readPreference: ReadPreference.SECONDARY_PREFERRED,
});
const result = await collection.findOne({ _id: 1 });
```

## Related Errors

- [Replica set error]({{< relref "/tools/mongodb/mongodb-replica-set-error-v2" >}})
- [Connection error]({{< relref "/tools/mongodb/mongodb-connection-error" >}})
