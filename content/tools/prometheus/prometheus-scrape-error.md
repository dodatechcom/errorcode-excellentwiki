---
title: "[Solution] Prometheus Scrape Error"
description: "Fix Prometheus scrape errors. Learn why this happens and how to resolve it quickly."
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Prometheus Scrape Error

Prometheus scrape errors occur when the server cannot collect metrics from target endpoints.

## Why This Happens

- Target unreachable
- TLS certificate invalid
- Authentication failed
- Scrape timeout exceeded

## Common Error Messages

- `scrape_failed`
- `scrape_timeout`
- `target_down`
- `scrape_auth_error`

## How to Fix It

### Solution 1: Verify target configuration

Check targets in the targets page:

```yaml
scrape_configs:
  - job_name: 'myapp'
    static_configs:
      - targets: ['localhost:9090'
```

### Solution 2: Fix TLS issues

Ensure certificates are valid:

```yaml
scrape_configs:
  - job_name: 'myapp'
    tls_config:
      ca_file: /etc/prometheus/ca.crt
```

### Solution 3: Check network connectivity

Verify Prometheus can reach the target:

```bash
curl http://target:9090/metrics
```


## Common Scenarios

- **Target shows as down:** Check if the target is accessible from the Prometheus server.
- **Scrape timeout:** Increase the scrape_timeout or optimize the target's metrics endpoint.

## Prevent It

- Verify network connectivity
- Use TLS for secure targets
- Monitor scrape duration
