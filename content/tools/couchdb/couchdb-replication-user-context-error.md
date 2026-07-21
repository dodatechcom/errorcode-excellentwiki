---
title: "[Solution] CouchDB Replication User Context Error — How to Fix"
description: "Fix CouchDB replication user context errors by resolving userCtx issues in replication, fixing authentication context problems, and handling permission errors"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Replication User Context Error

CouchDB replication user context errors occur when replication fails due to incorrect or missing user context (userCtx) during authentication.

## Why It Happens

- Replication user does not exist
- User does not have sufficient permissions
- UserCtx is not properly configured
- Session expired during replication
- Admin credentials are required but missing
- User password changed during replication

## Common Error Messages

```
{ "error": "unauthorized", "reason": "User not found" }
```

```
{ "error": "forbidden", "reason": "Insufficient permissions" }
```

```
{ "error": "unauthorized", "reason": "Authentication required" }
```

```
{ "error": "forbidden", "reason": "Admin access required" }
```

## How to Fix It

### 1. Check User Context

```bash
# Check current user context
curl http://localhost:5984/_session | jq '.userCtx'

# Check if user exists
curl http://localhost:5984/_users/org.couchdb.user:replicator
```

### 2. Fix User Permissions

```bash
# Create replicator user
curl -X PUT http://localhost:5984/_users/org.couchdb.user:replicator \
  -H "Content-Type: application/json" \
  -d '{
    "name": "replicator",
    "password": "secret",
    "roles": [],
    "type": "user"
  }'

# Grant database admin role
curl -X PUT http://localhost:5984/_node/_local/_security \
  -H "Content-Type: application/json" \
  -d '{
    "admins": {
      "names": ["replicator"],
      "roles": []
    },
    "readers": {
      "names": [],
      "roles": []
    }
  }'
```

### 3. Configure Replication with Auth

```bash
# Use inline authentication
curl -X PUT http://localhost:5984/_replicator/my_rep \
  -H "Content-Type: application/json" \
  -d '{
    "_id": "my_rep",
    "source": {
      "url": "http://source:5984/db",
      "auth": {
        "basic": {
          "username": "replicator",
          "password": "secret"
        }
      }
    },
    "target": {
      "url": "http://target:5984/db",
      "auth": {
        "basic": {
          "username": "replicator",
          "password": "secret"
        }
      }
    }
  }'
```

### 4. Use Session Authentication

```bash
# Login and use session cookie
curl -X POST http://localhost:5984/_session \
  -H "Content-Type: application/json" \
  -d '{"name": "replicator", "password": "secret"}' \
  -c cookies.txt

# Use session in replication
curl -b cookies.txt -X PUT http://localhost:5984/_replicator/my_rep \
  -H "Content-Type: application/json" \
  -d '{
    "_id": "my_rep",
    "source": "http://source:5984/db",
    "target": "http://target:5984/db"
  }'
```

## Common Scenarios

- **User not found**: Create the replicator user.
- **Insufficient permissions**: Grant admin role to replicator user.
- **Auth expired**: Re-authenticate and restart replication.

## Prevent It

- Use dedicated replicator user with appropriate permissions
- Store credentials securely
- Monitor authentication status

## Related Pages

- [CouchDB Replication Error](/tools/couchdb/couchdb-replication-error)
- [CouchDB Auth Error](/tools/couchdb/couchdb-auth-error)
- [CouchDB Permission Error](/tools/couchdb/couchdb-permission-error)
