---
title: "[Solution] Grafana Dashboard Provisioning Folder Error"
description: "How to fix Grafana provisioning folder errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Folder not created before dashboard provisioning
- Folder UID mismatch

## How to Fix

```yaml
apiVersion: 1
providers:
  - name: 'default'
    folder: 'Production'
    type: file
    options:
      path: /var/lib/grafana/dashboards
```

## Examples

```bash
journalctl -u grafana-server | grep -i folder
```
