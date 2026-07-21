---
title: "[Solution] Neo4j Auth Error"
description: "Fix Neo4j authentication errors when login credentials are invalid or expired"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Auth Error

Authentication errors occur when the client provides invalid credentials.

## Common Causes

- Wrong password for neo4j user
- Auth disabled but client sending credentials
- Custom auth plugin failing
- LDAP connection to auth provider down

## Common Error Messages

```
Neo.ClientError.Security.Unauthorized: The client is unauthorized
```

## How to Fix It

### 1. Reset Default Password

```bash
cypher-shell -u neo4j -p neo4j "ALTER CURRENT USER SET PASSWORD FROM 'neo4j' TO 'newpassword'"
```

### 2. Check Auth Configuration

```properties
# neo4j.conf
dbms.security.auth_enabled=true
```

### 3. Disable Auth Temporarily

```properties
# neo4j.conf
dbms.security.auth_enabled=false
```

## Examples

```bash
cypher-shell -u neo4j -p password "RETURN 1"
```
