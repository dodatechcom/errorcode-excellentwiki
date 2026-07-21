---
title: "[Solution] Prometheus Basic Auth Error"
description: "How to fix basic authentication errors when scraping password-protected endpoints"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Wrong username or password in basic_auth config
- Password file not found or unreadable
- Target does not accept basic authentication
- Special characters in password not handled properly

## How to Fix

Configure basic auth in scrape config:

```yaml
scrape_configs:
  - job_name: 'app'
    basic_auth:
      username: admin
      password: secret123
    static_configs:
      - targets: ['localhost:8080']
```

Use password file for security:

```yaml
scrape_configs:
  - job_name: 'app'
    basic_auth:
      username: admin
      password_file: /etc/prometheus/password
```

Create the password file:

```bash
echo 'secret123' > /etc/prometheus/password
chmod 600 /etc/prometheus/password
```

## Examples

```bash
# Test basic auth manually
curl -u admin:secret123 http://localhost:8080/metrics

# Verify credentials
curl -u admin:wrongpass http://localhost:8080/metrics
```
