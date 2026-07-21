---
title: "[Solution] Prometheus Alertmanager Email Receiver Error"
description: "How to fix Alertmanager email notification errors"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- SMTP server unreachable or misconfigured
- Authentication failure with SMTP server
- Invalid email addresses in configuration
- SMTP TLS configuration error
- Email content exceeding size limit

## How to Fix

Configure email receiver:

```yaml
receivers:
  - name: 'email'
    email_configs:
      - to: 'ops-team@example.com'
        from: 'alertmanager@example.com'
        smarthost: 'smtp.example.com:587'
        auth_username: 'alertmanager@example.com'
        auth_password: 'password'
        require_tls: true
```

Test SMTP connectivity:

```bash
telnet smtp.example.com 587
```

## Examples

```bash
# Test email sending
echo "Test email" | mail -s "Alert Test" ops-team@example.com

# Check email notification status
curl http://localhost:9093/metrics | grep "alertmanager_notifications_total"

# Verify SMTP config
amtool check-config /etc/alertmanager/alertmanager.yml
```
