---
title: "[Solution] ScyllaDB Authentication Error — How to Fix"
description: "Fix ScyllaDB authentication errors by configuring PasswordAuthenticator, fixing role permissions, and resolving SASL handshake failures"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB Authentication Error

ScyllaDB authentication errors occur when clients fail to authenticate or lack permissions for operations. ScyllaDB supports multiple authentication and authorization mechanisms.

## Why It Happens

- PasswordAuthenticator is enabled but client sends no credentials
- Username or password is incorrect
- Role does not have the required permissions
- SASL handshake fails between driver and server
- Authorization is enabled but role lacks GRANT permissions
- Client driver is not configured for authentication

## Common Error Messages

```
AuthenticationError: Error from server: code=0010 [Unauthorized] ... Username and/or password are incorrect
```

```
UnauthorizedError: Error from server: code=0010 [Unauthorized] ... User has no VALIDATE permission
```

```
AuthenticationError: Failed to authenticate
```

```
InvalidCredentials: Authenticator failed to login
```

## How to Fix It

### 1. Configure Authentication

```yaml
# In scylla.yaml
authenticator: PasswordAuthenticator
authorizer: CassandraAuthorizer
role_manager: CassandraRoleManager
```

```bash
# Restart ScyllaDB after auth changes
sudo systemctl restart scylla-server
```

### 2. Create and Configure Roles

```cql
-- Connect as default superuser (first node only)
cqlsh -u cassandra -p cassandra

-- Create a new role with password
CREATE ROLE admin WITH PASSWORD = 'secure_password' AND LOGIN = true AND SUPERUSER = true;

-- Create application role
CREATE ROLE app_user WITH PASSWORD = 'app_password' AND LOGIN = true;

-- Grant permissions
GRANT ALL ON KEYSPACE mykeyspace TO app_user;
GRANT SELECT ON KEYSPACE mykeyspace TO read_user;

-- Alter existing role password
ALTER ROLE cassandra WITH PASSWORD = 'new_password';
```

### 3. Configure Driver Authentication

```python
# Python driver
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

auth_provider = PlainTextAuthProvider(
    username='app_user',
    password='app_password'
)

cluster = Cluster(
    ['10.0.0.1'],
    auth_provider=auth_provider,
    protocol_version=4
)
session = cluster.connect('mykeyspace')
```

```java
// Java driver
CqlSession session = CqlSession.builder()
    .withLocalDatacenter("datacenter1")
    .withAuthCredentials("app_user", "app_password")
    .build();
```

### 4. Fix Permission Issues

```cql
-- Check current permissions
LIST ALL PERMISSIONS OF app_user;

-- Grant specific permissions
GRANT SELECT, INSERT, UPDATE ON TABLE mykeyspace.users TO app_user;
GRANT CREATE ON KEYSPACE mykeyspace TO app_user;

-- Revoke permissions
REVOKE ALL ON KEYSPACE mykeyspace FROM old_user;

-- Check role membership
LIST ROLES OF app_user;
```

## Common Scenarios

- **Fresh install requires auth**: Change from AllowAllAuthenticator to PasswordAuthenticator.
- **Driver connection fails after enabling auth**: Update driver config with auth provider.
- **Role cannot access table**: Grant specific table-level permissions.

## Prevent It

- Use role-based access control with least-privilege principle
- Rotate passwords regularly and use strong credentials
- Monitor authentication failures in ScyllaDB logs

## Related Pages

- [ScyllaDB Connection Error](/tools/scylladb/scylladb-connection-error)
- [ScyllaDB Schema Error](/tools/scylladb/scylladb-schema-error)
- [ScyllaDB SSL Error](/tools/scylladb/scylladb-ssl-error)
