---
title: "MongoDB SCRAM authentication failed"
description: "MongoDB rejects a client connection because SCRAM-SHA authentication credentials are invalid or missing"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

This error occurs when a client tries to connect to a MongoDB instance that requires authentication, but the provided username or password is incorrect, or the user lacks the necessary privileges.

## Common Causes

- Incorrect username or password in the connection string
- User does not exist in the authentication database
- Authentication database mismatch (e.g. authenticating against `admin` when user is in `mydb`)
- Password was recently changed but the client still uses the old one

## How to Fix

1. Verify the connection string format:

```javascript
// mongodb://username:password@host:port/authSource?authSource=admin
const uri = "mongodb://admin:secret@localhost:27017/mydb?authSource=admin"
```

2. Check the user exists and has correct roles:

```javascript
use admin
db.getUsers({ showCustomData: true })
```

3. Create a user if it does not exist:

```javascript
use mydb
db.createUser({
  user: "appuser",
  pwd: "secretpass",
  roles: [{ role: "readWrite", db: "mydb" }]
})
```

4. Reset a password if credentials are stale:

```javascript
use admin
db.changeUserPassword("appuser", "newpassword")
```

## Examples

```javascript
const client = new MongoClient("mongodb://wronguser:wrongpass@localhost:27017/mydb?authSource=admin")
await client.connect()
// MongoServerError: SCRAM authentication failed
```

## Related Errors

- [Connection Refused](/tools/mongodb/connection-refused)
