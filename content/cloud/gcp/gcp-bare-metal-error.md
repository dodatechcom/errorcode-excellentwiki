---
title: "[Solution] GCP Bare Metal Solution Error — instance network storage errors"
description: "Fix GCP Bare Metal Solution errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 108
---

Bare Metal Solution errors occur when there are issues with physical server instances, storage volumes, or dedicated network connections.

## Common Causes
- Bare Metal API not enabled in project
- Insufficient capacity in target zone
- Network attachment not properly configured
- Storage volume not mounted or formatted
- Dedicated host not available in region

## How to Fix

### 1. Enable Bare Metal Solution API
```bash
gcloud services enable baremetalsolution.googleapis.com --project=PROJECT_ID
```

### 2. List Bare Metal instances
```bash
gcloud bare-metal instances list --location=ZONE
```

### 3. Describe instance details
```bash
gcloud bare-metal instances describe INSTANCE_NAME --location=ZONE
```

### 4. Create a new instance
```bash
gcloud bare-metal instances create INSTANCE_NAME \
  --location=ZONE \
  --machine-type=MACHINE_TYPE \
  --network=NETWORK_NAME \
  --os-image=OS_IMAGE
```

### 5. Manage storage volumes
```bash
gcloud bare-metal volumes list --location=ZONE
gcloud bare-metal volumes create VOLUME_NAME \
  --location=ZONE \
  --size=100Gi \
  --type=SSD
```

## Examples

### Provision Bare Metal instance
```bash
gcloud bare-metal instances create my-server \
  --location=us-central1-b \
  --machine-type=64x10 \
  --network=my-vpc \
  --os-image=rhel8
```

### List available network attachments
```bash
gcloud bare-metal networks list --location=us-central1
```

## Related Errors
- [GCP Compute Engine Error](/cloud/gcp/gcp-compute-error/)
- [GCP VPC Network Error](/cloud/gcp/gcp-vpc-error/)
- [GCP Filestore Error](/cloud/gcp/gcp-filestore-error/)