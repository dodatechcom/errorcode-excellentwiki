---
title: "[Solution] Grafana Dashboard Provisioning GitHub Error"
description: "How to fix Grafana provisioning from GitHub errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- GitHub token expired
- Repository path incorrect
- Branch not found

## How to Fix

```yaml
apiVersion: 1
providers:
  - name: 'github'
    type: github
    options:
      owner: myorg
      repository: grafana-dashboards
      token: ghp_xxx
      branch: main
      path: dashboards
```

## Examples

```bash
curl -H "Authorization: token ghp_xxx" "https://api.github.com/repos/myorg/grafana-dashboards/contents/dashboards" | jq '.[].name'
```
