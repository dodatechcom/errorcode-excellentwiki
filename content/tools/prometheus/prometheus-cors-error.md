---
title: "[Solution] Prometheus CORS Error"
description: "How to fix Prometheus Cross-Origin Resource Sharing errors"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Browser blocking cross-origin requests to Prometheus API
- Missing CORS headers in Prometheus response
- Grafana or other tool accessing Prometheus from different origin
- Web configuration missing CORS settings

## How to Fix

Configure CORS in web-config.yml:

```yaml
tls_server_config:
  cert_file: /etc/prometheus/server.crt
  key_file: /etc/prometheus/server.key
```

Use Grafana proxy instead of direct access:

```ini
# grafana.ini
[auth.proxy]
enabled = true
```

## Examples

```bash
# Test CORS headers
curl -I -X OPTIONS -H "Origin: http://grafana:3000" http://localhost:9090/api/v1/query

# Check web configuration
curl -s http://localhost:9090/api/v1/status/config | grep -i cors
```
