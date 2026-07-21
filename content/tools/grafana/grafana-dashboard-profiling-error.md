---
title: "[Solution] Grafana Dashboard Profiling Error"
description: "How to fix Grafana profiling errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Profiling endpoint disabled
- Dashboard load time exceeding threshold

## How to Fix

```ini
[profiling]
enabled = true
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" "http://localhost:3000/api/dashboards/uid/UID" -w "Total time: %{time_total}s\n" -o /dev/null
```
