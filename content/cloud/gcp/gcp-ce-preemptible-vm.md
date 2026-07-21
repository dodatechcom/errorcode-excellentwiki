---
title: "[Solution] GCP Preemptible VM Error"
description: "PREEMPTED when a preemptible VM instance is terminated."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Preemptible VM Error` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Instance was preempted (max 24 hours)
- Maintenance event caused termination
- Preemptible instance group was scaled down
- Instance was started as preemptible

## How to Fix

### Check preemptible status

```bash
gcloud compute instances describe my-vm --zone us-central1-a --format="value(scheduling.preemptible)"
```
### Create non-preemptible

```bash
gcloud compute instances create my-vm --zone us-central1-a --no-preemptible
```
### Check preemptible quota

```bash
gcloud compute regions describe us-central1 --format="table(quotas.metric,quotas.limit,quotas.usage)"
```

## Examples

- Instance preempted after 12 hours of runtime
- Preemptible instance lost due to maintenance event

## Related Errors

- [GCP Compute Error]({{< relref "/cloud/gcp/gcp-compute-error" >}}) -- General Compute errors
- [Spot Instance]({{< relref "/cloud/gcp/gcp-ce-spot-instance" >}}) -- Spot instances
