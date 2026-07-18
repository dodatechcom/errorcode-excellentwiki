---
title: "[Solution] MariaDB SSL Error — How to Fix"
description: "Fix MariaDB SSL certificate errors, handshake failures, and TLS version mismatches by configuring SSL files, ciphers, and client settings properly"
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# MariaDB SSL Error

SSL errors in MariaDB occur when the encrypted connection between client and server cannot be established. This happens due to missing or expired certificates, mismatched CN, unsupported TLS versions, or missing CA files.

## Why It Happens

- SSL certificate files are missing, expired, or have wrong permissions
- Certificate CN or SAN does not match the hostname
- Server and client support different TLS versions
- `require_secure_transport` is ON but SSL is not configured
- CA certificate is not provided to the client
- Private key does not match the certificate

## Common Error Messages

```
ERROR 2026 (HY000): SSL connection error: SSL_CTX_use_certificate_file failed
```

```
ERROR 2026 (HY000): SSL connection error: tlsv1 alert unknown ca
```

```
ERROR 2026 (HY000): SSL connection error: SSL23_GET_SERVER_HELLO:protocol version not supported
```

```
ERROR 2026 (HY000): SSL connection error: ASN1_get_object:header too long
```

## How to Fix It

### 1. Verify SSL Certificate Files

```bash
mysql -u root -e "SHOW VARIABLES LIKE '%ssl%';"

# Verify cert and key match
openssl x509 -noout -modulus -in server-cert.pem | md5sum
openssl rsa -noout -modulus -in server-key.pem | md5sum
```

### 2. Generate Fresh SSL Certificates

```bash
openssl genrsa 2048 > ca-key.pem
openssl req -new -x509 -nodes -days 3650 -key ca-key.pem -out ca.pem -subj "/CN=MySQL_CA"
openssl req -newkey rsa:2048 -nodes -keyout server-key.pem -out server-req.pem -subj "/CN=mysql-server"
openssl x509 -req -in server-req.pem -days 3650 -CA ca.pem -CAkey ca-key.pem -set_serial 01 -out server-cert.pem
chown mysql:mysql server-*.pem ca-*.pem
chmod 600 server-key.pem ca-key.pem
```

### 3. Configure MariaDB to Use SSL

```ini
[mysqld]
ssl-ca = /etc/mysql/ssl/ca.pem
ssl-cert = /etc/mysql/ssl/server-cert.pem
ssl-key = /etc/mysql/ssl/server-key.pem
tls_version = TLSv1.2,TLSv1.3
require_secure_transport = ON
```

### 4. Fix Client SSL Connection

```bash
mysql -h myhost -u myuser -p   --ssl-ca=/path/to/ca.pem   --ssl-cert=/path/to/client-cert.pem   --ssl-key=/path/to/client-key.pem
```

## Common Scenarios

- **Certificate expired after one year**: Regenerate certificates and restart MariaDB.
- **Application cannot verify server cert**: Provide the CA file to the client's trust store.
- **TLS version mismatch**: Upgrade client library or relax `tls_version` on the server.

## Prevent It

- Set calendar reminders for certificate rotation before expiry
- Use proper certificate management tools instead of self-signed certs in production
- Test SSL connections after any MariaDB upgrade

## Related Pages

- [MariaDB Connection Error](/tools/mariadb/mariadb-connection-error)
- [MariaDB User Error](/tools/mariadb/mariadb-user-error)
- [MySQL SSL Error](/tools/mysql/mysql-ssl-error)
