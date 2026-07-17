---
title: "[Solution] Cassandra Authentication Failed - Fix Credentials and Roles"
description: "Fix Cassandra authentication errors by verifying role names and passwords, granting LOGIN permissions to roles, and configuring the correct authentication provi"
tools: ["cassandra"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

A Cassandra authentication error occurs when the client driver cannot authenticate with the Cassandra cluster. The server rejects the connection with an `UnauthorizedException` or `AuthenticationException` after the driver sends credentials.

## What This Error Means

Cassandra supports several authentication providers (e.g., `PasswordAuthenticator`, `AllowAllAuthenticator`). When authentication is enabled, the driver must provide valid username and password credentials during the CQL native protocol handshake. If the credentials are incorrect or the role does not exist, the server returns an authentication error.

The error message typically states `Username and/or password are incorrect` or `User has no DESCRIBE permission`.

## Why It Happens

- Incorrect username or password in the connection configuration
- The Cassandra role was created with a different case (Cassandra roles are case-sensitive)
- `AllowAllAuthenticator` was replaced with `PasswordAuthenticator` and existing drivers were not updated
- Role was granted to a different keyspace scope
- Password changed in Cassandra but not updated in the application
- SASL authentication mechanism mismatch between driver and server
- The role does not have `LOGIN` permission

## How to Fix It

### 1. Verify the Role Exists

```cql
SELECT rolename, super, datacenter, login FROM system_auth.roles;
```

### 2. Create or Update the Role

```cql
CREATE ROLE app_user WITH PASSWORD = 'secure_password' AND LOGIN = true AND SUPERUSER = false;
GRANT ALL PERMISSIONS ON KEYSPACE my_keyspace TO app_user;
```

### 3. Reset a Password

```cql
ALTER ROLE app_user WITH PASSWORD = 'new_secure_password';
```

### 4. Configure the Driver

```java
CqlSession session = CqlSession.builder()
    .addContactPoint(new InetSocketAddress("10.0.1.5", 9042))
    .withLocalDatacenter("datacenter1")
    .withAuthCredentials("app_user", "secure_password")
    .build();
```

```python
from cassandra.cluster import Cluster
cluster = Cluster(
    ['10.0.1.5'],
    auth_provider=PlainTextAuthProvider('app_user', 'secure_password')
)
session = cluster.connect()
```

### 5. Check Authentication Provider

```yaml
# cassandra.yaml
authenticator: org.apache.cassandra.auth.PasswordAuthenticator
authorizer: org.apache.cassandra.auth.CassandraAuthorizer
role_manager: org.apache.cassandra.auth.CassandraRoleManager
```

### 6. Use AllowAllAuthenticator for Development Only

```yaml
# cassandra.yaml - development only
authenticator: org.apache.cassandra.auth.AllowAllAuthenticator
```

## Common Mistakes

- Copying roles between environments without updating passwords
- Using `GRANT` without first granting `LOGIN` to the role
- Forgetting that roles are case-sensitive in Cassandra
- Not restarting or reconnecting the driver after changing authentication settings
- Mixing AllowAllAuthenticator in development with PasswordAuthenticator in production

## Related Pages

- [Cassandra Connection Error](/tools/cassandra/cassandra-connection-error)
- [Cassandra NoHostAvailableException](/tools/cassandra/cassandra-unavailable)
- [Cassandra Schema Error](/tools/cassandra/cassandra-schema-error)
