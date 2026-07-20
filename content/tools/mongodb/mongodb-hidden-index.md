---
title: "[Solution] MongoDB Hidden Index Error"
description: "Fix MongoDB hidden index issues and queries ignoring indexes"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Hidden Index Error

Hidden indexes are not used by the query planner:

```
// Queries may perform collection scans instead of using the hidden index
```

## Common Causes

- An index was marked hidden during testing and not unhidden
- The query planner does not consider hidden indexes for query plans
- Performance degrades because the query falls back to a collection scan
- The index was hidden via `collMod` and forgotten

## How to Fix

### 1. Check if any indexes are hidden

```javascript
db.users.getIndexes().forEach(idx => {
  if (idx.hidden) {
    print("HIDDEN:", idx.name);
  }
});
```

### 2. Unhide an index

```javascript
db.runCommand({
  collMod: "users",
  index: {
    name: "email_1",
    hidden: false
  }
});
```

### 3. Use hidden indexes for testing before making them visible

```javascript
// Create an index as hidden first
db.users.createIndex({ email: 1 }, { hidden: true });

// Test that it works as expected
db.users.find({ email: "test@example.com" }).explain("executionStats");

// Unhide when ready
db.runCommand({ collMod: "users", index: { name: "email_1", hidden: false } });
```

### 4. Verify the query is using the correct index

```javascript
db.users.find({ email: "test@example.com" }).explain("executionStats");
// Check which index was used
// If the query does a COLLSCAN, check if the index is hidden
```

## Examples

```bash
# Find all hidden indexes
mongosh --eval '
  db.users.getIndexes().forEach(i => {
    if (i.hidden) print("Hidden:", i.name, JSON.stringify(i.key));
  });
'

# Create a hidden index, test, then unhide
mongosh --eval '
  db.users.createIndex({email:1}, {hidden:true});
  let plan = db.users.find({email:"test@test.com"}).explain("executionStats");
  print("Index used:", plan.executionStats.stage);
  db.runCommand({collMod:"users", index:{name:"email_1", hidden:false}});
'
```