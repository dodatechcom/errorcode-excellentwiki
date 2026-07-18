---
title: "[Solution] Docker Compose TLS Certificate Verification Failed Error — How to Fix"
description: "Fix Docker Compose TLS certificate verification failed errors. Resolve SSL handshake failures, certificate trust issues, and registry errors."
comments: true
---

## What This Error Means

The `TLS certificate verification failed` error occurs when Docker Compose cannot verify the SSL/TLS certificate presented by a registry, API endpoint, or another service during build, pull, or runtime operations. The certificate chain is invalid, expired, self-signed, or not trusted.

A typical error:

```
Error response from daemon: Get "https://registry.example.com/v2/":
tls: failed to verify certificate: x509: certificate
signed by unknown authority
```

Or:

```
x509: certificate has expired or is not yet valid
```

Or:

```
Error: error while interpolating environment variables:
failed to connect to TCP host:
x509: certificate signed by unknown authority
```

Or:

```
certificate verify failed: unable to get local issuer certificate
```

## Why It Happens

TLS certificate errors occur when:

- **Self-signed certificates**: The registry or endpoint uses a certificate that is not signed by a trusted Certificate Authority.
- **Expired certificate**: The server's certificate has passed its validity period.
- **Missing CA certificate**: The Certificate Authority that signed the certificate is not in Docker's trust store.
- **Intermediate certificate missing**: The certificate chain is incomplete, missing intermediate CA certificates.
- **Hostname mismatch**: The certificate is issued for a different hostname than the one being accessed.
- **Corporate proxy intercepting TLS**: A man-in-the-middle proxy re-signs traffic with its own certificate.
- **Docker daemon trust store outdated**: The system's CA certificate bundle is not updated.

## Common Error Messages

### Unknown certificate authority

```
x509: certificate signed by unknown authority
```

The certificate is valid but signed by a CA that Docker does not trust.

### Expired certificate

```
x509: certificate has expired or is not yet valid: current time
2024-03-15 is after 2024-01-01T00:00:00Z
```

The certificate's validity period has ended.

### Hostname verification failure

```
x509: cannot validate certificate for 192.168.1.100
because it doesn't contain any IP SANs
```

The certificate is issued for a domain name, not the IP address being used.

### Incomplete certificate chain

```
tls: failed to verify certificate: x509: certificate
signed by unknown authority (possibly because of
"x509: missing intermediate certificate"
```

The server does not provide the full certificate chain.

## How to Fix It

### Solution 1: Add the certificate to Docker's trust store

Copy the CA certificate to Docker's certificate directory.

```bash
# Create the certificate directory for the registry
sudo mkdir -p /etc/docker/certs.d/registry.example.com

# Copy the CA certificate
sudo cp ca.crt /etc/docker/certs.d/registry.example.com/ca.crt

# For the Docker daemon itself
sudo mkdir -p /etc/docker/certs.d/registry.example.com
sudo cp ca.crt /etc/docker/certs.d/registry.example.com/ca.crt

# Restart Docker
sudo systemctl restart docker
```

### Solution 2: Configure insecure registries

Allow Docker to connect to registries without TLS verification (development only).

```bash
# Edit Docker daemon configuration
sudo tee /etc/docker/daemon.json <<EOF
{
  "insecure-registries": [
    "registry.example.com:5000",
    "192.168.1.100:5000"
  ]
}
EOF

# Restart Docker
sudo systemctl restart docker
```

```yaml
# Use insecure registry in compose file
services:
  api:
    image: registry.example.com:5000/myapi:latest
    # The registry must be in insecure-registries config
```

### Solution 3: Update system CA certificates

Keep the CA certificate bundle current.

```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install ca-certificates
sudo update-ca-certificates

# CentOS/RHEL
sudo update-ca-trust

# Alpine
apk add ca-certificates
```

### Solution 4: Configure Docker to trust a custom CA

Add a custom CA to the system-wide trust store.

```bash
# Copy the custom CA certificate
sudo cp custom-ca.crt /usr/local/share/ca-certificates/custom-ca.crt

# Update the trust store
sudo update-ca-certificates

# Restart Docker to pick up new certificates
sudo systemctl restart docker
```

### Solution 5: Fix certificate chain issues on the server

Ensure the server provides the complete certificate chain.

```bash
# Test the certificate chain
openssl s_client -connect registry.example.com:443 -showcerts

# Verify the certificate
openssl verify -CAfile ca.crt server.crt

# Check certificate expiry
openssl x509 -in server.crt -noout -dates
```

### Solution 6: Configure compose services for self-signed TLS

For internal services using self-signed certificates, disable TLS verification in the application.

```yaml
services:
  api:
    image: myapi:latest
    environment:
      # Python requests
      - REQUESTS_CA_BUNDLE=/certs/ca.crt
      # Node.js
      - NODE_TLS_REJECT_UNAUTHORIZED=0
      # Java
      - JAVA_OPTS=-Djavax.net.ssl.trustStore=/certs/truststore.jks
    volumes:
      - ./certs:/certs:ro
```

## Common Scenarios

### Private Docker registry with self-signed certificate

An internal registry uses a certificate signed by the company's private CA.

```bash
# Create certificate directory
sudo mkdir -p /etc/docker/certs.d/myregistry.local:5000

# Copy the company CA certificate
sudo cp /etc/ssl/certs/company-ca.crt \
  /etc/docker/certs.d/myregistry.local:5000/ca.crt

# Restart Docker
sudo systemctl restart docker

# Test pulling an image
docker pull myregistry.local:5000/myapp:latest
```

### Corporate proxy intercepting HTTPS

A corporate proxy performs TLS interception, replacing server certificates with its own.

```bash
# Export the proxy's CA certificate
echo | openssl s_client -connect proxy.corp.com:443 -showcerts 2>/dev/null | \
  openssl x509 -outform PEM > proxy-ca.crt

# Add to Docker trust store
sudo cp proxy-ca.crt /usr/local/share/ca-certificates/proxy-ca.crt
sudo update-ca-certificates
sudo systemctl restart docker
```

### Build context downloading from HTTPS source

A Dockerfile downloads a resource over HTTPS from a server with an invalid certificate.

```dockerfile
# Dockerfile
RUN wget https://internal.server.com/package.tar.gz
# Fails with: x509: certificate signed by unknown authority
```

Fix by adding the CA certificate during build:

```dockerfile
FROM ubuntu:22.04

COPY company-ca.crt /usr/local/share/ca-certificates/
RUN update-ca-certificates

RUN wget https://internal.server.com/package.tar.gz
```

## Prevent It

- **Use trusted certificates from established CAs**: Avoid self-signed certificates in production. Use Let's Encrypt or a proper internal CA that is added to all Docker hosts' trust stores during provisioning.
- **Automate CA certificate distribution**: Include CA certificate installation in your infrastructure provisioning scripts (Ansible, Terraform, cloud-init). Every Docker host should have the necessary CA certificates before any compose stack is deployed.
- **Monitor certificate expiration**: Set up alerts for certificate expiration dates well in advance. Use tools like `openssl` or monitoring services to check certificate validity and renew before expiry to prevent service disruptions.
