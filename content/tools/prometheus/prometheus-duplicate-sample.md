---
title: "[Solution] Prometheus Duplicate Sample Error"
description: "How to fix Prometheus duplicate sample errors during metric ingestion"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Two targets writing the same metric with identical labels
- Misconfigured relabeling creating duplicate series
- Federation or remote write creating duplicate data
- Multiple Prometheus instances scraping the same target

## How to Fix

Check for duplicate series:

```bash
promtool tsdb analyze prometheus-data/
```

Review relabel configs:

```yaml
scrape_configs:
  - job_name: 'app'
    relabel_configs:
      - source_labels: [__address__]
        target_label: instance
        action: replace
```

Use unique identifiers in relabeling:

```yaml
    relabel_configs:
      - source_labels: [__meta_consul_tags]
        regex: '.*,prometheus,.*'
        target_label: __param_target
```

## Examples

```bash
# Check for duplicate targets
curl -s http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | .labels.instance' | sort | uniq -d

# Query for duplicate metric names
curl -s 'http://localhost:9090/api/v1/query?query=count by (__name__)({__name__!=""})' | jq '.data.result[] | select(.value[1] > "1")'
```
