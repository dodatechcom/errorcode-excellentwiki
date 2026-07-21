---
title: "[Solution] Prometheus Relabel Drop Action Error"
description: "How to fix Prometheus relabel drop action incorrectly filtering targets"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Regex matching too broadly, dropping desired targets
- Wrong source_labels causing unexpected drops
- Regex pattern too permissive
- Testing regex without considering label format

## How to Fix

Use precise drop action:

```yaml
scrape_configs:
  - job_name: 'app'
    relabel_configs:
      - source_labels: [__meta_consul_tags]
        regex: '.*,deprecated,.*'
        action: drop
```

Test regex carefully:

```bash
# Test what will be dropped
echo "deprecated,v1" | grep -P '.*,deprecated,.*'
# Match - will be dropped

echo "production,v2" | grep -P '.*,deprecated,.*'
# No match - will be kept
```

## Examples

```bash
# View active targets
curl -s http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | .labels.instance'

# Check drop rules
curl -s http://localhost:9090/api/v1/status/config | grep -A 5 "action: drop"
```
