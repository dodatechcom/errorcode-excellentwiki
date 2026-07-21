---
title: "[Solution] GCP Compute Engine Instance Template Creation Error"
description: "Fix instance template creation errors. Resolve Compute Engine template conflicts, disk, and network configuration issues in GCP."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP Compute Engine Instance Template Creation Error

The Instance Template Creation error occurs when creating Compute Engine instance templates fails due to invalid configuration, disk, or network settings.

## Common Causes

- Template name already exists in the project
- Source image does not exist or is not accessible
- Network interface references a non-existent VPC or subnet
- Disk size is below minimum or exceeds quota
- Machine type is not available in the specified zone

## How to Fix

### 1. List existing templates
```bash
gcloud compute instance-templates list --format="table(name,status)"
```

### 2. Create instance template
```bash
gcloud compute instance-templates create my-template \
  --machine-type=e2-standard-4 \
  --image-family=debian-12 \
  --image-project=debian-cloud \
  --boot-disk-size=50GB \
  --network=default
```

### 3. Check available machine types
```bash
gcloud compute machine-types list --zones=ZONE \
  --format="table(name,zone,guestCpus)"
```

### 4. Verify image availability
```bash
gcloud compute images list --project=debian-cloud \
  --filter="name~debian-12" --format="table(name,status)"
```

## Examples

### Create template with SSD
```bash
gcloud compute instance-templates create fast-template \
  --machine-type=n2-standard-8 \
  --image-family=ubuntu-2204-lts \
  --image-project=ubuntu-os-cloud \
  --boot-disk-type=pd-ssd \
  --boot-disk-size=200GB \
  --tags=web-server
```

### Delete old template
```bash
gcloud compute instance-templates delete OLD_TEMPLATE --quiet
```

## Related Errors

- [GCP Instance Template]({{< relref "/cloud/gcp/gcp-instance-template" >}})
- [GCP Image Not Found]({{< relref "/cloud/gcp/gcp-image-not-found" >}})
