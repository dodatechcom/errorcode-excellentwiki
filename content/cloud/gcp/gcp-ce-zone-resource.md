---
title: "[Solution] GCP Zone Does Not Have Enough Resources"
description: "ZONE_DOES_NOT_HAVE_ENOUGH_RESOURCES when the zone lacks capacity."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Zone Does Not Have Enough Resources` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Zone has shortage of requested machine type
- GPU resources exhausted in the zone
- SSD/local SSD capacity fully allocated
- High demand period causes shortage

## How to Fix

### Try different zone

```bash
gcloud compute instances create my-vm --zone us-central1-b --machine-type e2-medium
```
### Try different machine type

```bash
gcloud compute machine-types list --zones=us-central1-a --format="table(name, guests, memoryMb)"
```
### List available zones

```bash
gcloud compute zones list --filter="region:us-central1" --format="table(name,status)"
```

## Examples

- Cannot create n2-standard-16 in us-central1-a
- GPU A100 not available in us-central1-a

## Related Errors

- [GCP Compute Error]({{< relref "/cloud/gcp/gcp-compute-error" >}}) -- General Compute errors
- [Quota Exceeded]({{< relref "/cloud/gcp/gcp-quota-exceeded" >}}) -- Quota
