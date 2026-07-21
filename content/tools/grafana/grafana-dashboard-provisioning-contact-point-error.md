---
title: "[Solution] Grafana Dashboard Provisioning Contact Point Error"
description: "How to fix Grafana provisioning contact point errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Contact point referenced by alert not provisioned
- Settings incomplete

## How to Fix

```yaml
apiVersion: 1
contactPoints:
  - orgId: 1
    name: ops-team
    receivers:
      - uid: slack-1
        type: slack
        settings:
          url: https://hooks.slack.com/services/T00/B00/xxx
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/v1/provisioning/contact-points | jq '.[].name'
```
