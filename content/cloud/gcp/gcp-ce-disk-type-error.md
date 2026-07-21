---
title: "[Solution] GCP Compute Engine Disk Type Error"
description: "Fix Compute Engine disk type errors. Resolve pd-standard, pd-ssd, pd-balanced, and local SSD disk type issues in GCP."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP Compute Engine Disk Type Error

The Compute Engine Disk Type error occurs when creating or using disks with incompatible or unavailable disk types.

## Common Causes

- Disk type is not available in the target zone
- Local SSD is not supported by the instance machine type
- pd-balanced requires specific minimum disk size
- Image is not compatible with the requested disk type
- Zone does not support the requested disk type

## How to Fix

### 1. Check available disk types
```bash
gcloud compute disk-types list --zones=ZONE --format="table(name,zone)"
```

### 2. Create disk with correct type
```bash
gcloud compute disks create my-disk \
  --zone=ZONE \
  --size=100GB \
  --type=pd-ssd
```

### 3. Change disk type
```bash
gcloud compute disks set-disk-type my-disk \
  --zone=ZONE \
  --disk-type=pd-balanced
```

### 4. Check minimum disk size
```bash
gcloud compute disk-types describe pd-balanced --zone=ZONE
```

## Examples

### Create local SSD
```bash
gcloud compute instances create my-vm \
  --zone=ZONE \
  --machine-type=n2-standard-4 \
  --local-ssd=interface=NVME,size=375 \
  --local-ssd=interface=NVME,size=375
```

### List disk types in zone
```bash
gcloud compute disk-types list --zones=us-central1-a \
  --format="table(name,defaultDiskSizeGb)"
```

## Related Errors

- [GCP Disk Create Error]({{< relref "/cloud/gcp/gcp-disk-create-error" >}})
- [GCP CE Disk Not Found]({{< relref "/cloud/gcp/gcp-ce-disk-not-found" >}})
