---
title: "[Solution] GCP Compute Engine Disk Not Found"
description: "NOT_FOUND when the specified disk does not exist."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Compute Engine Disk Not Found` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Disk name is incorrect
- Disk was deleted
- Disk in different project
- Disk in different zone

## How to Fix

### List disks

```bash
gcloud compute disks list
```
### Check disk

```bash
gcloud compute disks describe my-disk --zone us-central1-a
```
### Create disk

```bash
gcloud compute disks create my-disk --zone us-central1-a --size 100GB --type pd-ssd
```

## Examples

- Disk my-disk not found in zone us-central1-a
- Disk deleted but VM still references it

## Related Errors

- [GCP Compute Error]({{< relref "/cloud/gcp/gcp-compute-error" >}}) -- General Compute errors
- [Disk Resize]({{< relref "/cloud/gcp/gcp-ce-disk-resize" >}}) -- Disk resize
