---
title: "[Solution] CouchDB Authentication Error — How to Fix"
description: "Fix CouchDB authentication errors by configuring admin users, setting up cookie sessions, and resolving LDAP plugin issues"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Authentication Error

CouchDB authentication errors occur when users cannot log in, sessions expire unexpectedly, or admin operations are blocked. CouchDB supports multiple authentication mechanisms.

## Why It Happens

- No admin user is configured (server is in "admin party" mode)
- Username or password is incorrect
- Session cookie has expired or is not being sent
- LDAP or proxy auth plugin misconfiguration
- `_users` database is missing or corrupted
- Admin password contains special characters that are not URL-encoded

## Common Error Messages

```
{ "error": "unauthorized", "reason": "You are not a server admin." }
```

```
{ "error": "unauthorized", "reason": "Name or password is incorrect." }
```

```
{ "error": "forbidden", "reason": "You must be an admin to perform this operation." }
```

```
{ "error": "bad_request", "reason": "invalid_auth" }
```

## How to Fix It

### 1. Create Admin User

```bash
# Create first admin user
curl -X PUT http://localhost:5984/_users/org.couchdb.user:admin \
  -H "Content-Type: application/json" \
  -d '{
    "name": "admin",
    "password": "securepassword",
    "roles": ["_admin"],
    "type": "user"
  }'

# Or use the setup wizard
curl -X POST http://localhost:5984/_cluster_setup \
  -H "Content-Type: application/json" \
  -d '{
    "action": "enable_single_node",
    "bind_address": "0.0.0.0",
    "username": "admin",
    "password": "securepassword"
  }'
```

### 2. Fix Cookie Authentication

```ini
; In local.ini
[httpd]
authentication_handler = couch_httpd_auth:authentication_handler
require_valid_user = true

[chttpd]
require_valid_user = true
```

```bash
# Get session cookie
curl -X POST http://localhost:5984/_session \
  -H "Content-Type: application/json" \
  -d '{"name": "admin", "password": "securepassword"}' \
  -c cookies.txt

# Use session cookie for subsequent requests
curl -b cookies.txt http://localhost:5984/_all_dbs
```

### 3. Configure JWT Authentication

```ini
; In local.ini
[httpd]
authentication_handler = couch_httpd_auth:jwt_authentication_handler

[chttpd_auth]
jwt_authentication_handler = couch_httpd_auth:jwt_authentication_handler
secret = your_jwt_secret_here
```

```bash
# Test JWT auth
curl -H "Authorization: Bearer <jwt_token>" \
  http://localhost:5984/_session
```

### 4. Fix Password Issues with Special Characters

```bash
# URL-encode special characters in passwords
# Password: p@ss#word!123
# Encoded: p%40ss%23word%21123

curl -u "admin:p%40ss%23word%21123" http://localhost:5984/_all_dbs

# Or use --digest authentication
curl --digest -u admin:password http://localhost:5984/_all_dbs
```

## Common Scenarios

- **Fresh install allows any admin operation**: Create an admin user immediately after setup.
- **Session expires during long operations**: Increase session timeout or use API tokens.
- **Proxy auth returns wrong user**: Configure `X-Auth-CouchDB-UserName` header correctly.

## Prevent It

- Always set up authentication before exposing CouchDB to the network
- Use strong passwords and rotate them regularly
- Monitor failed login attempts in the CouchDB log

## Related Pages

- [CouchDB Security Error](/tools/couchdb/couchdb-security-error)
- [CouchDB SSL Error](/tools/couchdb/couchdb-ssl-error)
- [CouchDB Connection Error](/tools/couchdb/couchdb-connection-error)
