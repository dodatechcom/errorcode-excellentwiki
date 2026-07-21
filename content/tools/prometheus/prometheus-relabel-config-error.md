---
title: "[Solution] Prometheus Relabel Config Error"
description: "How to fix Prometheus relabel configuration errors"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Invalid regex pattern in relabel_config
- Missing required fields (source_labels, target_label)
- Unknown action specified
- Regex match group index out of range

## How to Fix

Validate relabel config syntax:

```yaml
scrape_configs:
  - job_name: 'app'
    relabel_configs:
      - source_labels: [__address__]
        regex: '(.*):(.*)'
        target_label: host
        replacement: '${1}'
        action: replace
```

Check regex pattern:

```bash
echo "localhost:8080" | grep -P '(.*):(.*)'
```

Valid relabel actions:

```yaml
# replace (default): regex match and replace
# keep: keep targets matching regex
# drop: drop targets matching regex
# hashmod: hash modulo
# labelmap: map label names
```

## Examples

```bash
# Test relabel regex
echo "10.0.0.1:8080" | grep -oP '(\d+\.\d+\.\d+\.\d+)'

# Check relabel configs
curl -s http://localhost:9090/api/v1/status/config | grep -A 10 relabel_configs

# Validate config
promtool check config prometheus.yml
```
