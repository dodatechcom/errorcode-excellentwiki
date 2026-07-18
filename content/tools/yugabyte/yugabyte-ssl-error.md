---
title: "[Solution] YugabyteDB SSL Error — How to Fix"
description: "Fix YugabyteDB SSL errors by configuring TLS certificates, resolving certificate validation failures, and fixing SSL connection issues"
tools: ["yugabyte"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# YugabyteDB SSL Error

YugabyteDB SSL errors occur when TLS/SSL connections fail due to certificate issues, misconfiguration, or protocol mismatches.

## Why It Happens

- SSL certificates are not configured
- Certificate has expired or is invalid
- Client does not trust the server certificate
- SSL is not enabled in YugabyteDB configuration
- Certificate CN does not match hostname
- Mutual TLS requires client certificate

## Common Error Messages

```
FATAL: connection requires SSL
```

```
ERROR: certificate verify failed
```

```
FATAL: no pg_hba.conf entry for SSL connection
```

```
ERROR: SSL connection error
```

## How to Fix It

### 1. Generate SSL Certificates

```bash
# Generate CA key and cert
openssl genrsa -out ca.key 2048
openssl req -x509 -new -key ca.key -out ca.crt -days 3650

# Generate server key and cert
openssl genrsa -out server.key 2048
openssl req -new -key server.key -out server.csr -subj "/CN=yb-tserver-1"
openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt -days 3650

# Generate client key and cert
openssl genrsa -out client.key 2048
openssl req -new -key client.key -out client.csr -subj "/CN=yugabyte"
openssl x509 -req -in client.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out client.crt -days 3650
```

### 2. Configure YugabyteDB for SSL

```bash
# In tserver.gflags:
--use_client_to_server_encryption=true
--certs_dir=/home/yugabyte/certs

# Copy certs to all nodes
scp ca.crt server.crt server.key yb-tserver-1:/home/yugabyte/certs/
```

### 3. Connect with SSL

```bash
# Connect with SSL
ysqlsh -h yb-tserver-1 -p 5433 -U yugabyte --ssl
  --sslcertfile=client.crt
  --sslkeyfile=client.key
  --sslrootcertfile=ca.crt
```

### 4. Configure pg_hba.conf for SSL

```bash
# In pg_hba.conf:
# hostssl all all 0.0.0.0/0 md5
# hostnossl all all 0.0.0.0/0 reject
```

## Common Scenarios

- **Connection requires SSL but client doesn't provide certs**: Generate and configure client certificates.
- **Certificate expired**: Regenerate certificates with longer validity.
- **Self-signed cert rejected**: Add CA cert to client trust store.

## Prevent It

- Use valid certificates from trusted CA in production
- Rotate certificates before expiration
- Configure pg_hba.conf to reject non-SSL connections

## Related Pages

- [YugabyteDB Connection Error](/tools/yugabyte/yugabyte-connection-error)
- [YugabyteDB Auth Error](/tools/yugabyte/yugabyte-auth-error)
- [YugabyteDB Config Error](/tools/yugabyte/yugabyte-gflag-error)
