---
title: "[Solution] CouchDB Admin Error — How to Fix"
description: "Fix CouchDB admin errors by resolving admin account issues, fixing admin configuration, and handling administrative API access problems"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Admin Error

CouchDB admin errors occur when administrative operations fail due to missing admin accounts, incorrect configuration, or unauthorized API access.

## Why It Happens

- No admin user is configured in CouchDB
- Admin password is incorrect or expired
- Admin API endpoint is not accessible
- Single-node setup requires manual admin creation
- Cluster setup has inconsistent admin accounts
- Admin credentials are stored in wrong configuration file

## Common Error Messages

```
{ "error": "unauthorized", "reason": "You must be an admin to do this." }
```

```
{ "error": "not_found", "reason": "no admin account" }
```

```
{ "error": "forbidden", "reason": "Admin access required" }
```

```
{ "error": "bad_request", "reason": "Invalid admin credentials" }
```

## How to Fix It

### 1. Create Admin User

```bash
# Create first admin via CouchDB setup API
curl -X PUT http://localhost:5984/_users/org.couchdb.user:admin \
  -H "Content-Type: application/json" \
  -d '{"name": "admin", "password": "secret", "roles": [], "type": "user"}'

# Or use the setup endpoint
curl -X POST http://localhost:5984/_cluster_setup \
  -H "Content-Type: application/json" \
  -d '{
    "action": "enable_single_node",
    "bind_address": "0.0.0.0",
    "username": "admin",
    "password": "secret"
  }'
```

### 2. Fix Admin Configuration

```ini
; In local.ini
[admins]
admin = secret
; Passwords are hashed on first startup
```

```bash
# Restart CouchDB after config change
sudo systemctl restart couchdb
```

### 3. Reset Admin Password

```bash
# If locked out, edit local.ini directly
# Remove the admin line and restart
# Then create a new admin via API

# Edit local.ini
sudo vim /opt/couchdb/etc/local.ini

# Remove: admin = -hashed_password
# Restart
sudo systemctl restart couchdb

# Create new admin
curl -X PUT http://localhost:5984/_users/org.couchdb.user:admin \
  -H "Content-Type: application/json" \
  -d '{"name": "admin", "password": "new_secret", "roles": [], "type": "user"}'
```

### 4. Verify Admin Access

```bash
# Test admin access
curl -u admin:secret http://localhost:5984/_all_dbs

# Check admin status
curl -u admin:secret http://localhost:5984/_session
```

## Common Scenarios

- **Cannot create database**: No admin user configured; create one first.
- **Admin login fails**: Check local.ini for correct password hash.
- **Cluster admin mismatch**: Ensure all nodes have the same admin user.

## Prevent It

- Configure admin user during initial setup
- Store admin credentials securely
- Use session tokens instead of basic auth in production

## Related Pages

- [CouchDB Auth Error](/tools/couchdb/couchdb-auth-error)
- [CouchDB Security Error](/tools/couchdb/couchdb-security-error)
- [CouchDB Connection Error](/tools/couchdb/couchdb-connection-error)
