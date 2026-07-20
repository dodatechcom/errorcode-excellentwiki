---
title: "[Solution] MongoDB SSL TLS Handshake Failed"
description: "Fix MongoDB SSL/TLS handshake errors during secure connections"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB SSL/TLS Handshake Failed Error

The TLS handshake failure prevents the client from establishing a secure connection:

```
MongoNetworkError: SSL handshake failed
```

```
error:14094418:SSL routines:ssl3_read_bytes:tlsv1 alert unknown ca
```

## Common Causes

- The server uses a self-signed certificate not trusted by the client
- The CA certificate is missing from the client's trust store
- TLS protocol version mismatch (server requires TLS 1.2, client uses 1.0)
- Certificate has expired
- The `--tls` flag is not passed to `mongosh`
- Certificate Common Name (CN) or SAN does not match the hostname
- Cipher suite is not supported by either side
- The PEM key file and certificate file are mismatched

## How to Fix

### 1. Enable TLS on the server

```yaml
# /etc/mongod.conf
net:
  tls:
    mode: requireTLS
    certificateKeyFile: /etc/ssl/mongodb.pem
    CAFile: /etc/ssl/ca.pem
```

### 2. Connect with the proper CA certificate

```bash
mongosh \
  --tls \
  --tlsCAFile /etc/ssl/ca.pem \
  --host mongo.example.com \
  --port 27017
```

### 3. Verify the certificate

```bash
openssl s_client -connect mongo.example.com:27017 -CAfile /etc/ssl/ca.pem
openssl x509 -in /etc/ssl/mongodb.pem -text -noout
```

### 4. Ensure certificate matches the hostname

```bash
openssl x509 -in /etc/ssl/mongodb.pem -noout -text | grep -A2 "Subject Alternative Name"
```

The SAN must include the hostname used in the connection string.

### 5. Use allowInvalidHostnames for testing only

```javascript
const client = new MongoClient(uri, {
  tls: true,
  tlsCAFile: '/etc/ssl/ca.pem',
  tlsAllowInvalidHostnames: true  // Not for production!
});
```

## Examples

```bash
# Generate a self-signed certificate for testing
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes

# Combine into PEM for MongoDB
cat key.pem cert.pem > /etc/ssl/mongodb.pem

# Test TLS connection
mongosh --tls --tlsCAFile /etc/ssl/ca.pem --host mongo.example.com

# Verify the cipher suite being used
openssl s_client -connect mongo.example.com:27017 -tls1_2
```