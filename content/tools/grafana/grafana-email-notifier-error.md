---
title: "[Solution] Grafana Email Notifier Error"
description: "How to fix Grafana email notification errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- SMTP server not configured
- SMTP authentication failure
- SMTP TLS/STARTTLS error

## How to Fix

```ini
[smtp]
enabled = true
host = smtp.gmail.com:587
user = alerts@example.com
password = your-password
from_address = grafana@example.com
```

## Examples

```bash
journalctl -u grafana-server | grep -i smtp
```
