---
title: "[Solution] Grafana Dashboard Provisioning Mute Time Error"
description: "How to fix Grafana provisioning mute time errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Mute time interval syntax wrong
- Time range not valid

## How to Fix

```yaml
apiVersion: 1
muteTimeIntervals:
  - orgId: 1
    name: weekends
    timeIntervals:
      - weekdays: ['saturday', 'sunday']
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/v1/provisioning/mute-timings | jq '.[].name'
```
