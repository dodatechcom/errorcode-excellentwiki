---
title: "[Solution] GCP Cloud Monitoring Alert Policy Error"
description: "Fix Cloud Monitoring alert policy errors. Resolve alert creation, notification channel, and metric filtering issues in GCP Monitoring."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP Cloud Monitoring Alert Policy Error

The Cloud Monitoring Alert Policy error occurs when alert policies fail to trigger, send notifications, or correctly interpret metric data.

## Common Causes

- Notification channel is not configured or verified
- Metric filter expression has syntax errors
- Alert condition duration is too short causing flapping
- Monitoring agent is not installed on the target VM
- Time series alignment period causes data gaps

## How to Fix

### 1. List alert policies
```bash
gcloud alpha monitoring policies list --format="table(name,displayName,enabled)"
```

### 2. Create an alert policy
```bash
gcloud alpha monitoring policies create \
  --display-name="High CPU Alert" \
  --condition-filter='metric.type="compute.googleapis.com/instance/cpu/utilization"' \
  --condition-threshold-value=0.9 \
  --condition-threshold-duration=300s \
  --notification-channels=CHANNEL_ID
```

### 3. Verify notification channels
```bash
gcloud alpha monitoring channels list --format="table(name,displayName,type)"
```

### 4. Check metric availability
```bash
gcloud monitoring time-series list \
  --filter='metric.type="compute.googleapis.com/instance/cpu/utilization"' \
  --interval-start-time=$(date -u -d "1 hour ago" +%Y-%m-%dT%H:%M:%SZ)
```

## Examples

### Create multi-condition alert
```bash
gcloud alpha monitoring policies create \
  --display-name="Disk and CPU Alert" \
  --condition-filter='metric.type="compute.googleapis.com/instance/cpu/utilization"' \
  --condition-threshold-value=0.9 \
  --condition-threshold-duration=300s \
  --notification-channels=CHANNEL_ID
```

### Add email notification channel
```bash
gcloud alpha monitoring channels create \
  --display-name="Ops Team Email" \
  --type=email \
  --channel-labels=email_address=ops@example.com
```

## Related Errors

- [GCP Cloud Monitoring Error]({{< relref "/cloud/gcp/gcp-cloud-monitoring-error" >}})
- [GCP Monitoring Alert Policy]({{< relref "/cloud/gcp/gcp-monitoring-alert-policy" >}})
