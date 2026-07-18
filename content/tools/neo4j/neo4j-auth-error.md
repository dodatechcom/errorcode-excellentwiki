---
title: "[Solution] Neo4j Authentication Error — How to Fix"
description: "Fix Neo4j authentication errors including password issues, role-based access control, and LDAP/Kerberos integration problems"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Authentication Error

Authentication errors in Neo4j occur when users cannot log in due to incorrect credentials, expired passwords, misconfigured authentication providers, or role-based access control issues.

## Why It Happens

- The username or password is incorrect
- The default password has not been changed
- LDAP or Kerberos configuration is wrong
- The user's role lacks required permissions
- The authentication provider is unreachable
- The password policy has expired the user's password
- Multiple authentication providers are configured incorrectly

## Common Error Messages

```
Neo.ClientError.Security.Unauthorized: The client is unauthorized due to authentication failure
```

```
Neo.ClientError.Security.Unauthorized: Invalid username or password
```

```
Neo.ClientError.Security.AuthProviderUnavailable:
LDAP server is unavailable
```

```
Neo.ClientError.Security.Forbidden: User 'neo4j' does not have privilege 'WRITE'
```

## How to Fix It

### 1. Reset Neo4j Password

```bash
# Stop Neo4j
sudo systemctl stop neo4j

# Reset password
neo4j-admin dbms set-initial-password newpassword

# Start Neo4j
sudo systemctl start neo4j
```

### 2. Fix Role-Based Access Control

```cypher
// Show all roles and users
SHOW ROLES;
SHOW USERS;

// Grant a role to a user
GRANT ROLE readWrite TO 'myuser';

// Create a custom role
CREATE ROLE dataEngineer;
GRANT READ (*) TO dataEngineer;
GRANT WRITE (*) TO dataEngineer;
GRANT ROLE dataEngineer TO 'engineer1';
```

### 3. Fix LDAP Configuration

```bash
# In neo4j.conf
dbms.security.ldap.enabled=true
dbms.security.ldap.host=ldap.example.com
dbms.security.ldap.port=389
dbms.security.ldap.user_dn_template=cn={0},ou=users,dc=example,dc=com
dbms.security.ldap.authorization.enabled=true
```

### 4. Fix Authentication Provider Issues

```bash
# Check Neo4j logs for auth errors
tail -f /var/log/neo4j/neo4j.log | grep -i auth

# Verify LDAP connectivity
ldapsearch -x -H ldap://ldap.example.com -b "ou=users,dc=example,dc=com" "(cn=myuser)"
```

## Common Scenarios

- **Fresh install with default password**: Change the default password immediately after first login.
- **LDAP server unreachable**: Check network connectivity and LDAP server status.
- **User lacks write permission**: Grant the appropriate role with `GRANT ROLE readWrite TO user`.

## Prevent It

- Change the default Neo4j password on first deployment
- Use role-based access control with least-privilege principles
- Monitor authentication failures in the audit log

## Related Pages

- [Neo4j Connection Error](/tools/neo4j/neo4j-connection-error)
- [Neo4j User Error](/tools/neo4j/neo4j-user-error)
- [Neo4j Bolt Error](/tools/neo4j/neo4j-bolt-error)
