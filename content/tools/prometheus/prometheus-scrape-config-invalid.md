---
title: "[Solution] Prometheus Scrape Config Invalid"
description: "How to fix invalid scrape_config entries in Prometheus configuration"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Missing `job_name` in scrape_config
- Invalid `static_configs` format
- Wrong `scheme` value (must be http or https)
- Malformed `targets` list
- Unknown fields in scrape_config

## How to Fix

Validate scrape configuration:

```bash
promtool check config prometheus.yml
```

Correct scrape_config structure:

```yaml
scrape_configs:
  - job_name: 'my-app'
    static_configs:
      - targets: ['localhost:8080']
```

Check for typos in field names:

```yaml
# Wrong: scrape_config (missing s)
scrape_config:
  - job_name: 'app'

# Correct
scrape_configs:
  - job_name: 'app'
```

Verify target format:

```yaml
# Wrong
targets: 'localhost:8080'

# Correct
targets: ['localhost:8080']
```

## Examples

```bash
# Test specific scrape config
promtool check config prometheus.yml 2>&1 | grep scrape

# Reload configuration
kill -HUP $(pidof prometheus)

# View active scrape targets
curl http://localhost:9090/api/v1/targets
```
