---
title: "[Solution] Prometheus Service Discovery Error"
description: "Fix Prometheus service discovery errors. Learn why this happens and how to resolve it quickly."
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Prometheus Service Discovery Error

Prometheus service discovery errors occur when targets are not discovered automatically.

## Why This Happens

- SD config invalid
- Provider unreachable
- Label mismatch
- Refresh interval wrong

## Common Error Messages

- `sd_config_error`
- `sd_provider_error`
- `sd_label_error`
- `sd_refresh_error`

## How to Fix It

### Solution 1: Configure service discovery

Set up proper SD:

```yaml
scrape_configs:
  - job_name: 'kubernetes'
    kubernetes_sd_configs:
      - role: pod
        namespaces:
          - default
```

### Solution 2: Check provider access

Verify the SD provider is accessible.

### Solution 3: Adjust refresh interval

Set appropriate refresh interval.


## Common Scenarios

- **Targets not discovered:** Check SD configuration and provider access.
- **Labels missing:** Verify label selectors.

## Prevent It

- Use appropriate SD role
- Monitor discovery
- Verify provider access
