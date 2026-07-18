---
title: "[Solution] CouchDB SSL Error — How to Fix"
description: "Fix CouchDB SSL/TLS errors by generating valid certificates, configuring HTTPS, and resolving certificate chain issues"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB SSL Error

CouchDB SSL errors occur when TLS/HTTPS connections fail due to invalid certificates, misconfigured SSL settings, or protocol mismatches.

## Why It Happens

- Self-signed certificate is not trusted by the client
- Certificate has expired or is not yet valid
- SSL certificate does not match the server hostname
- Wrong port configured for HTTPS (6984 instead of 5984)
- TLS version mismatch between client and server
- Private key does not match the certificate

## Common Error Messages

```
{ "error": "ssl_error", "reason": "certificate verify failed" }
```

```
SSL: CERTIFICATE_VERIFY_FAILED
```

```
{ "error": "ssl_error", "reason": "no suitable peer certificate" }
```

```
{ "error": "econnrefused", "reason": "Connection refused - connect(2) for port 6984" }
```

## How to Fix It

### 1. Generate SSL Certificate

```bash
# Generate self-signed certificate for testing
openssl req -x509 -newkey rsa:4096 \
  -keyout /opt/couchdb/etc/ssl/server.key \
  -out /opt/couchdb/etc/ssl/server.crt \
  -days 365 -nodes \
  -subj "/C=US/ST=State/L=City/O=Org/CN=couch.example.com"

# Set correct permissions
chmod 600 /opt/couchdb/etc/ssl/server.key
chmod 644 /opt/couchdb/etc/ssl/server.crt
chown couchdb:couchdb /opt/couchdb/etc/ssl/server.*
```

### 2. Configure CouchDB for HTTPS

```ini
; In local.ini
[daemons]
; Enable HTTPS
{chttpd, start_link, [
  {ip, "0.0.0.0"},
  {port, 6984},
  {ssl, true},
  {certfile, "/opt/couchdb/etc/ssl/server.crt"},
  {keyfile, "/opt/couchdb/etc/ssl/server.key"}
]}
```

```bash
# Restart CouchDB after SSL configuration
sudo systemctl restart couchdb

# Test HTTPS connection
curl -k https://localhost:6984/
```

### 3. Fix Certificate Chain Issues

```bash
# Verify certificate
openssl x509 -in /opt/couchdb/etc/ssl/server.crt -text -noout

# Check certificate expiration
openssl x509 -in /opt/couchdb/etc/ssl/server.crt -enddate -noout

# Verify key matches certificate
openssl x509 -noout -modulus -in server.crt | md5sum
openssl rsa -noout -modulus -in server.key | md5sum
# Both should output the same hash
```

### 4. Configure Client to Trust Self-Signed Cert

```bash
# Add certificate to system trust store (Ubuntu/Debian)
sudo cp server.crt /usr/local/share/ca-certificates/couchdb.crt
sudo update-ca-certificates

# Or use curl with --cacert
curl --cacert /opt/couchdb/etc/ssl/server.crt https://localhost:6984/

# Or skip verification (testing only)
curl -k https://localhost:6984/
```

## Common Scenarios

- **Self-signed cert rejected by client**: Add the cert to the client's trust store or use `--cacert`.
- **Certificate expired**: Regenerate with a new validity period.
- **Mixed HTTP/HTTPS**: Ensure all nodes use the same protocol in the cluster.

## Prevent It

- Use Let's Encrypt for production certificates with auto-renewal
- Monitor certificate expiration dates
- Configure proper certificate chain including intermediate certificates

## Related Pages

- [CouchDB Connection Error](/tools/couchdb/couchdb-connection-error)
- [CouchDB Auth Error](/tools/couchdb/couchdb-auth-error)
- [CouchDB HTTP Error](/tools/couchdb/couchdb-http-error)
