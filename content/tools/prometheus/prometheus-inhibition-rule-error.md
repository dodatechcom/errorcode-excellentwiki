---
title: "[Solution] Prometheus Alertmanager Inhibition Rule Error"
description: "How to fix Alertmanager inhibition rules not suppressing alerts correctly"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Source and target matchers not matching correctly
- Inhibition rules applied in wrong order
- Label names case-sensitive mismatch
- Missing labels in inhibited alerts

## How to Fix

Configure inhibition rules:

```yaml
inhibit_rules:
  - source_matchers:
      - severity = critical
    target_matchers:
      - severity = warning
    equal: ['alertname', 'instance']
```

Test matcher expressions:

```bash
amtool --alertmanager.url=http://localhost:9093 config routes
```

Verify alert labels:

```bash
curl -s http://localhost:9090/api/v1/alerts | jq '.data.alerts[] | .labels'
```

## Examples

```bash
# Check inhibition rules
amtool --alertmanager.url=http://localhost:9093 config show | grep -A 10 inhibit_rules

# View inhibited alerts
curl -s http://localhost:9090/api/v1/alerts | jq '.data.alerts[] | select(.status.inhibitedBy != null)'
```
