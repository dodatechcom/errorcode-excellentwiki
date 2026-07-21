---
title: "[Solution] GCP Instance Template Error -- template creation disk network errors"
description: "Fix GCP Instance Template errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 114
---

Instance Template errors occur when there are issues with template creation, disk configuration, or network settings.

## Common Causes
- Invalid source image or image family
- Disk size exceeds maximum for selected image
- Network interface references non-existent VPC or subnet
- Machine type not available in region
- Confidential compute configuration conflict

## How to Fix

### 1. List instance templates
```bash
gcloud compute instance-templates list
```

### 2. Describe template details
```bash
gcloud compute instance-templates describe TEMPLATE_NAME
```

### 3. Create instance template
```bash
gcloud compute instance-templates create TEMPLATE_NAME \
  --machine-type=MACHINE_TYPE \
  --image-family=IMAGE_FAMILY \
  --image-project=PROJECT \
  --boot-disk-size=50GB \
  --network=NETWORK_NAME \
  --subnet=SUBNET_NAME \
  --tags=TAG1,TAG2
```

### 4. Create template with custom disk
```bash
gcloud compute instance-templates create TEMPLATE_NAME \
  --machine-type=e2-standard-4 \
  --create-disk=name=data-disk,size=200GB,type=pd-ssd,auto-delete=yes \
  --image-family=debian-11 \
  --image-project=debian-cloud
```

### 5. Delete outdated template
```bash
gcloud compute instance-templates delete OLD_TEMPLATE --quiet
```

## Examples

### Create template for web servers
```bash
gcloud compute instance-templates create web-template \
  --machine-type=e2-standard-2 \
  --image-family=ubuntu-2204-lts \
  --image-project=ubuntu-os-cloud \
  --boot-disk-size=30GB \
  --network=prod-vpc \
  --subnet=web-subnet \
  --tags=http-server,https-server \
  --metadata=startup-script='#!/bin/bash
apt-get update && apt-get install -y nginx'
```

### Create template with multiple disks
```bash
gcp compute instance-templates create db-template \
  --machine-type=e2-standard-8 \
  --image-family=debian-11 \
  --create-disk=name=data,size=500GB,type=pd-ssd \
  --create-disk=name=logs,size=100GB,type=pd-standard
```

## Related Errors
- [GCP Compute Engine Error](/cloud/gcp/gcp-compute-error/)
- [GCP VPC Network Error](/cloud/gcp/gcp-vpc-error/)
- [GCP Sole Tenant Error](/cloud/gcp/gcp-sole-tenant-error/)