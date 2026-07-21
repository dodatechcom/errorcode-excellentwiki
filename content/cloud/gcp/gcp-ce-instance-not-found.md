---
title: "[Solution] GCP Compute Engine Instance Not Found"
description: "NOT_FOUND when the specified VM instance does not exist."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Compute Engine Instance Not Found` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Instance name is incorrect
- Instance was deleted
- Instance in different project
- Instance in different zone

## How to Fix

### List instances

```bash
gcloud compute instances list
```
### Check instance

```bash
gcloud compute instances describe my-vm --zone us-central1-a
```
### Create instance

```bash
gcloud compute instances create my-vm --zone us-central1-a --machine-type e2-medium
```

## Examples

- Instance my-vm not found in zone us-central1-a
- Instance deleted but startup script still references it

## Related Errors

- [GCP Compute Error]({{< relref "/cloud/gcp/gcp-compute-error" >}}) -- General Compute errors
- [Zone Resource]({{< relref "/cloud/gcp/gcp-ce-zone-resource" >}}) -- Zone resource issues
