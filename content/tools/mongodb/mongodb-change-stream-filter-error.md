---
title: "[Solution] MongoDB Change Stream Filter Error"
description: "Fix MongoDB change stream filter error when invalid match expression is used in change stream pipeline"
tools: ["mongodb"]
error-types: ["tool-error"]
severities: ["error"]
---

# MongoDB Change Stream Filter Error

A change stream pipeline receives an invalid or unsupported filter expression. Change streams have a limited subset of aggregation stages available for filtering.

## Common Causes

- Using unsupported aggregation stages in the change stream pipeline
- Invalid field references in the $match filter
- Attempting to use $lookup or $unwind in change stream pipeline
- Filter references fields that do not exist in the change event
- Using update descriptions in the filter that are not available

## How to Fix

### Use Valid Change Stream Stages

```javascript
// Valid: $match with change event fields
const changeStream = db.collection('orders').watch([
  {
    $match: {
      'operationType': { $in: ['insert', 'update', 'replace'] },
      'fullDocument.status': 'urgent'
    }
  }
]);

// Valid: $project to reshape events
const changeStream2 = db.collection('orders').watch([
  {
    $project: {
      operationType: 1,
      documentKey: 1,
      fullDocument: 1
    }
  }
]);
```

### Filter by Operation Type

```javascript
const stream = db.collection('users').watch([
  { $match: { operationType: 'insert' } }  // only new documents
]);

stream.on('change', (change) => {
  console.log('New user:', change.fullDocument);
});
```

### Filter by Updated Fields

```javascript
const stream = db.collection('orders').watch([
  {
    $match: {
      'updateDescription.updatedFields': {
        $exists: true
      },
      'updateDescription.updatedFields.status': 'shipped'
    }
  }
]);
```

### Filter by Document Key

```javascript
// Watch specific documents only
const stream = db.collection('orders').watch([], {
  filter: {
    $or: [
      { 'documentKey._id': { $in: ['order-1', 'order-2'] } }
    ]
  }
});
```

## Examples

```
MongoServerError: $lookup is not supported in change stream pipeline

MongoServerError: unsupported stage "$unwind" in change stream pipeline
  supported stages: $match, $project, $addFields, $set, $unset

MongoServerError: cannot reference "fullDocument.status" in $match
  because fullDocument is not available for delete operations
```

## Related Errors

- [MongoDB Change Stream Error]({{< relref "/tools/mongodb/mongodb-change-stream-error" >}}) -- change stream issues
- [MongoDB Change Stream Resume Failed]({{< relref "/tools/mongodb/mongodb-change-stream-resume-failed" >}}) -- resume issues
- [MongoDB Aggregation Error]({{< relref "/tools/mongodb/mongodb-aggregation-error" >}}) -- aggregation issues
