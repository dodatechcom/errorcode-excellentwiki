---
title: "[Solution] Grafana Notifier Provisioning Error"
description: "How to fix Grafana notification provisioning errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Invalid webhook URL
- Missing required fields
- Duplicate contact point names

## How to Fix

```yaml
apiVersion: 1
contactPoints:
  - orgId: 1
    name: slack-alerts
    receivers:
      - uid: slack-channel
        type: slack
        settings:
          url: https://hooks.slack.com/services/T00/B00/xxx
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/v1/provisioning/contact-points | jq '.[].name'
```
