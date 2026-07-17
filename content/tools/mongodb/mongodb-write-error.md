---
title: "MongoDB Write Error"
description: "MongoDB write operation fails due to write concern, validation, or write conflict."
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

# MongoDB Write Error

A MongoDB write error occurs when a write operation (insert, update, delete) fails. This can be caused by write concern issues, document validation failures, or write conflicts.

## Common Causes

- Write concern timeout exceeded
- Document validation rules violated
- Write conflict in multi-statement transactions
- Disk space exhaustion

## How to Fix

### Check Write Concern

```javascript
db.collection.insertOne(
  { name: 'test' },
  { writeConcern: { w: 'majority', wtimeout: 5000 } }
);
```

### Validate Document Schema

```javascript
db.createCollection('users', {
  validator: {
    $jsonSchema: {
      bsonType: 'object',
      required: ['name', 'email'],
      properties: {
        name: { bsonType: 'string' },
        email: { bsonType: 'string' }
      }
    }
  }
});
```

### Handle Write Conflicts

```javascript
const session = client.startSession();
try {
  session.startTransaction();
  await collection.updateOne({ _id: 1 }, { $inc: { count: 1 } }, { session });
  await session.commitTransaction();
} catch (e) {
  await session.abortTransaction();
}
```

### Check Disk Space

```bash
df -h /var/lib/mongodb
```

### Reduce Write Concern for Performance

```javascript
db.collection.insertOne(
  { name: 'test' },
  { writeConcern: { w: 1 } }  // Acknowledge from primary only
);
```

## Examples

```javascript
// Write concern timeout
MongoServerError: Not enough data-bearing nodes (5ms timeout)

// Document validation
MongoServerError: Document failed validation
```

## Related Errors

- [Duplicate Key Error]({{< relref "/tools/mongodb/duplicate-key" >}}) — duplicate key violation
- [Timeout Error]({{< relref "/tools/mongodb/timeout-error" >}}) — operation timeout
