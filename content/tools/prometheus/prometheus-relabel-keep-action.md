---
title: "[Solution] Prometheus Relabel Keep Action Error"
description: "How to fix Prometheus relabel keep action dropping desired targets"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Regex pattern not matching any targets
- Wrong source_labels specified
- Regex is case-sensitive and does not match
- Missing leading or trailing anchors in regex

## How to Fix

Use correct keep action:

```yaml
scrape_configs:
  - job_name: 'app'
    relabel_configs:
      - source_labels: [__meta_consul_tags]
        regex: '.*,production,.*'
        action: keep
```

Test regex against label values:

```bash
echo "production,web,primary" | grep -P '.*,production,.*'
```

Use case-insensitive matching:

```yaml
    relabel_configs:
      - source_labels: [__meta_consul_tags]
        regex: '(?i).*production.*'
        action: keep
```

## Examples

```bash
# Test regex
echo "staging,web" | grep -P '.*,production,.*'
# No match - target will be dropped

echo "production,web" | grep -P '.*,production,.*'
# Match - target will be kept
```
