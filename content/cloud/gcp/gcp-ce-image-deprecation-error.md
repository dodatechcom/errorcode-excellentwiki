---
title: "[Solution] GCP Compute Engine Image Deprecation Error"
description: "Fix Compute Engine image deprecation errors. Migrate from deprecated OS images, update instance templates, and manage image lifecycle in GCP."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP Compute Engine Image Deprecation Error

The Compute Engine Image Deprecation error occurs when VM instances or templates reference deprecated OS images that are no longer available.

## Common Causes

- Instance references a deprecated Debian or CentOS image
- Instance template uses an old image family
- Automated deployment uses hardcoded image paths
- Image project is incorrect or image was deprecated
- Custom image was removed from the project

## How to Fix

### 1. List available images
```bash
gcloud compute images list --project=debian-cloud \
  --filter="status=READY" --format="table(name,family)"
```

### 2. Update to latest image
```bash
gcloud compute instances set-image VM_NAME \
  --image-family=debian-12 \
  --image-project=debian-cloud \
  --zone=ZONE
```

### 3. Update instance template
```bash
gcloud compute instance-templates update TEMPLATE_NAME \
  --image-family=debian-12 \
  --image-project=debian-cloud
```

### 4. Find deprecated images
```bash
gcloud compute images list --filter="status=DEPRECATED" \
  --format="table(name,family)"
```

## Examples

### List current image families
```bash
gcloud compute images list --project=debian-cloud --format="table(family)"
```

### Update MIG template
```bash
gcloud compute instance-groups managed rolling-update start MIG_NAME \
  --version=template=NEW_TEMPLATE \
  --zone=ZONE
```

## Related Errors

- [GCP Image Not Found]({{< relref "/cloud/gcp/gcp-image-not-found" >}})
- [GCP Instance Template]({{< relref "/cloud/gcp/gcp-instance-template" >}})
