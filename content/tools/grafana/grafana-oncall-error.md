---
title: "[Solution] Grafana OnCall Error"
description: "Fix Grafana oncall errors. Learn why this happens and how to resolve it quickly."
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Grafana OnCall Error

Grafana OnCall errors occur when alerting, escalation, or on-call scheduling fails.

## Why This Happens

- Escalation failed
- Schedule error
- Notification not sent
- Integration failed

## Common Error Messages

- `oncall_escalation_error`
- `oncall_schedule_error`
- `oncall_notification_error`
- `oncall_integration_error`

## How to Fix It

### Solution 1: Configure OnCall

Set up OnCall integration:

```yaml
escalation_policies:
  - name: default
    steps:
      - type: notify_users
        users: ["user@example.com"]
```

### Solution 2: Check schedules

Verify on-call schedules are configured.

### Solution 3: Fix integrations

Check integration settings.


## Common Scenarios

- **Escalation failed:** Check escalation policy configuration.
- **Notification not sent:** Verify notification channels.

## Prevent It

- Configure escalation policies
- Test notifications
- Monitor on-call status
