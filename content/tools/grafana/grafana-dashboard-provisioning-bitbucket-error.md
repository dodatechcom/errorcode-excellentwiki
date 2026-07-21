---
title: "[Solution] Grafana Dashboard Provisioning Bitbucket Error"
description: "How to fix Grafana provisioning from Bitbucket errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Bitbucket credentials invalid
- Workspace or repository wrong

## How to Fix

```yaml
apiVersion: 1
providers:
  - name: 'bitbucket'
    type: bitbucket
    options:
      owner: myworkspace
      repository: myrepo
      branch: main
      path: dashboards
```

## Examples

```bash
curl -u "user:app-password" "https://api.bitbucket.org/2.0/repositories/myworkspace/myrepo/src/main/dashboards/" | jq '.values[].name'
```
