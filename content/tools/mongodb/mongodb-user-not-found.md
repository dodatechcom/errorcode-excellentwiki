---
title: "[Solution] MongoDB User Not Found Error"
description: "Fix MongoDB user not found errors during authentication"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB User Not Found Error

```
MongoServerError: User "myuser" not found
```

```
MongoServerError: auth failed, user not found
```

## Common Causes

- The username does not exist in the specified authSource database
- The user was created in a different database
- The authSource parameter is wrong
- The user was dropped

## How to Fix

### 1. Check which users exist

```javascript
use admin
db.getUsers()
```

### 2. Check a specific user

```javascript
use admin
db.getUser("myuser")
```

### 3. Verify the authSource in the connection string

```
mongodb://myuser:password@localhost:27017/mydb?authSource=admin
```

### 4. Create the user if it does not exist

```javascript
use admin
db.createUser({
  user: "myuser",
  pwd: "securePassword!",
  roles: [{ role: "readWrite", db: "mydb" }]
});
```

## Examples

```bash
# List all users in admin database
mongosh --eval "use admin; db.getUsers()"

# Check user in a specific database
mongosh --eval "use mydb; db.getUsers()"

# Verify user authentication
mongosh --username myuser --password securePassword! --authenticationDatabase admin
```