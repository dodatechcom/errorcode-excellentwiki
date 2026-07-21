---
title: "[Solution] Prometheus Target Labels Conflict"
description: "How to fix target labels conflicting in Prometheus relabeling"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Two relabel rules writing to the same target label
- Target exposing a label that conflicts with `job` or `instance`
- Multiple relabel_configs overwriting the same label
- honor_labels not set when target labels should be preserved

## How to Fix

Use honor_labels to preserve target labels:

```yaml
scrape_configs:
  - job_name: 'app'
    honor_labels: true
```

Avoid conflicting relabel rules:

```yaml
relabel_configs:
  # Check that no two rules write to the same target_label
  - source_labels: [__meta_consul_service]
    target_label: service
    action: replace
  # Do not also write to 'service' label
```

## Examples

```bash
# Check for label conflicts in logs
journalctl -u prometheus | grep "label conflict"

# View target labels
curl -s http://localhost:9090/api/v1/targets | jq '.data.activeTargets[0].labels'
```
