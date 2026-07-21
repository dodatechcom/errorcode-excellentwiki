---
title: "[Solution] Prometheus GCE Service Discovery Error"
description: "How to fix Prometheus GCE-based service discovery errors"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- GCP credentials not configured
- Wrong GCP project ID
- Firewall rules blocking scrape port
- Instances not properly labeled

## How to Fix

Configure GCE SD:

```yaml
scrape_configs:
  - job_name: 'gce'
    gce_sd_configs:
      - project: my-gcp-project
        zone: us-central1-a
        filter: 'labels.prometheus=true'
```

## Examples

```bash
# Test GCP credentials
gcloud auth application-default print-access-token

# List GCE instances
gcloud compute instances list --filter="labels.prometheus=true"

# Check discovered targets
curl http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | select(.discoveredLabels.__meta_gce_label_prometheus != null)'
```
