---
title: "[Solution] MongoDB TTL Index Error"
description: "Fix MongoDB TTL index creation and expiration errors"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB TTL Index Error

TTL indexes may not work as expected:

```
MongoServerError: Only non-compound, non-array, non-geo fields can have a TTL index
```

TTL indexes that exist but do not delete documents are a common issue.

## Common Causes

- The TTL index is on a compound index (not allowed)
- The field is an array (not allowed for TTL)
- The field does not contain a Date type value
- The TTL monitor has not run yet (runs every 60 seconds)
- The indexed field is a string instead of a Date
- The TTL index was created on `_id` (not supported)

## How to Fix

### 1. Ensure the TTL field contains Date objects

```javascript
// Correct
await db.sessions.insertOne({
  sessionId: "abc123",
  createdAt: new Date()  // Date object, not string
});

// Wrong
await db.sessions.insertOne({
  sessionId: "abc123",
  createdAt: "2024-01-15T00:00:00Z"  // String, not Date
});
```

### 2. Create TTL index on a single non-array field

```javascript
// Correct
db.sessions.createIndex({ createdAt: 1 }, { expireAfterSeconds: 3600 });

// Wrong: compound index
db.sessions.createIndex({ createdAt: 1, userId: 1 }, { expireAfterSeconds: 3600 });
```

### 3. Wait for the TTL monitor

The TTL monitor runs every 60 seconds. Be patient.

### 4. Use expireAfterSeconds: 0 for immediate expiration

```javascript
db.logs.createIndex({ expireAt: 1 }, { expireAfterSeconds: 0 });
```

## Examples

```bash
# Set up a TTL collection
mongosh --eval '
  db.sessions.drop();
  db.sessions.createIndex({createdAt:1}, {expireAfterSeconds: 10});
  db.sessions.insertOne({data:"temp", createdAt: new Date()});
  print("Document inserted. Waiting for TTL monitor...");
'

# Check TTL index configuration
mongosh --eval '
  db.sessions.getIndexes().forEach(i => {
    if (i.expireAfterSeconds !== undefined) {
      print(i.name, "TTL:", i.expireAfterSeconds, "seconds");
    }
  });
'
```