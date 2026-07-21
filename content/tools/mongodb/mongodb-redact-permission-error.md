---
title: "[Solution] MongoDB $redact Permission Denied Error"
description: "Fix MongoDB $redact permission denied error when document-level access control filters out all documents"
tools: ["mongodb"]
error-types: ["tool-error"]
severities: ["error"]
---

# MongoDB $redact Permission Denied Error

The $redact stage removes all documents because none satisfy the access control conditions. The result is an empty pipeline output when some documents were expected.

## Common Causes

- User does not have the required role to view documents
- Document field values do not match the $$DESCEND or $$KEEP expressions
- Access level field is missing or has unexpected values
- Field name in $$PRUNE conditions does not exist in documents
- Role hierarchy does not include the required access level

## How to Fix

### Verify User Roles

```javascript
// Check user permissions
db.getUsers()

// Check specific user roles
db.getUser('analyst')

// Grant appropriate role
db.grantRolesToUser('analyst', [{
  role: 'read',
  db: 'analytics'
}])
```

### Check Document Structure

```javascript
// Ensure documents have the access control field
db.collection('reports').find({
  accessLevel: { $exists: true }
})

// Sample document
// { _id: 1, data: "...", accessLevel: "confidential", dept: "finance" }
```

### Fix $redact Pipeline

```javascript
db.collection('reports').aggregate([
  {
    $redact: {
      $cond: {
        if: { $gte: ['$$accessLevel', 2] },  // access level 2+
        then: '$$DESCEND',
        else: '$$PRUNE'
      }
    }
  },
  { $match: { dept: 'finance' } }
])
```

### Add Debugging to $redact

```javascript
// Debug: see which documents are being redacted
db.collection('reports').aggregate([
  { $addFields: { _originalAccessLevel: '$accessLevel' } },
  {
    $redact: {
      $cond: {
        if: { $eq: ['$$accessLevel', 'public'] },
        then: '$$DESCEND',
        else: '$$PRUNE'
      }
    }
  }
])
```

## Examples

```
MongoServerError: $redact pipeline returned 0 documents
  All documents were redacted. Check access level fields.

MongoServerError: $$DESCEND requires the field "accessLevel"
  to exist in the document
```

## Related Errors

- [MongoDB Authorization Failure]({{< relref "/tools/mongodb/mongodb-authorization-failure" >}}) -- auth issues
- [MongoDB Privilege Check Error]({{< relref "/tools/mongodb/mongodb-privilege-check-error" >}}) -- privilege issues
- [MongoDB Role Not Found]({{< relref "/tools/mongodb/mongodb-role-not-found" >}}) -- role issues
