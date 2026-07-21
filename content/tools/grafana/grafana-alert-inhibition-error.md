---
title: "[Solution] Grafana Alert Inhibition Error"
description: "How to fix Grafana alert inhibition errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Source matchers not matching any alerts
- Target and source mismatch
- Rules ordering incorrect

## How to Fix

```yaml
inhibit_rules:
  - source_match:
      severity: 'critical'
    target_match:
      severity: 'warning'
    equal: ['alertname', 'instance']
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/alertmanager/grafana/api/v2/status | jq '.config.original'
```
