---
title: "[Solution] Cassandra Authentication Error — How to Fix"
description: "Fix Cassandra authentication errors by configuring credentials, enabling SASL providers, fixing role permissions, and resolving certificate-based auth issues."
tools: ["cassandra"]
error-types: ["authentication-error"]
severities: ["error"]
weight: 5
comments: true
---

A Cassandra authentication error occurs when a client cannot prove its identity to the cluster. Cassandra supports multiple authentication mechanisms, and misconfiguration at any layer — network, protocol, or authorization — will block access.

## Why It Happens

Authentication errors in Cassandra can involve credentials, SASL negotiation, TLS certificates, or role-based access control. The root cause depends on which authentication method is configured.

- The client provides incorrect username or password
- PasswordAuthenticator is not enabled in cassandra.yaml
- The client driver uses a different SASL mechanism than the server expects
- TLS client certificates are missing, expired, or not signed by the expected CA
- The authenticated role does not have permission on the target keyspace or table
- JMX authentication is configured separately and blocking the connection
- The role was created with LOGIN = false, preventing connection

## Common Error Messages

```text
AuthenticationException: Username and/or password are incorrect
```

The credentials are wrong or authentication is not enabled on the server. This is the most common authentication error.

```text
SaslException: No compatible SASL mechanism found
```

The client and server disagree on which SASL mechanism to use. Common when one side expects Kerberos but the other expects password auth.

```text
UnauthorizedException: User cassandra has no permission on CREATE KEYSPACE
```

The user authenticated successfully but lacks the authorization to perform the requested operation.

```text
SSLHandshakeException: Received fatal alert: certificate_unknown
```

The server rejected the client's TLS certificate. This is a certificate-based authentication failure.

## How to Fix It

### 1. Enable and Configure Password Authentication

```yaml
# cassandra.yaml
authenticator: PasswordAuthenticator
authorizer: CassandraAuthorizer
role_manager: CassandraRoleManager
```

```bash
# After enabling authentication, restart all nodes sequentially
nodetool drain
sudo systemctl restart cassandra

# Default credentials are cassandra/cassandra — change immediately
cqlsh -u cassandra -p cassandra
ALTER ROLE cassandra WITH PASSWORD = 'new_secure_password';
```

### 2. Create and Configure Roles

```cql
-- Create a new application role
CREATE ROLE app_user WITH PASSWORD = 'secure_password' AND LOGIN = true;

-- Grant keyspace access
GRANT ALL ON KEYSPACE my_keyspace TO app_user;

-- Grant table-level permissions
GRANT SELECT, INSERT, UPDATE ON TABLE my_keyspace.users TO app_user;

-- Revoke permissions
REVOKE DROP ON KEYSPACE my_keyspace FROM app_user;

-- Check existing permissions
LIST ALL PERMISSIONS OF app_user;
```

```cql
-- Verify the role exists and has LOGIN = true
SELECT rolename, super, can_login, salted_hash
FROM system_auth.roles
WHERE rolename = 'app_user';
```

### 3. Configure Client Driver Authentication

```java
// Java driver with password auth
CqlSession session = CqlSession.builder()
    .addContactPoint(new InetSocketAddress("10.0.1.1", 9042))
    .withLocalDatacenter("datacenter1")
    .withAuthCredentials("app_user", "secure_password")
    .build();
```

```python
# Python driver with password auth
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

auth = PlainTextAuthProvider(username='app_user', password='secure_password')
cluster = Cluster(['10.0.1.1'], port=9042, auth_provider=auth)
session = cluster.connect('my_keyspace')
```

```bash
# cqlsh with credentials file
echo "username: app_user
password: secure_password" > ~/.cqlshrc

cqlsh --credentials ~/.cqlshrc
```

### 4. Configure Kerberos Authentication

```yaml
# cassandra.yaml
authenticator: AllowAllAuthenticator  # Temporary during setup
# or
authenticator: PasswordAuthenticator

# For Kerberos, use a custom SASL authenticator
```

```properties
# cassandra-env.sh
-Dcassandra.jmx.local.password-file=/etc/cassandra/jmxremote.password
-Dcassandra.jmx.local.access-file=/etc/cassandra/jmxremote.access
```

```bash
# Test Kerberos ticket
kinit -kt /etc/cassandra/cassandra.keytab cassandra/cassandra-host@REALM.COM

# Verify ticket
klist
```

## Common Scenarios

**Authentication fails after enabling PasswordAuthenticator.** Existing clients will lose connection. Enable authentication on one node at a time, update all client drivers with credentials, then enable on the remaining nodes. Alternatively, do a coordinated restart of all nodes and clients simultaneously.

**Roles created via CQL cannot login.** Ensure `LOGIN = true` is set when creating the role. Roles created with `LOGIN = false` can be granted permissions but cannot authenticate.

**TLS client certificate auth fails.** Ensure the client certificate is signed by a CA that the server trusts. Check certificate expiry with `openssl x509 -in client.crt -noout -dates` and verify the CA chain with `openssl verify -CAfile ca.crt client.crt`.

## Prevent It

- Change the default `cassandra/cassandra` credentials immediately after enabling authentication and never use them in production
- Use least-privilege roles — grant only the specific permissions each application needs on the tables it accesses
- Rotate passwords and certificates on a regular schedule, and automate credential distribution through a secrets manager like Vault
