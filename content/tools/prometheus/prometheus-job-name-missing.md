---
title: "[Solution] Prometheus job_name Missing"
description: "How to fix the missing job_name error in Prometheus scrape configuration"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- `job_name` field omitted from scrape_config
- `job_name` is empty or null
- Multiple scrape_configs sharing the same job_name

## How to Fix

Add a unique `job_name` to each scrape config:

```yaml
scrape_configs:
  - job_name: 'node-exporter'
    static_configs:
      - targets: ['localhost:9100']
  - job_name: 'app-metrics'
    static_configs:
      - targets: ['localhost:8080']
```

Verify no duplicate job names:

```bash
grep "job_name:" prometheus.yml | sort | uniq -d
```

Each scrape config must have a unique job name:

```bash
promtool check config prometheus.yml
```

## Examples

```yaml
# Valid scrape configs
scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']
  - job_name: 'cadvisor'
    static_configs:
      - targets: ['localhost:8080']
```

```bash
# Check for missing job_name
promtool check config prometheus.yml
```
