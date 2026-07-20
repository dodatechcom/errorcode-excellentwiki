---
title: "[Solution] MongoDB Authentication Failed"
description: "Fix MongoDB authentication failed error when connecting to the database server"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Authentication Failed Error

The `auth failed` error occurs when MongoDB rejects the credentials provided during connection. This typically appears as:

```
MongoServerError: Authentication failed.
```

or in older versions:

```
auth failed, username: myuser db: admin code: 18 AuthenticationFailed
```

## Common Causes

- Incorrect username or password
- The user does not exist in the authentication database
- The user does not have sufficient privileges
- `authSource` parameter is missing or incorrect in the connection string
- Password contains special characters that are not URL-encoded
- SCRAM-SHA-256 vs SCRAM-SHA-1 mismatch between client and server
- The user was created on a different database than the one specified in `authSource`
- Kerberos or LDAP token has expired
- MongoDB Atlas password contains characters that break the connection URI

## How to Fix

### 1. Verify the user exists

```javascript
use admin
db.getUsers()
// or for a specific user
db.getUser("myuser")
```

### 2. Check the authSource

The connection string must include the correct `authSource`:

```
mongodb://myuser:mypassword@localhost:27017/mydatabase?authSource=admin
```

If the user was created in `admin`, the `authSource` must be `admin`, not `mydatabase`.

### 3. Re-create the user with correct permissions

```javascript
use admin
db.createUser({
  user: "myuser",
  pwd: "securePassword123!",
  roles: [
    { role: "readWrite", db: "mydatabase" },
    { role: "dbAdmin", db: "mydatabase" }
  ]
})
```

### 4. URL-encode special characters in the password

If your password is `p@ss:word/123`, it must be encoded as:

```
mongodb://myuser:p%40ss%3Aword%2F123@localhost:27017/mydatabase?authSource=admin
```

### 5. Force SCRAM-SHA-256 authentication mechanism

```
mongodb://myuser:password@localhost:27017/mydatabase?authSource=admin&authMechanism=SCRAM-SHA-256
```

## Examples

```bash
# Test authentication from the command line
mongosh --username myuser --password mypassword --authenticationDatabase admin

# Verify with a direct connection
mongosh "mongodb://myuser:password@localhost:27017/admin"

# Check server logs for auth details
tail -f /var/log/mongodb/mongod.log | grep -i auth

# Drop and recreate the user
mongosh --eval '
  use admin;
  db.dropUser("myuser");
  db.createUser({
    user: "myuser",
    pwd: "newSecurePass!",
    roles: [{ role: "readWrite", db: "mydatabase" }]
  });
'
```