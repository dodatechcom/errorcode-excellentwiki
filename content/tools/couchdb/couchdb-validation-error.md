---
title: "[Solution] CouchDB Validation Error — How to Fix"
description: "Fix CouchDB validation errors by resolving validation function failures, fixing document validation issues, and handling design doc validation errors"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Validation Error

CouchDB validation errors occur when validation functions in design documents reject document updates due to invalid data or schema violations.

## Why It Happens

- Document does not match validation rules
- Validation function is too restrictive
- Validation function contains bugs
- Required fields are missing
- Field types are incorrect
- Validation function throws an exception

## Common Error Messages

```
{ "error": "forbidden", "reason": "Document failed validation" }
```

```
{ "error": "forbidden", "reason": "Validation failed: ..." }
```

```
{ "error": "internal_server_error", "reason": "Validation function error" }
```

```
{ "error": "bad_request", "reason": "Invalid document format" }
```

## How to Fix It

### 1. Fix Validation Function

```bash
# Define correct validation function
curl -X PUT http://localhost:5984/mydb/_design/app \
  -H "Content-Type: application/json" \
  -d '{
    "_id": "_design/app",
    "validate_doc_update": "function(newDoc, oldDoc, userCtx) { if (!newDoc.type) { throw({forbidden: \"Document must have type field\"}); } if (newDoc.type === \"event\" && !newDoc.timestamp) { throw({forbidden: \"Event must have timestamp\"}); } }"
  }'
```

### 2. Fix User Permissions

```bash
# Check user context
curl http://localhost:5984/_session | jq '.userCtx'

# Validation should check userCtx for write permissions
curl -X PUT http://localhost:5984/mydb/_design/app \
  -H "Content-Type: application/json" \
  -d '{
    "_id": "_design/app",
    "validate_doc_update": "function(newDoc, oldDoc, userCtx) { if (!userCtx.name) { throw({unauthorized: \"Login required\"}); } }"
  }'
```

### 3. Test Validation Function

```bash
# Test validation with valid doc
curl -X PUT http://localhost:5984/mydb/valid_doc \
  -H "Content-Type: application/json" \
  -d '{"type": "event", "timestamp": "2024-01-01"}'

# Test validation with invalid doc
curl -X PUT http://localhost:5984/mydb/invalid_doc \
  -H "Content-Type: application/json" \
  -d '{"name": "no type field"}'
```

### 4. Debug Validation Function

```bash
# Enable debugging
curl -X PUT http://localhost:5984/mydb/_design/app \
  -H "Content-Type: application/json" \
  -d '{
    "_id": "_design/app",
    "validate_doc_update": "function(newDoc, oldDoc, userCtx) { if (!newDoc.type) { throw({forbidden: \"Missing type\"}); } log(\"Validation passed\"); }"
  }'
```

## Common Scenarios

- **Document rejected**: Check the validation function requirements.
- **User not authorized**: Ensure userCtx is checked in validation function.
- **Validation function error**: Fix JavaScript syntax in validation function.

## Prevent It

- Test validation functions with various document types
- Provide clear error messages in validation functions
- Allow admin users to bypass validation when necessary

## Related Pages

- [CouchDB Design Doc Error](/tools/couchdb/couchdb-design-doc-error)
- [CouchDB Document Error](/tools/couchdb/couchdb-document-error)
- [CouchDB Security Error](/tools/couchdb/couchdb-security-error)
