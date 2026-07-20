---
title: "[Solution] MongoDB Update Validation Error"
description: "Fix MongoDB update validation errors on documents"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Update Validation Error

Update validation errors occur when an update operation violates schema validation rules:

```
MongoServerError: Document failed validation
```

```
WriteError: Document failed validation
{ index: 0, code: 121, errmsg: 'Document failed validation' }
```

## Common Causes

- The update produces a document that violates a `$jsonSchema` validation rule
- The update tries to set a field to a value outside the allowed range
- Required fields are being removed or set to null
- The document no longer matches the collection validator after the update
- A `$rename` operation causes a required field to become missing

## How to Fix

### 1. Review the collection validator

```javascript
db.getCollectionInfos({ name: "myCollection" })[0].options.validator
```

### 2. Check what the update would produce

```javascript
// Run a find with the same filter to see affected documents
const docs = await db.myCollection.find({ _id: 1 }).toArray();
console.log("Before:", docs[0]);
```

### 3. Use validationAction: "warn" during development

```javascript
db.createCollection("myCollection", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["name", "email"],
      properties: {
        name: { bsonType: "string" },
        email: { bsonType: "string" }
      }
    }
  },
  validationAction: "warn"  // Log warnings but allow the operation
});
```

### 4. Relax the validator temporarily

```javascript
db.runCommand({
  collMod: "myCollection",
  validationLevel: "moderate"  // Only validate new documents and updates to existing valid documents
});
```

## Examples

```bash
# View the current validator
mongosh --eval "db.getCollectionInfos({name:'users'})[0].options.validator"

# Test an update that violates validation
mongosh --eval '
  db.users.updateOne({_id:1}, {$set:{age:-5}});
'

# Temporarily disable validation
mongosh --eval '
  db.runCommand({collMod:"users", validationLevel:"off"});
  db.users.updateOne({_id:1}, {$set:{age:-5}});
  db.runCommand({collMod:"users", validationLevel:"strict"});
'
```