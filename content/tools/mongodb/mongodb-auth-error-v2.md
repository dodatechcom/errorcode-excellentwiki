---
title: "MongoDB - SCRAM authentication failed"
description: "MongoDB client fails SCRAM authentication when credentials are incorrect or authentication mechanism is misconfigured"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

A SCRAM authentication failed error occurs when the MongoDB client cannot authenticate with the server using the SCRAM (Salted Challenge Response Authentication Mechanism). This is triggered by incorrect credentials, wrong auth database, or mechanism mismatch.

## Common Causes

- Incorrect username or password in connection string
- Wrong `authSource` database specified
- User created in a different database than expected
- SCRAM-SHA-256 vs SCRAM-SHA-1 mismatch
- Special characters in password not URL-encoded

## How to Fix

1. Verify credentials and authSource in the connection string:

```javascript
// Correct format with authSource
const uri = 'mongodb://username:password@localhost:27017/mydb?authSource=admin';
const client = new MongoClient(uri);
await client.connect();
```

2. URL-encode special characters in password:

```javascript
// If password is: p@ss!w0rd
const encodedPassword = encodeURIComponent('p@ss!w0rd');
const uri = `mongodb://user:${encodedPassword}@localhost:27017/mydb?authSource=admin`;
```

3. Verify user exists in the correct database:

```javascript
// Connect as admin and check
use admin
db.system.users.find({ user: "myuser" })
```

4. Create or update the user with correct auth source:

```javascript
use admin
db.createUser({
  user: "myuser",
  pwd: "mypassword",
  roles: [{ role: "readWrite", db: "mydb" }]
})
```

5. Check the authentication mechanism:

```javascript
// Force SCRAM-SHA-256
const client = new MongoClient(uri, {
  authMechanism: 'SCRAM-SHA-256',
  authSource: 'admin',
});
```

## Examples

```javascript
// Error: SCRAM authentication failed
const client = new MongoClient('mongodb://user:wrongpass@localhost:27017/mydb');
await client.connect();
// MongoServerError: SCRAM authentication failed

// Fix: correct password and authSource
const client = new MongoClient(
  'mongodb://user:correctpass@localhost:27017/mydb?authSource=admin'
);
```

## Related Errors

- [Connection error]({{< relref "/tools/mongodb/mongodb-connection-error" >}})
- [Write error]({{< relref "/tools/mongodb/mongodb-write-error" >}})
