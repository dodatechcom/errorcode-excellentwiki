---
title: "[Solution] MongoDB Read Preference Error"
description: "Fix MongoDB read preference error when the specified read mode cannot find a suitable replica set member"
tools: ["mongodb"]
error-types: ["tool-error"]
severities: ["error"]
---

# MongoDB Read Preference Error

The driver cannot find a suitable replica set member matching the specified read preference. Reads fail when no member matches the mode, tag sets, or max staleness constraints.

## Common Causes

- No secondary members are available for secondaryPreferred reads
- Tag sets do not match any available members
- maxStalenessSeconds is set too low for current replication lag
- Read preference tags reference removed or renamed members
- All matching members are down or unreachable

## How to Fix

### Check Replica Set Status

```javascript
rs.status()

// Check member states and tags
rs.status().members.forEach(m => {
  console.log(m.name, m.stateStr, m.tags);
})
```

### Adjust Read Preference

```javascript
const client = new MongoClient(uri, {
  readPreference: 'secondaryPreferred',
  readPreferenceTags: [
    { region: 'us-east', tier: 'readonly' },  // prefer these tags
    { region: '' }                              // fallback: any region
  ],
  maxStalenessSeconds: 60  // allow up to 60s stale data
});
```

### Use Flexible Tag Matching

```javascript
const readPrefs = [{
  mode: 'secondary',
  tags: [{ datacenter: 'us-east' }]   // prefer us-east
}, {
  mode: 'secondary',
  tags: [{ datacenter: 'eu-west' }]   // fallback to eu-west
}, {
  mode: 'secondaryPreferred'          // fallback to any secondary
}];
```

### Set Realistic maxStalenessSeconds

```javascript
// Set high enough to account for replication lag
const client = new MongoClient(uri, {
  readPreference: 'secondary',
  maxStalenessSeconds: 120  // allow 2 min staleness
});
```

## Examples

```
MongoServerError: No suitable server for read preference
  { mode: "secondary", tags: [{ region: "us-west" }] }

MongoServerError: maxStalenessSeconds value of 5 is too low.
  Replication lag is currently 30 seconds.
```

## Related Errors

- [MongoDB Replication Lag]({{< relref "/tools/mongodb/mongodb-replication-lag" >}}) -- replica lag
- [MongoDB Server Selection Timeout]({{< relref "/tools/mongodb/mongodb-server-selection-timeout" >}}) -- server selection
- [MongoDB Replica Set Error]({{< relref "/tools/mongodb/mongodb-replica-set-error" >}}) -- replica issues
