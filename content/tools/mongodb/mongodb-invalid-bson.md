---
title: "[Solution] MongoDB Invalid BSON Error"
description: "Fix invalid BSON errors when inserting or updating documents"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Invalid BSON Error

Invalid BSON data causes operations to fail:

```
MongoServerError: Invalid BSON: cannot decode element, type: 0
```

```
BSONError: Input must be a valid BSON document
```

## Common Causes

- Binary data was corrupted during transmission
- An embedded document contains null bytes or invalid UTF-8 characters
- The client driver generated malformed BSON
- Data was manually edited in a binary format
- A field contains a JavaScript function (`$where`) with invalid syntax
- Date values are out of the representable range

## How to Fix

### 1. Validate documents before insertion

```javascript
const bson = require('bson');

function validateBSON(doc) {
  try {
    bson.serialize(doc);
    return true;
  } catch (e) {
    console.error('Invalid BSON:', e.message);
    return false;
  }
}
```

### 2. Sanitize string fields

```javascript
function sanitizeString(str) {
  // Remove null bytes and invalid characters
  return str.replace(/\x00/g, '').replace(/[\x00-\x08\x0B\x0C\x0E-\x1F]/g, '');
}
```

### 3. Use proper BSON types instead of raw objects

```javascript
// Instead of passing raw Date strings
const doc = {
  createdAt: new Date(),           // Correct
};
```

### 4. Check for data corruption in existing documents

```javascript
db.myCollection.find().forEach(doc => {
  try {
    bson.serialize(doc);
  } catch (e) {
    print("Corrupted doc _id:", doc._id);
  }
});
```

## Examples

```bash
# Validate all documents in a collection
mongosh --eval '
  let errors = 0;
  db.mycol.find().forEach(doc => {
    try { bson.serialize(doc); }
    catch(e) { errors++; print("Bad doc:", doc._id); }
  });
  print("Total errors:", errors);
'

# Check collection integrity
mongosh --eval "db.mycol.validate({full: true})"

# Export and re-import to fix corruption
mongoexport --db mydb --collection mycol --out backup.json
mongoimport --db mydb --collection mycol --file backup.json
```