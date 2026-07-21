---
title: "[Solution] Prometheus Alertmanager Pushover Receiver Error"
description: "How to fix Alertmanager Pushover notification errors"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Invalid Pushover user key or application token
- Pushover API unreachable
- Notification priority too high for user settings
- Message length exceeding Pushover limit

## How to Fix

Configure Pushover receiver:

```yaml
receivers:
  - name: 'pushover'
    pushover_configs:
      - user_key: 'your-user-key'
        token: 'your-application-token'
        title: '{{ .CommonAnnotations.summary }}'
        message: '{{ .CommonAnnotations.description }}'
        priority: '{{ if eq .CommonLabels.severity "critical" }}2{{ else }}0{{ end }}'
```

## Examples

```bash
# Test Pushover notification
curl -s   --form-string "token=YOUR_APP_TOKEN"   --form-string "user=YOUR_USER_KEY"   --form-string "message=Test alert from Prometheus"   https://api.pushover.net/1/messages.json
```
