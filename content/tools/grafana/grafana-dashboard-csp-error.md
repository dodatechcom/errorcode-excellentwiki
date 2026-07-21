---
title: "[Solution] Grafana Dashboard CSP Error"
description: "How to fix Grafana CSP errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- CSP blocking inline scripts
- External resource loading blocked

## How to Fix

```ini
[security]
content_security_policy = true
content_security_policy_template = "script-src 'self' 'unsafe-inline' 'unsafe-eval'; style-src 'self' 'unsafe-inline';"
```

## Examples

```bash
curl -I http://localhost:3000/api/health | grep -i content-security-policy
```
