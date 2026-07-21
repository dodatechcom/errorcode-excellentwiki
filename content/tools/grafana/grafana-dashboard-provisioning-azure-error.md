---
title: "[Solution] Grafana Dashboard Provisioning Azure DevOps Error"
description: "How to fix Grafana provisioning from Azure DevOps errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Azure DevOps PAT invalid
- Project or repository wrong

## How to Fix

```yaml
apiVersion: 1
providers:
  - name: 'azure'
    type: azuredevops
    options:
      repo: myorg/myproject/myrepo
      branch: main
      path: dashboards
```

## Examples

```bash
curl -u ":PAT" "https://dev.azure.com/myorg/myproject/_apis/git/repositories/myrepo/items?path=dashboards" | jq '.value[].path'
```
