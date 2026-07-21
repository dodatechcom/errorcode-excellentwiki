---
title: "[Solution] Prometheus Alertmanager Routing Tree Error"
description: "How to fix Alertmanager routing tree configuration errors"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Invalid receiver name in route
- Circular route references
- Missing default receiver
- Route matchers with syntax errors

## How to Fix

Configure proper routing tree:

```yaml
route:
  receiver: 'default'
  group_by: ['alertname', 'cluster']
  group_wait: 30s
  group_interval: 5m
  repeat_interval: 4h
  routes:
    - match:
        severity: critical
      receiver: 'pagerduty-critical'
    - match:
        severity: warning
      receiver: 'slack-warning'
```

Validate configuration:

```bash
amtool check-config alertmanager.yml
```

## Examples

```bash
# Validate routing config
amtool check-config /etc/alertmanager/alertmanager.yml

# Test route matching
amtool --alertmanager.url=http://localhost:9093 config routes --tree

# View active routes
curl http://localhost:9093/api/v2/status | jq '.config.original.route'
```
