---
title: "[Solution] Prometheus TLS Config Error"
description: "How to fix TLS configuration errors in Prometheus scrape and remote write"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Invalid or missing TLS certificate file
- Certificate and key mismatch
- Expired TLS certificate
- CA certificate not trusted
- Wrong file permissions on TLS files

## How to Fix

Configure TLS in scrape config:

```yaml
scrape_configs:
  - job_name: 'app'
    scheme: 'https'
    tls_config:
      ca_file: /etc/prometheus/ca.crt
      cert_file: /etc/prometheus/client.crt
      key_file: /etc/prometheus/client.key
      insecure_skip_verify: false
```

Verify certificate validity:

```bash
openssl x509 -in /etc/prometheus/client.crt -noout -dates
```

Check certificate and key match:

```bash
diff <(openssl x509 -in client.crt -noout -modulus)      <(openssl rsa -in client.key -noout -modulus)
```

## Examples

```bash
# Test HTTPS connection
curl --cacert /etc/prometheus/ca.crt https://target:443/metrics

# Check certificate chain
openssl s_client -connect target:443 -CAfile /etc/prometheus/ca.crt

# Skip certificate verification (testing only)
tls_config:
  insecure_skip_verify: true
```
