---
title: "[Solution] Prometheus Relabel Labelmap Action Error"
description: "How to fix Prometheus labelmap relabel action for label name mapping"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Regex pattern not matching any label names
- Wrong regex for label name mapping
- Label names contain unexpected characters
- labelmap applied after other relabel rules modified labels

## How to Fix

Use correct labelmap configuration:

```yaml
relabel_configs:
  - regex: '__meta_consul_service_(.+)'
    target_label: 'consul_\1'
    action: labelmap
```

This maps labels like `__meta_consul_service_name` to `consul_name`.

Test regex against label names:

```bash
echo "__meta_consul_service_name" | grep -oP '__meta_consul_service_(.+)'
# Output: name
```

## Examples

```bash
# View meta labels
curl -s http://localhost:9090/api/v1/targets | jq '.data.activeTargets[0].labels' | grep meta

# Test regex
echo "__meta_consul_tags" | grep -oP '__meta_consul_service_(.+)'
```
