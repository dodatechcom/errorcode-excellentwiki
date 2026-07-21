---
title: "[Solution] Grafana Plugin Dependency Error"
description: "How to fix Grafana plugin dependency errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Required Grafana version mismatch
- Missing companion plugin
- Node.js version mismatch

## How to Fix

```bash
grafana-cli --version
sudo apt-get install grafana
sudo systemctl restart grafana-server
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/plugins | jq '.[] | {id: .id, version: .info.version}'
```
