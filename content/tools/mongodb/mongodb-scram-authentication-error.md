---
title: "[Solution] MongoDB SCRAM Authentication Error"
description: "Fix MongoDB SCRAM authentication mechanism errors"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB SCRAM Authentication Error

```
MongoServerError: SCRAM authentication failed
```

```
MongoServerError: Authentication failed. SCRAM conversation invalid
```

## Common Causes

- Password was changed between authentication attempts
- The SCRAM mechanism version mismatch
- The salt or iteration count in the stored credentials is corrupt
- Client and server support different SCRAM versions

## How to Fix

### 1. Specify the authentication mechanism explicitly

```
mongodb://user:password@localhost:27017/mydb?authMechanism=SCRAM-SHA-256
```

### 2. Reset the user credentials

```javascript
use admin
db.changeUserPassword("myuser", "newSecurePassword!")
```

### 3. Drop and recreate the user

```javascript
use admin
db.dropUser("myuser")
db.createUser({
  user: "myuser",
  pwd: "newPassword!",
  roles: [{ role: "readWrite", db: "mydb" }],
  mechanisms: ["SCRAM-SHA-256"]  // Specify mechanism
});
```

### 4. Check server authentication settings

```yaml
# /etc/mongod.conf
security:
  authorization: enabled
  authenticationMechanisms: SCRAM-SHA-256
```

## Examples

```bash
# Test SCRAM-SHA-256 authentication
mongosh --authenticationMechanism SCRAM-SHA-256 \
  --username myuser --password mypassword \
  --authenticationDatabase admin

# Check stored credentials
mongosh --eval "use admin; db.system.users.findOne({user:'myuser'})"

# Change password
mongosh --eval "use admin; db.changeUserPassword('myuser', 'newPass123!')"
```