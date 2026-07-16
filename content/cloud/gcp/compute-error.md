---
title: "GCP Compute Engine: The Zone Does Not Have Enough Resources"
description: "Compute Engine: The zone does not have enough resources — Fix Google Cloud zone resource exhaustion."
cloud: ["gcp"]
error-types: ["quota-error"]
severities: ["error"]
tags: ["gcp", "compute", "zone", "resources", "insufficient", "capacity", "machine-type"]
weight: 5
---

The `The zone does not have enough resources` error occurs when a Google Cloud zone has insufficient capacity for the requested resource (e.g., specific machine type, GPU, or SSD). This is a temporary capacity issue, not a quota limit.

## Common Causes

- The zone has a shortage of the requested machine type (e.g., `n2-standard-8`)
- GPU resources are exhausted in the zone
- SSD/local SSD capacity is fully allocated
- High demand period (e.g., Black Friday) causes temporary capacity shortages

## How to Fix

Try a different zone:

```bash
# List available zones for a region
gcloud compute zones list --filter="region:us-central1" \
  --format="table(name,status)"

# Create in a different zone
gcloud compute instances create my-vm \
  --zone=us-central1-b \
  --machine-type=e2-medium
```

Try a different machine type:

```bash
# List available machine types in the zone
gcloud compute machine-types list \
  --zones=us-central1-a \
  --format="table(name, guests, memoryMb, imageFamily)"
```

Use a committed use discount for guaranteed capacity:

```bash
gcloud compute instances create my-vm \
  --zone=us-central1-a \
  --machine-type=n2-standard-4 \
  --maintenance-policy=MIGRATE
```

Set up a managed instance group for automatic zone failover:

```bash
gcloud compute instance-groups managed create my-mig \
  --zone=us-central1-a \
  --template=my-template \
  --size=2
```

## Examples

- Cannot create `n2-standard-16` in `us-central1-a` — try `us-central1-b`
- GPU (A100) not available in `us-central1-a` — check `us-central1-c` or `us-central1-f`
- Local SSD capacity exhausted — use a persistent SSD disk instead

## Related Errors

- [GCP Quota Exceeded]({{< relref "/cloud/gcp/quota-exceeded2" >}}) — quota limits (different from capacity).
- [GCP Instance Not Found]({{< relref "/cloud/gcp/instance-not-found2" >}}) — instance not found.
- [AWS Instance Limit]({{< relref "/cloud/aws/ec2-quota" >}}) — AWS equivalent.
