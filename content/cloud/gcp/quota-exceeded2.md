---
title: "GCP Quota Exceeded: Quota Exceeded for Quota"
description: "Quota exceeded: Quota exceeded for quota — Fix Google Cloud resource quota limits."
error-types: ["quota-error"]
severities: ["error"]
weight: 5
---

The `Quota exceeded: Quota exceeded for quota` error occurs when a Google Cloud project exceeds its allocated quota for a specific resource (e.g., CPUs, IPs, or API requests). This prevents new resource creation until the quota is increased or resources are freed.

## Common Causes

- Too many VMs running in a zone/region, exhausting the CPU quota
- Default quotas are conservative for new projects
- Shared project across teams with no centralized quota management
- Resources are created in a zone where the quota is lower than other zones

## How to Fix

Check current quota usage:

```bash
gcloud compute project-info describe --project=my-project \
  --format="value(quotas[].{Metric:metric, Usage:usage, Limit:limit})"
```

View quota for a specific resource:

```bash
gcloud compute regions describe us-central1 \
  --format="value(quotas[].{Metric:metric, Usage:usage, Limit:limit})"
```

Request a quota increase:

```bash
gcloud compute project-info add-metadata \
  --project=my-project \
  --metadata="quota-override-cpus=100"
```

Or through the console:

```bash
gcloud alpha services quota increase \
  --service=compute.googleapis.com \
  --metric=CPUS \
  --region=us-central1 \
  --value=100
```

Delete unused resources:

```bash
# List non-running instances
gcloud compute instances list --filter="status!=RUNNING"

# Delete stopped instances
gcloud compute instances delete stopped-vm --zone=us-central1-a
```

## Examples

- Cannot create more than 8 CPU instances in `us-central1-a` because the default quota is 8
- Project exceeds the 230 external IP address limit for a region
- Cloud Functions deployment fails because the project has reached 1000 function instances

## Related Errors

- [GCP Compute Error]({{< relref "/cloud/gcp/compute-error" >}}) — not enough resources in zone.
- [GCP Permission Denied]({{< relref "/cloud/gcp/permission-denied10" >}}) — permission issues.
- [Azure Quota Exceeded]({{< relref "/cloud/azure/quota-exceeded" >}}) — Azure equivalent.
