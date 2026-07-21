---
title: "[Solution] GCP Autoscaler"
description: "AutoscalerError for autoscaling."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Autoscaler` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Cool-down period not set
- Metric not supported for autoscaling
- Max instances < min instances

## How to Fix

### Update autoscaler

```bash
gcloud compute instance-groups managed set-autoscaling myGroup --max-num-replicas=10 --min-num-replicas=2
```

## Examples

- Example scenario: cool-down period not set
- Example scenario: metric not supported for autoscaling
- Example scenario: max instances < min instances

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
