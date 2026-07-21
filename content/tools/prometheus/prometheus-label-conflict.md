---
title: "[Solution] Prometheus Label Conflict Error"
description: "How to fix Prometheus label conflict when target and relabeling clash"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Target exposes a label that conflicts with relabel target
- `honor_labels: false` causing target labels to be overwritten
- Multiple relabel rules writing to the same target label
- Reserved labels (`job`, `instance`) conflicting with target labels

## How to Fix

Use `honor_labels: true` to keep target labels:

```yaml
scrape_configs:
  - job_name: 'app'
    honor_labels: true
    static_configs:
      - targets: ['localhost:8080']
```

Check for label conflicts in logs:

```bash
journalctl -u prometheus | grep "label conflict"
```

Adjust relabeling to avoid conflicts:

```yaml
    relabel_configs:
      - source_labels: [__meta_consul_service]
        target_label: service_name
        action: replace
```

## Examples

```bash
# Check for conflicting labels
curl -s 'http://localhost:9090/api/v1/query?query={__name__!=""}' | jq '.data.result[0].metric' | sort

# View relabel configs
curl -s http://localhost:9090/api/v1/status/config | grep -A 10 relabel_configs
```
