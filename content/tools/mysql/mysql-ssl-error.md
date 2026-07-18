---
title: "[Solution] MySQL SSL Connection Error - Fix TLS and Certificate Errors"
description: "Fix MySQL SSL connection errors by configuring TLS certificates, enabling SSL on the server, and matching client-server SSL settings properly"
tools: ["mysql"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

# MySQL SSL Connection Error

This error occurs when a client tries to connect to MySQL using SSL/TLS but the connection fails due to certificate issues, protocol mismatches, or configuration problems.

## What This Error Means

MySQL may report various SSL-related errors:

```
ERROR 2026 (HY000): SSL connection error: SSL_CTX_set_default_verify_paths failed
```

Or:

```
ERROR 2026 (HY000): SSL connection error: protocol version mismatch
```

Or from the client:

```
mysql: SSL connection error: certificate verify failed
```

These errors indicate that the TLS handshake between the client and server failed. MySQL supports SSL/TLS encryption for client-server connections, and both sides must agree on the protocol, certificates, and cipher suite.

## Why It Happens

- SSL is required on the server but the client does not have SSL configured
- The server certificate is expired, self-signed, or not trusted by the client
- The client certificate is not in the server's `ssl_ca` file
- The TLS protocol version does not match (client uses TLS 1.0, server requires TLS 1.2)
- The SSL certificate CN (Common Name) does not match the server hostname
- The `--ssl-mode` option on the client does not match the server's SSL requirements
- The SSL certificate files have wrong permissions or are missing

## How to Fix It

### 1. Check Server SSL Status

```sql
-- Check if SSL is enabled on the server
SHOW VARIABLES LIKE '%ssl%';

-- Check current connections' SSL status
SHOW STATUS LIKE 'Ssl_cipher';
```

### 2. Enable SSL on the Server

```bash
# In my.cnf
[mysqld]
ssl-ca = /etc/mysql/ssl/ca.pem
ssl-cert = /etc/mysql/ssl/server-cert.pem
ssl-key = /etc/mysql/ssl/server-key.pem
require_secure_transport = ON
```

### 3. Generate Self-Signed Certificates

```bash
# Generate CA key and certificate
openssl genrsa 2048 > ca-key.pem
openssl req -new -x509 -nodes -days 3650 -key ca-key.pem -out ca.pem \
    -subj "/CN=MySQL_CA"

# Generate server key and certificate
openssl req -newkey rsa:2048 -nodes -keyout server-key.pem \
    -out server-req.pem -subj "/CN=mysql-server"
openssl x509 -req -in server-req.pem -days 3650 \
    -CA ca.pem -CAkey ca-key.pem -set_serial 01 -out server-cert.pem
```

### 4. Configure Client SSL Mode

```bash
# Require SSL connection
mysql -u myuser -p --ssl-mode=REQUIRED -h mysql-server

# Verify the SSL connection
mysql -u myuser -p --ssl-mode=REQUIRED -h mysql-server -e "SHOW STATUS LIKE 'Ssl_cipher';"

# Accept SSL but don't require it
mysql -u myuser -p --ssl-mode=PREFERRED -h mysql-server
```

### 5. Skip SSL for Local Development

```bash
# Disable SSL for localhost connections
mysql -u root -p --skip-ssl

# Or in my.cnf
[client]
ssl-mode = DISABLED
```

### 6. Verify Certificate Permissions

```bash
# Certificate files must be readable by the mysql user
ls -la /etc/mysql/ssl/
sudo chown mysql:mysql /etc/mysql/ssl/*.pem
sudo chmod 600 /etc/mysql/ssl/server-key.pem
sudo chmod 644 /etc/mysql/ssl/*.pem
```

## Common Mistakes

- Using self-signed certificates in production without distributing the CA certificate to all clients
- Forgetting to update certificates before they expire
- Setting `require_secure_transport = ON` without first ensuring all clients have SSL configured
- Not checking that the certificate CN matches the hostname clients use to connect
- Mixing up `--ssl-mode=VERIFY_CA` and `--ssl-mode=VERIFY_IDENTITY` -- the latter also checks the CN

## Related Pages

- [MySQL Connection Refused](/tools/mysql/mysql-connection-refused)
- [MySQL Access Denied](/tools/mysql/mysql-access-denied)
- [MySQL User Limit](/tools/mysql/mysql-user-limit)
- [PostgreSQL Config Error](/tools/postgresql/pg-config-error)
