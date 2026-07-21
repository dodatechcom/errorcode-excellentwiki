---
title: "[Solution] CouchDB Password Error — How to Fix"
description: "Fix CouchDB password errors by resolving authentication failures, fixing password hash issues, and handling credential management problems"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Password Error

CouchDB password errors occur when password authentication fails due to incorrect credentials, hash mismatches, or configuration issues.

## Why It Happens

- Password hash in local.ini is incorrect
- User was created with wrong password
- Password hash algorithm changed between versions
- Admin password was reset but not updated in all places
- Password contains special characters that are not escaped
- Cookie session has expired

## Common Error Messages

```
{ "error": "unauthorized", "reason": "Name or password is incorrect." }
```

```
{ "error": "forbidden", "reason": "You are not a server admin." }
```

```
{ "error": "bad_request", "reason": "Invalid password format" }
```

```
{ "error": "unauthorized", "reason": "Session expired" }
```

## How to Fix It

### 1. Reset Admin Password

```bash
# Edit local.ini and remove the admin line
sudo vim /opt/couchdb/etc/local.ini
# Remove: admin = -hashed_password

# Restart CouchDB
sudo systemctl restart couchdb

# Create new admin
curl -X PUT http://localhost:5984/_users/org.couchdb.user:admin \
  -H "Content-Type: application/json" \
  -d '{"name": "admin", "password": "new_secret", "roles": [], "type": "user"}'
```

### 2. Fix User Password

```bash
# Update user password
curl -X PUT http://localhost:5984/_users/org.couchdb.user:appuser \
  -H "Content-Type: application/json" \
  -H "If-Match: 1-abc123" \
  -d '{
    "name": "appuser",
    "password": "new_password",
    "roles": [],
    "type": "user"
  }'
```

### 3. Check Authentication

```bash
# Test authentication
curl -u admin:password http://localhost:5984/_session

# Check user document
curl -u admin:password http://localhost:5984/_users/org.couchdb.user:admin
```

### 4. Fix Cookie Authentication

```bash
# Login to get session cookie
curl -X POST http://localhost:5984/_session \
  -H "Content-Type: application/json" \
  -d '{"name": "admin", "password": "secret"}' \
  -c cookies.txt

# Use session cookie
curl -b cookies.txt http://localhost:5984/_all_dbs
```

## Common Scenarios

- **Password not working**: Reset the password by editing local.ini.
- **User cannot authenticate**: Ensure the user document has the correct password.
- **Session expired**: Re-authenticate to get a new session cookie.

## Prevent It

- Use strong passwords for admin accounts
- Store credentials securely
- Implement proper session management

## Related Pages

- [CouchDB Auth Error](/tools/couchdb/couchdb-auth-error)
- [CouchDB Security Error](/tools/couchdb/couchdb-security-error)
- [CouchDB Admin Error](/tools/couchdb/couchdb-admin-error)
