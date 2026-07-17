---
title: "MongoDB Authentication Error"
description: "MongoDB client fails to authenticate with the database server."
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
tags: ["mongodb", "authentication", "password", "credential", "auth"]
weight: 5
---

# MongoDB Authentication Error

A MongoDB authentication error occurs when the client cannot authenticate with the database server. The credentials are incorrect or authentication is not properly configured.

## Common Causes

- Incorrect username or password
- Authentication database not specified
- User does not have required permissions
- SCRAM authentication mechanism mismatch

## How to Fix

### Verify Credentials

```bash
mongosh -u admin -p password --authenticationDatabase admin
```

### Check User Exists

```javascript
use admin
db.getUsers()
```

### Create User

```javascript
use mydb
db.createUser({
  user: "myuser",
  pwd: "mypassword",
  roles: [{ role: "readWrite", db: "mydb" }]
})
```

### Specify Auth Database in Connection String

```javascript
const uri = 'mongodb://user:pass@localhost:27017/mydb?authSource=admin';
```

### Enable Authentication

```yaml
# /etc/mongod.conf
security:
  authorization: enabled
```

## Examples

```javascript
// Wrong auth database
const client = new MongoClient('mongodb://user:pass@localhost:27017/mydb');
// Error: Authentication failed

// Fix: specify authSource
const client = new MongoClient('mongodb://user:pass@localhost:27017/mydb?authSource=admin');
```

## Related Errors

- [Connection Error]({{< relref "/tools/mongodb/mongodb-connection-error" >}}) — connection failure
- [Permission Error]({{< relref "/tools/mongodb/auth-error" >}}) — authorization error
