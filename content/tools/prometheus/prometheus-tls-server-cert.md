---
title: "[Solution] Prometheus TLS Server Certificate Error"
description: "How to fix Prometheus TLS server certificate errors for web UI and API"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- TLS certificate expired
- Certificate does not match the server hostname
- Missing private key file
- Certificate chain incomplete

## How to Fix

Configure TLS for Prometheus web:

```bash
prometheus   --web.config.file=web-config.yml
```

Create web-config.yml:

```yaml
tls_server_config:
  cert_file: /etc/prometheus/server.crt
  key_file: /etc/prometheus/server.key
  client_auth_type: RequireAndVerifyClientCert
  client_ca_file: /etc/prometheus/ca.crt
```

## Examples

```bash
# Check certificate expiry
openssl x509 -in /etc/prometheus/server.crt -noout -dates

# Test HTTPS endpoint
curl -k https://localhost:9090/-/healthy

# Verify certificate chain
openssl s_client -connect localhost:9090 -CAfile /etc/prometheus/ca.crt
```
