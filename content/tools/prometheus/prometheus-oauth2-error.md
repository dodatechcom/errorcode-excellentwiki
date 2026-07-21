---
title: "[Solution] Prometheus OAuth2 Error"
description: "How to fix OAuth2 authentication errors in Prometheus scrape and remote write"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Invalid client_id or client_secret
- Token URL endpoint unreachable
- OAuth2 token expired and not refreshed
- Scopes not matching target requirements
- TLS errors connecting to OAuth2 provider

## How to Fix

Configure OAuth2 in scrape config:

```yaml
scrape_configs:
  - job_name: 'app'
    oauth2:
      client_id: my-client-id
      client_secret: my-client-secret
      token_url: https://auth.example.com/token
      scopes:
        - read:metrics
      tls_config:
        ca_file: /etc/prometheus/ca.crt
```

Use client credentials file:

```yaml
    oauth2:
      client_id: my-client-id
      client_secret_file: /etc/prometheus/client_secret
      token_url: https://auth.example.com/token
```

## Examples

```bash
# Test OAuth2 token retrieval
curl -X POST https://auth.example.com/token   -d 'grant_type=client_credentials&client_id=my-id&client_secret=my-secret'

# Check Prometheus logs for OAuth errors
journalctl -u prometheus | grep -i oauth
```
