---
title: "[Solution] CouchDB Security Error — How to Fix"
description: "Fix CouchDB security errors by configuring database security objects, setting admin roles, and resolving access denied issues"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Security Error

CouchDB security errors occur when users lack permissions to access databases, design documents, or admin endpoints. Security is configured through database security objects and role-based access.

## Why It Happens

- User is not in the required admin or reader role
- Database security object blocks access
- CORS configuration prevents browser requests
- Admin endpoint requires `_admin` role
- Design document has restricted access
- Missing authentication header in requests

## Common Error Messages

```
{ "error": "forbidden", "reason": "You must be an admin to perform this operation." }
```

```
{ "error": "unauthorized", "reason": "Name or password is incorrect." }
```

```
{ "error": "forbidden", "reason": "You are not allowed to access this db." }
```

```
{ "error": "forbidden", "reason": "only_admin" }
```

## How to Fix It

### 1. Configure Database Security Object

```bash
# Set database security
curl -X PUT http://localhost:5984/mydb/_security \
  -H "Content-Type: application/json" \
  -d '{
    "admins": {
      "names": ["admin"],
      "roles": ["_admin"]
    },
    "members": {
      "names": ["user1", "user2"],
      "roles": ["developers"]
    }
  }'

# Read current security settings
curl http://localhost:5984/mydb/_security
```

### 2. Create Users with Roles

```bash
# Create admin user
curl -X PUT http://localhost:5984/_users/org.couchdb.user:admin \
  -H "Content-Type: application/json" \
  -d '{
    "name": "admin",
    "password": "secure_password",
    "roles": ["_admin"],
    "type": "user"
  }'

# Create regular user
curl -X PUT http://localhost:5984/_users/org.couchdb.user:user1 \
  -H "Content-Type: application/json" \
  -d '{
    "name": "user1",
    "password": "user_password",
    "roles": ["developers"],
    "type": "user"
  }'
```

### 3. Configure CORS for Browser Access

```ini
; In local.ini
[httpd]
enable_cors = true

[cors]
origins = https://example.com,http://localhost:3000
methods = GET, PUT, POST, HEAD, DELETE
headers = accept, authorization, content-type, origin, referer
credentials = true
max_age = 3600
```

```bash
# Test CORS preflight
curl -X OPTIONS http://localhost:5984/mydb \
  -H "Origin: https://example.com" \
  -H "Access-Control-Request-Method: GET"
```

### 4. Restrict Design Document Access

```javascript
// In your design document's validate_doc_update function
function(newDoc, oldDoc, userCtx) {
  // Only admins can modify design documents
  if (newDoc._id.startsWith('_design/') && userCtx.roles.indexOf('_admin') === -1) {
    throw({forbidden: 'Only admins can modify design documents'});
  }

  // Users can only update their own documents
  if (oldDoc && oldDoc.owner !== userCtx.name) {
    throw({forbidden: 'You can only update your own documents'});
  }
}
```

## Common Scenarios

- **CORS blocks browser requests**: Add the frontend origin to the `origins` list in `local.ini`.
- **Design document update blocked**: Add `_admin` role to the user or modify `validate_doc_update`.
- **Cross-node access fails**: Configure inter-node authentication in clustered setup.

## Prevent It

- Use the principle of least privilege for user roles
- Enable CORS only for trusted origins
- Audit security settings regularly with `_security` endpoint

## Related Pages

- [CouchDB Auth Error](/tools/couchdb/couchdb-auth-error)
- [CouchDB CORS Error](/tools/couchdb/couchdb-cors-error)
- [CouchDB SSL Error](/tools/couchdb/couchdb-ssl-error)
