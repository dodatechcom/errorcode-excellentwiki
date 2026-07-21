---
title: "[Solution] CouchDB Replication Auth Error — How to Fix"
description: "Fix CouchDB replication auth errors by resolving authentication failures during replication, fixing credential issues, and handling auth configuration problems"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Replication Auth Error

CouchDB replication auth errors occur when authentication fails between source and target databases during replication.

## Why It Happens

- Credentials are incorrect
- User does not exist
- User password has changed
- Authentication method is not supported
- SSL certificate is invalid
- Session has expired

## Common Error Messages

```
{ "error": "unauthorized", "reason": "Authentication failed" }
```

```
{ "error": "unauthorized", "reason": "Invalid credentials" }
```

```
{ "error": "unauthorized", "reason": "User not found" }
```

```
{ "error": "unauthorized", "reason": "Password incorrect" }
```

## How to Fix It

### 1. Test Authentication

```bash
# Test source authentication
curl -u user:pass http://source:5984/_session

# Test target authentication
curl -u user:pass http://target:5984/_session

# Check user exists
curl -u admin:admin http://source:5984/_users/org.couchdb.user:replicator
```

### 2. Fix Credentials

```bash
# Create/update user
curl -X PUT http://source:5984/_users/org.couchdb.user:replicator \
  -H "Content-Type: application/json" \
  -d '{
    "name": "replicator",
    "password": "new_password",
    "roles": [],
    "type": "user"
  }'

# Use credentials in replication
curl -X PUT http://localhost:5984/_replicator/my_rep \
  -H "Content-Type: application/json" \
  -d '{
    "_id": "my_rep",
    "source": {
      "url": "http://source:5984/db",
      "auth": {
        "basic": {
          "username": "replicator",
          "password": "new_password"
        }
      }
    },
    "target": "http://target:5984/db"
  }'
```

### 3. Use Session Authentication

```bash
# Login to get session
curl -X POST http://source:5984/_session \
  -H "Content-Type: application/json" \
  -d '{"name": "replicator", "password": "new_password"}' \
  -c cookies.txt

# Use session cookie
curl -b cookies.txt http://source:5984/mydb
```

### 4. Configure Auth

```bash
# Check auth configuration
curl http://localhost:5984/_node/_local/_config/httpd | jq '.authentication'

# Enable basic auth
curl -X PUT http://localhost:5984/_node/_local/_config/httpd/authentication \
  -H "Content-Type: text/plain" \
  -d '"basic"'
```

## Common Scenarios

- **Auth failed**: Verify credentials and user exists.
- **User not found**: Create the replication user.
- **Password changed**: Update password in replication document.

## Prevent It

- Store credentials securely
- Use dedicated replication users
- Monitor authentication status

## Related Pages

- [CouchDB Replication Error](/tools/couchdb/couchdb-replication-error)
- [CouchDB Auth Error](/tools/couchdb/couchdb-auth-error)
- [CouchDB Password Error](/tools/couchdb/couchdb-password-error)
