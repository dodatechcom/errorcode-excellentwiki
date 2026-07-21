---
title: "[Solution] Grafana Dashboard Public Access Error"
description: "How to fix Grafana public dashboard errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Anonymous access not enabled
- Public dashboard not configured
- Sensitive data exposed

## How to Fix

```ini
[auth.anonymous]
enabled = true
org_name = Main Org.
org_role = Viewer
```

## Examples

```bash
curl -s http://localhost:3000/api/org | jq '.name'
```
