---
title: "[Solution] Prometheus OAuth2 Token Error"
description: "Fix Prometheus OAuth2 token errors. Resolve authentication failures when using OAuth2 for remote write or scrape."
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

# Prometheus OAuth2 Token Error

Prometheus OAuth2 token errors occur when the OAuth2 client fails to obtain or refresh an access token for authenticating with a remote endpoint or scrape target.

## Common Causes

- OAuth2 client credentials are invalid or expired
- Token endpoint URL is incorrect or unreachable
- Client secret is missing or misconfigured
- OAuth2 scope is not authorized for the client

## How to Fix It

### Solution 1: Configure OAuth2 credentials correctly

Set up OAuth2 in prometheus.yml:

```yaml
scrape_configs:
  - job_name: "oauth-app"
    oauth2:
      client_id: "prometheus-client"
      client_secret_file: "/etc/prometheus/secrets/client_secret"
      token_url: "https://auth.example.com/oauth/token"
      scopes:
        - "metrics:read"
    static_configs:
      - targets: ["app:8080"]
```

### Solution 2: Test the token endpoint

Manually request a token:

```bash
curl -X POST "https://auth.example.com/oauth/token" \
  -d "grant_type=client_credentials" \
  -d "client_id=prometheus-client" \
  -d "client_secret=secret123" \
  -d "scope=metrics:read"
```

### Solution 3: Check token refresh logs

Monitor Prometheus logs for OAuth2 errors:

```bash
journalctl -u prometheus | grep -i "oauth\|token" | tail -20
```

## Prevent It

- Use client_secret_file instead of inline secrets
- Monitor OAuth2 token expiry and refresh
- Test token acquisition before deploying
