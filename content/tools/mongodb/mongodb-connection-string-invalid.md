---
title: "[Solution] MongoDB Connection String Invalid Format Error"
description: "Fix MongoDB connection string invalid format error when the URI cannot be parsed due to malformed syntax"
tools: ["mongodb"]
error-types: ["tool-error"]
severities: ["error"]
---

# MongoDB Connection String Invalid Format Error

The MongoDB driver rejects the connection string because it does not conform to the standard MongoDB URI format. Parsing fails at a specific character or section.

## Common Causes

- Special characters in password not URL-encoded
- Missing or extra characters in the connection string
- Incorrect scheme (e.g., "mongodb" vs "mongodb+srv")
- Port number is not a valid integer
- Options contain invalid key-value pairs
- IPv6 address not enclosed in brackets

## How to Fix

### URL-Encode Special Characters

```javascript
// Password with special characters must be encoded
// Raw: p@ss:w0rd!
// Encoded: p%40ss%3Aw0rd!

const uri = 'mongodb://admin:p%40ss%3Aw0rd!@mongo1:27017/mydb?authSource=admin';
```

### Use Standard Connection String Format

```javascript
// Standard format
'mongodb://host1:27017,host2:27017/mydb?replicaSet=rs0'

// SRV format
'mongodb+srv://cluster0.example.mongodb.net/mydb'

// With authentication
'mongodb://user:password@host:27017/mydb?authSource=admin'
```

### Handle IPv6 Addresses

```javascript
// IPv6 must be in brackets
'mongodb://[::1]:27017/mydb'
'mongodb://[2001:db8::1]:27017/mydb'
```

### Validate Connection String

```javascript
const { URL } = require('url');

function validateMongoURI(uri) {
  try {
    const parsed = new URL(uri);
    if (!['mongodb:', 'mongodb+srv:'].includes(parsed.protocol)) {
      throw new Error('Invalid protocol: ' + parsed.protocol);
    }
    console.log('Valid URI');
    console.log('Host:', parsed.hostname);
    console.log('Port:', parsed.port || 'default');
    console.log('Database:', parsed.pathname.slice(1));
  } catch (err) {
    console.error('Invalid MongoDB URI:', err.message);
  }
}

validateMongoURI('mongodb://admin:pass@mongo:27017/mydb');
```

## Examples

```
MongoParseError: password contains an illegal unescaped character

MongoParseError: Invalid connection string:
  "mongodb://host:abc/mydb" -- port must be a number

MongoParseError: Invalid hostname "host:27017:extra"
  -- too many colons in authority
```

## Related Errors

- [MongoDB Connection Error]({{< relref "/tools/mongodb/mongodb-connection-error" >}}) -- connection issues
- [MongoDB DNS Resolution Failed]({{< relref "/tools/mongodb/mongodb-dns-resolution-failed" >}}) -- DNS issues
- [MongoDB Connection Refused]({{< relref "/tools/mongodb/mongodb-connection-refused" >}}) -- connection refused
