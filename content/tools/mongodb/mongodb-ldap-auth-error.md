---
title: "[Solution] MongoDB LDAP Auth Error"
description: "Fix MongoDB LDAP authentication errors"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB LDAP Auth Error

```
MongoServerError: sasl library error: -13
```

```
LDAP authentication failed
```

## Common Causes

- LDAP server is unreachable from the MongoDB server
- The bind DN or password is incorrect
- The LDAP search filter is misconfigured
- The user's LDAP group is not mapped to a MongoDB role
- TLS is required but not configured
- The SASL library is not installed on the MongoDB server

## How to Fix

### 1. Verify LDAP connectivity

```bash
ldapsearch -H ldap://ldap.example.com -D "cn=admin,dc=example,dc=com" -W -b "dc=example,dc=com"
```

### 2. Configure LDAP in mongod.conf

```yaml
security:
  authorization: enabled
  ldap:
    servers: "ldap.example.com"
    transportSecurity: tls
    timeoutMS: 5000
    userToDNMapping:
      - match: "(.+)"
        substitution: "cn={0},ou=users,dc=example,dc=com"
    authz:
      queryTemplate: "ou=groups,dc=example,dc=com??one?(member={0})"
```

### 3. Map LDAP groups to MongoDB roles

```javascript
use admin
db.createRole({
  role: "ldapReader",
  privileges: [],
  roles: ["read"]
});
```

### 4. Test LDAP authentication

```bash
mongosh --authenticationMechanism PLAIN \
  --username "cn=myuser,ou=users,dc=example,dc=com" \
  --password "ldapPassword" \
  --authenticationDatabase '$external'
```

## Examples

```bash
# Test LDAP bind
ldapsearch -H ldap://ldap.example.com \
  -D "cn=myuser,ou=users,dc=example,dc=com" \
  -W -b "ou=users,dc=example,dc=com" "(cn=myuser)"

# Check MongoDB LDAP configuration
mongosh --eval "db.adminCommand({getParameter:1, ldapServers:1})"
```