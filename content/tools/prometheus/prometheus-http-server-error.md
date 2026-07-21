---
title: "[Solution] Prometheus HTTP Server Error"
description: "How to fix Prometheus HTTP server errors when exposing metrics and API"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Port already in use
- Insufficient permissions to bind port
- Too many concurrent connections
- Request handler panic

## How to Fix

Check if port is available:

```bash
ss -tlnp | grep 9090
lsof -i :9090
```

Start with custom listen address:

```bash
prometheus --web.listen-address=0.0.0.0:9090
```

Check Prometheus process status:

```bash
curl http://localhost:9090/-/healthy
```

## Examples

```bash
# Check Prometheus health
curl http://localhost:9090/-/healthy

# Monitor HTTP requests
curl -s 'http://localhost:9090/api/v1/query?query=prometheus_http_requests_total'

# Check for errors
journalctl -u prometheus | grep -i "error"
```
