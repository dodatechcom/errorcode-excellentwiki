---
title: "[Solution] GCP Cloud Monitoring Error -- metric dashboard alert channel errors"
description: "Fix GCP Cloud Monitoring errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 147
---

Cloud Monitoring errors occur when there are issues with metrics collection, dashboard rendering, alert policies, or notification channels.

## Common Causes
- Custom metric descriptor creation fails
- Dashboard JSON schema invalid
- Alert policy condition threshold misconfigured
- Notification channel unreachable
- Monitoring API not enabled

## How to Fix

### 1. Enable Monitoring API
```bash
gcloud services enable monitoring.googleapis.com --project=PROJECT_ID
```

### 2. List alert policies
```bash
gcloud monitoring policies list --format="table(name,displayName,combiner)"
```

### 3. Create alert policy
```bash
gcloud monitoring policies create \
  --notification-channels=CHANNEL_ID \
  --condition-display-name="High CPU" \
  --condition-filter='metric.type="compute.googleapis.com/instance/cpu/utilization"' \
  --condition-threshold-value=0.8 \
  --condition-threshold-duration=300s \
  --display-name="CPU Alert"
```

### 4. List dashboards
```bash
gcloud monitoring dashboards list --format="table(name,displayName)"
```

### 5. Create uptime check
```bash
gcloud monitoring uptime create \
  --display-name="My Website" \
  --resource-type=url \
  --uri="https://example.com" \
  --check-interval=300s
```

## Examples

### Create custom metric
```bash
gcloud monitoring metrics-scopes create \
  --project=PROJECT_ID

gcloud alpha monitoring time-series create \
  --metric="custom.googleapis.com/my_metric" \
  --resource-type=global \
  --value-type=DOUBLE \
  --points-value=1.0
```

### List notification channels
```bash
gcloud monitoring channels list --format="table(name,type,displayName)"
```

## Related Errors
- [GCP Cloud Logging Error](/cloud/gcp/gcp-cloud-logging-error/)
- [GCP Error Reporting Error](/cloud/gcp/gcp-error-reporting-error/)
- [GCP Cloud Trace Error](/cloud/gcp/gcp-cloud-trace-error/)