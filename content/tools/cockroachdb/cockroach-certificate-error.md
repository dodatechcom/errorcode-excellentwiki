---
title: "[Solution] CockroachDB Certificate Error - Fix TLS and SSL Issues"
description: "Fix CockroachDB TLS certificate errors by generating valid CA and node certificates, verifying Subject Alternative Name entries, and setting correct file permis"
tools: ["cockroachdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

A CockroachDB certificate error occurs when the TLS handshake fails between the client and server, or between nodes in the cluster. The error messages include `certificate verify failed`, `SSL error`, or `x509: certificate signed by unknown authority`.

## What This Error Means

CockroachDB uses mutual TLS (mTLS) for inter-node and client-server communication. Both the server and client must present valid certificates signed by a CA that the other party trusts. A certificate error means the trust chain is broken, the certificate has expired, or the hostname does not match.

The error appears during the TLS handshake phase, before any SQL communication occurs. Common error codes include `x509: certificate signed by unknown authority`, `certificate has expired`, and `tls: bad certificate`.

## Why It Happens

- Using the auto-generated node certificates instead of a proper CA
- Certificate has expired (default CockroachDB certs expire after 1 year)
- Hostname or IP in the certificate does not match the actual server address
- Client certificate not signed by the same CA as the server
- Certificate file paths are incorrect or permissions are wrong
- Using `localhost` in the connection string but the cert is for a different hostname
- Mixing certificates from different CA hierarchies

## How to Fix It

### 1. Generate Proper Certificates

```bash
# Create CA cert
cockroach cert create-ca \
  --certs-dir=/certs \
  --ca-key=/certs/ca.key

# Create node cert
cockroach cert create-node \
  localhost 127.0.0.1 10.0.1.5 10.0.1.6 \
  --certs-dir=/certs \
  --ca-key=/certs/ca.key

# Create client cert
cockroach cert create-client \
  root \
  --certs-dir=/certs \
  --ca-key=/certs/ca.key
```

### 2. Start CockroachDB with TLS

```bash
cockroach start \
  --certs-dir=/certs \
  --advertise-addr=10.0.1.5 \
  --join=10.0.1.5:26257,10.0.1.6:26257
```

### 3. Connect with TLS Client

```bash
cockroach sql \
  --certs-dir=/certs \
  --host=10.0.1.5
```

### 4. Check Certificate Validity

```bash
openssl x509 -in /certs/node.crt -text -noout
# Check the Not Before, Not After, and Subject Alternative Names
```

### 5. Regenerate Expired Certificates

```bash
# Revoke and recreate all certificates
rm /certs/node.crt /certs/node.key /certs/client.root.crt /certs/client.root.key
cockroach cert create-node localhost 10.0.1.5 --certs-dir=/certs --ca-key=/certs/ca.key
cockroach cert create-client root --certs-dir=/certs --ca-key=/certs/ca.key
```

### 6. Verify File Permissions

```bash
chmod 600 /certs/ca.key /certs/node.key /certs/client.root.key
chmod 644 /certs/ca.crt /certs/node.crt /certs/client.root.crt
```

## Common Mistakes

- Using `--insecure` in production when TLS should be enabled
- Not including all node IPs and hostnames in the SAN (Subject Alternative Names)
- Forgetting that client certificates must be signed by the same CA as node certificates
- Not setting up certificate rotation before expiry

## Related Pages

- [CockroachDB Connection Refused](/tools/cockroachdb/cockroach-connection-refused)
- [CockroachDB Node Unavailable](/tools/cockroachdb/cockroach-node-unavailable)
- [CockroachDB Timeout](/tools/cockroachdb/cockroach-timeout)
