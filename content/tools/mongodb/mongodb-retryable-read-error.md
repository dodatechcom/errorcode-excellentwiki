---
title: "[Solution] MongoDB Retryable Read Error"
description: "Fix MongoDB retryable read error when read operations fail and cannot be automatically retried by the driver"
tools: ["mongodb"]
error-types: ["tool-error"]
severities: ["error"]
---

# MongoDB Retryable Read Error

A read operation fails and the driver cannot retry it because the error is not retryable or the read concern is not supported for retries.

## Common Causes

- Read operation against a single node (not a replica set)
- Error code indicates non-retryable failure (e.g., authentication error)
- Read concern "snapshot" is not retryable in some contexts
- Driver version does not support retryable reads
- Operation was sent to a mongos that cannot retry across shards

## How to Fix

### Enable Retryable Reads

```javascript
const client = new MongoClient(uri, {
  retryReads: true  // default: true in driver 3.6+
});
```

### Handle Non-Retryable Errors Manually

```javascript
async function readWithRetry(collection, filter) {
  const maxRetries = 3;
  for (let i = 0; i < maxRetries; i++) {
    try {
      return await collection.find(filter).toArray();
    } catch (err) {
      if (isRetryable(err) && i < maxRetries - 1) {
        console.log(`Retry ${i + 1}: ${err.message}`);
        await sleep(100 * Math.pow(2, i));
        continue;
      }
      throw err;
    }
  }
}

function isRetryable(err) {
  const retryableCodes = [6, 7, 89, 91, 189, 262, 9001, 10107, 11600, 13435];
  return retryableCodes.includes(err.code);
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}
```

### Use Replica Set for Retry Support

```javascript
// Retryable reads require a replica set or mongos
const uri = 'mongodb://mongo1:27017,mongo2:27017/?replicaSet=rs0';
const client = new MongoClient(uri, { retryReads: true });
```

## Examples

```
MongoServerError: read at cluster time {
  clusterTime: Timestamp(1715000000, 1)
} has been rolled back by stepdown

MongoServerError: Retryable read error on <mongo1:27017>:
  node is no longer primary (10107)
```

## Related Errors

- [MongoDB Read Error]({{< relref "/tools/mongodb/mongodb-read-error" >}}) -- read issues
- [MongoDB Retryable Write Error]({{< relref "/tools/mongodb/mongodb-retryable-write-error" >}}) -- write retries
- [MongoDB Server Selection Timeout]({{< relref "/tools/mongodb/mongodb-server-selection-timeout" >}}) -- selection issues
