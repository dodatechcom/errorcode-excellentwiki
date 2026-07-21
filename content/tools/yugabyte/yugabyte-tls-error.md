---
title: "[Solution] YugabyteDB TLS Error — How to Fix"
description: "Fix YugabyteDB TLS errors by resolving certificate validation failures, fixing SSL configuration, and handling encrypted connection issues"
tools: ["yugabyte"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# YugabyteDB TLS Error

YugabyteDB TLS errors occur when encrypted connections fail due to certificate issues, expired certificates, or misconfigured SSL/TLS settings between nodes or clients.

## Why It Happens

- TLS certificates have expired
- Certificate common name does not match hostname
- Client does not trust the server certificate CA
- TLS version is not supported by the client
- Certificate file permissions prevent reading
- Node-to-node TLS is not configured consistently

## Common Error Messages

```
ERROR: SSL connection error: certificate verify failed
```

```
FATAL: certificate has expired
```

```
ERROR: no pg_hba.conf entry for SSL connection
```

```
ERROR: unsupported TLS version
```

## How to Fix It

### 1. Generate New Certificates

```bash
# Generate CA key and certificate
openssl genrsa -out ca.key 2048
openssl req -x509 -new -nodes -key ca.key -sha256 -days 3650 \
  -out ca.crt -subj "/CN=YugabyteDB CA"

# Generate server certificate
openssl genrsa -out server.key 2048
openssl req -new -key server.key -out server.csr \
  -subj "/CN=yugabyte"
openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key \
  -CAcreateserial -out server.crt -days 365 -sha256
```

### 2. Configure TLS on YugabyteDB

```bash
# Place certificates in YugabyteDB directory
cp ca.crt server.crt server.key /opt/yugabyte/certs/

# Configure master TLS
--certs_dir_name=/opt/yugabyte/certs
--use_node_to_node_encryption=true
--use_client_to_server_encryption=true
```

### 3. Fix Client TLS Configuration

```python
# Python psycopg2 with TLS
import psycopg2

conn = psycopg2.connect(
    host='yugabyte',
    port=5433,
    dbname='mydb',
    user='yugabyte',
    password='password',
    sslmode='verify-full',
    sslrootcert='/opt/yugabyte/certs/ca.crt',
    sslcert='/opt/yugabyte/certs/client.crt',
    sslkey='/opt/yugabyte/certs/client.key'
)
```

### 4. Verify Certificate Chain

```bash
# Verify certificate
openssl verify -CAfile ca.crt server.crt

# Check certificate expiry
openssl x509 -in server.crt -noout -dates

# Test TLS connection
openssl s_client -connect yugabyte:5433 \
  -CAfile ca.crt -cert client.crt -key client.key
```

## Common Scenarios

- **Certificate expired**: Regenerate certificates and restart YugabyteDB.
- **Hostname mismatch**: Ensure the certificate CN or SAN matches the hostname.
- **Client cannot verify server**: Provide the CA certificate to the client.

## Prevent It

- Monitor certificate expiry dates
- Use automated certificate rotation
- Test TLS configuration before deploying

## Related Pages

- [YugabyteDB SSL Error](/tools/yugabyte/yugabyte-ssl-error)
- [YugabyteDB Connection Error](/tools/yugabyte/yugabyte-connection-error)
- [YugabyteDB Auth Error](/tools/yugabyte/yugabyte-auth-error)
