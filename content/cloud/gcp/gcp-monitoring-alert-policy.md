---
title: "[Solution] GCP Monitoring Alert Policy Error"
description: "INVALID_ARGUMENT when alert policy operations fail."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Monitoring Alert Policy Error` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Alert policy name is incorrect
- Notification channel does not exist
- Condition expression is invalid
- Alert policy is disabled

## How to Fix

### List alert policies

```bash
gcloud monitoring policies list --project my-project
```
### Check alert policy

```bash
gcloud monitoring policies describe my-alert --project my-project
```
### Create alert policy

```bash
gcloud monitoring policies create --project my-project --display-name="My Alert" --notification-channels=my-channel --condition-filter="metric.type="compute.googleapis.com/instance/cpu/utilization""
```

## Examples

- Alert policy references deleted notification channel
- Condition filter uses invalid metric type

## Related Errors

- [GCP Monitoring Error]({{< relref "/cloud/gcp/gcp-cloud-monitoring-error" >}}) -- General Monitoring errors
- [Workspace Not Found]({{< relref "/cloud/gcp/gcp-monitoring-workspace-not-found" >}}) -- Workspace not found
