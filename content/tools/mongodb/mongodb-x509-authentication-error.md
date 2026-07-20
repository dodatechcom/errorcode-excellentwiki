---
title: "[Solution] MongoDB x509 Authentication Error"
description: "Fix MongoDB x509 certificate authentication errors"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB x509 Authentication Error

```
MongoServerError: x509 authentication failed
```

```
No matching subject found in client certificate
```

## Common Causes

- The certificate CN (Common Name) does not match the MongoDB username
- The CA certificate is not trusted by the server
- The certificate has expired
- The certificate is not in PEM format
- The certificate does not have the required key usage

## How to Fix

### 1. Create a MongoDB user matching the certificate CN

```javascript
use $external
db.createUser({
  user: "CN=myuser,OU=Engineering,O=MyCompany",
  roles: [{ role: "readWrite", db: "mydb" }],
  mechanisms: ["X.509"]
});
```

### 2. Configure the server to use x509

```yaml
# /etc/mongod.conf
security:
  authorization: enabled
  clusterAuthMode: x509
net:
  tls:
    mode: requireTLS
    certificateKeyFile: /etc/ssl/mongodb.pem
    CAFile: /etc/ssl/ca.pem
```

### 3. Connect with x509 authentication

```bash
mongosh \
  --tls \
  --tlsCertificateKeyFile /etc/ssl/client.pem \
  --tlsCAFile /etc/ssl/ca.pem \
  --authenticationMechanism MONGODB-X509 \
  --authenticationDatabase '$external' \
  --username "CN=myuser,OU=Engineering,O=MyCompany"
```

### 4. Verify the certificate

```bash
openssl x509 -in client.pem -noout -subject
```

## Examples

```bash
# Create client certificate
openssl req -new -x509 -days 365 -nodes \
  -out client.pem -keyout client-key.pem \
  -subj "/CN=myuser/OU=Engineering/O=MyCompany"

# Test x509 authentication
mongosh --tls \
  --tlsCertificateKeyFile client.pem \
  --tlsCAFile ca.pem \
  --authenticationMechanism MONGODB-X509 \
  --authenticationDatabase '$external'
```