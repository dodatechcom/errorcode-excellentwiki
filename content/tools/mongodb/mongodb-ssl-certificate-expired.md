---
title: "[Solution] MongoDB SSL Certificate Expired Error"
description: "Fix MongoDB SSL certificate expired error when TLS handshake fails due to expired server or client certificates"
tools: ["mongodb"]
error-types: ["tool-error"]
severities: ["error"]
---

# MongoDB SSL Certificate Expired Error

The TLS/SSL handshake fails because the server or client certificate has expired. MongoDB rejects connections when certificate validity cannot be verified.

## Common Causes

- Server TLS certificate expired and was not renewed
- Client x.509 certificate expired
- Certificate Authority (CA) certificate is expired
- Certificate was issued with a short validity period
- System clock is incorrect, making valid certificates appear expired

## How to Fix

### Check Certificate Expiry

```bash
# Check server certificate expiry
openssl s_client -connect localhost:27017 </dev/null 2>/dev/null | \
  openssl x509 -noout -dates

# Check a specific PEM file
openssl x509 -in /etc/ssl/mongodb-server.pem -noout -dates
```

### Renew Expired Certificate

```bash
# Generate new server certificate
openssl req -new -x509 -days 3650 -nodes \
  -out /etc/ssl/mongodb-server.pem \
  -keyout /etc/ssl/mongodb-server-key.pem \
  -subj "/CN=mongodb-server/O=MyOrg"

# Restart mongod with new certificate
mongod --sslMode requireSSL \
  --sslPEMKeyFile /etc/ssl/mongodb-server.pem
```

### Verify System Clock

```bash
# Check current time
date -u
timedatectl status

# Fix clock
sudo ntpdate -s pool.ntp.org
```

### Connect With Updated Certificate

```javascript
const client = new MongoClient(uri, {
  ssl: true,
  sslValidate: true,
  sslCert: '/etc/ssl/client.pem',
  sslKey: '/etc/ssl/client-key.pem',
  sslCA: '/etc/ssl/ca.pem',
  checkServerIdentity: false  // only for testing
});
```

## Examples

```
MongoServerError: SSL certificate has expired.
  subject: CN=mongodb-server, O=MyOrg
  notAfter: Jan 1 00:00:00 2025 GMT

MongoNetworkError: SSL peer certificate validation failed:
  certificate has expired
```

## Related Errors

- [MongoDB SSL TLS Handshake Failed]({{< relref "/tools/mongodb/mongodb-ssl-tls-handshake-failed" >}}) -- handshake issues
- [MongoDB X509 Authentication Error]({{< relref "/tools/mongodb/mongodb-x509-authentication-error" >}}) -- x509 auth
- [MongoDB Authentication Failed]({{< relref "/tools/mongodb/mongodb-authentication-failed" >}}) -- auth failures
