---
title: "[Solution] Prometheus File Service Discovery Error"
description: "How to fix Prometheus file-based service discovery errors"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- JSON or YAML file format incorrect
- File not readable by Prometheus process
- File path misconfigured
- File not updated after target changes

## How to Fix

Create proper file SD config:

```yaml
scrape_configs:
  - job_name: 'file-sd'
    file_sd_configs:
      - files:
          - '/etc/prometheus/targets/*.json'
        refresh_interval: 5m
```

JSON format:

```json
[
  {
    "targets": ["host1:8080", "host2:8080"],
    "labels": {
      "env": "production",
      "team": "backend"
    }
  }
]
```

## Examples

```bash
# Validate JSON file
python3 -m json.tool /etc/prometheus/targets/app.json

# Check file SD targets
curl http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | select(.discoveredLabels.__param_targets != null)'
```
