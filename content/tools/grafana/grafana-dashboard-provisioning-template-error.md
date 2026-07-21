---
title: "[Solution] Grafana Dashboard Provisioning Template Error"
description: "How to fix Grafana provisioning template errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Template syntax invalid
- Template variables not defined

## How to Fix

```yaml
apiVersion: 1
templates:
  - orgId: 1
    name: default
    template: |
      {{ define "slack.title" }}[{{ .Status | toUpper }}] {{ .Labels.alertname }}{{ end }}
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/v1/provisioning/templates | jq '.[].name'
```
