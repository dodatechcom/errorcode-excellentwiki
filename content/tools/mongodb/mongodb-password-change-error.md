---
title: "[Solution] MongoDB Password Change Error"
description: "Fix MongoDB password change errors"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Password Change Error

```
MongoServerError: Could not update user
```

```
MongoServerError: password change failed
```

## Common Causes

- The old password is incorrect
- The user does not have permission to change passwords
- The new password does not meet the password validation policy
- The user was created with SCRAM-SHA-1 and the server requires SCRAM-SHA-256

## How to Fix

### 1. Change password using changeUserPassword

```javascript
use admin
db.changeUserPassword("myuser", "newSecurePassword123!")
```

### 2. Update user with new password and roles

```javascript
use admin
db.updateUser("myuser", {
  pwd: "newSecurePassword123!",
  roles: [{ role: "readWrite", db: "mydb" }]
});
```

### 3. Reset password as admin

```javascript
use admin
// Connect as admin user first
db.changeUserPassword("targetUser", "resetPassword!")
```

### 4. Check password validation policy

```javascript
db.adminCommand({ getParameter: 1, passwordDigestor: 1 })
```

## Examples

```bash
# Change password
mongosh --eval "use admin; db.changeUserPassword('myuser', 'newPass123!')"

# Verify user after password change
mongosh --eval "use admin; db.getUser('myuser')"

# Test new password
mongosh --username myuser --password newPass123! --authenticationDatabase admin \
  --eval "db.runCommand({connectionStatus:1})"
```