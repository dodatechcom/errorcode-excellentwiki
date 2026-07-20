---
title: "[Solution] MongoDB Unknown Operator Error"
description: "Fix MongoDB unknown operator errors in queries"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Unknown Operator Error

```
MongoServerError: Unrecognized pipeline stage name: '$invalidStage'
```

```
unknown operator: $invalid
```

## Common Causes

- The operator name is misspelled
- The operator is from a newer version of MongoDB
- The operator is used in the wrong context (e.g., aggregation operator in find)
- The operator does not exist

## How to Fix

### 1. Check the operator spelling

```javascript
// Correct
db.users.find({ age: { $gte: 18 } })

// Wrong
db.users.find({ age: { $great: 18 } })
```

### 2. Use the correct operator for the context

```javascript
// Aggregation operators
db.users.aggregate([
  { $match: { age: { $gte: 18 } } },
  { $group: { _id: "$city", count: { $sum: 1 } } }
])

// Find operators
db.users.find({ age: { $gte: 18 }, city: "NYC" })
```

### 3. Check MongoDB version for supported operators

```javascript
db.adminCommand({ buildInfo: 1 }).version
```

## Examples

```bash
# Test operator syntax
mongosh --eval '
  try {
    db.test.find({field: {$invalid: 1}});
  } catch(e) { print("Error:", e.message); }
'

# List aggregation stages
mongosh --eval "db.adminCommand({listCommands:1}).commands | grep aggregate"
```