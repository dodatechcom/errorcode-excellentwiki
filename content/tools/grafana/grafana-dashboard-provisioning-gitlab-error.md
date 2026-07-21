---
title: "[Solution] Grafana Dashboard Provisioning GitLab Error"
description: "How to fix Grafana provisioning from GitLab errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- GitLab token invalid
- Project ID wrong

## How to Fix

```yaml
apiVersion: 1
providers:
  - name: 'gitlab'
    type: gitlab
    options:
      project: mygroup/myproject
      token: glpat-xxx
      branch: main
      path: dashboards
```

## Examples

```bash
curl -H "PRIVATE-TOKEN: glpat-xxx" "https://gitlab.com/api/v4/projects/mygroup%2Fmyproject/repository/tree?path=dashboards" | jq '.[].name'
```
