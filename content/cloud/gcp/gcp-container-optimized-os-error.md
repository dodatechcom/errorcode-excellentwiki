---
title: "[Solution] GCP Container-Optimized OS Error — update kernel errors"
description: "Fix GCP Container-Optimized OS errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 116
---

Container-Optimized OS errors occur when there are issues with OS updates, kernel modules, or container runtime on COS instances.

## Common Causes
- Automatic update reboots interrupting workloads
- Kernel module not available in COS
- Container image compatibility issues
- Limited package manager access in COS
- Systemd service configuration conflicts

## How to Fix

### 1. Check COS version
```bash
gcloud compute ssh INSTANCE --zone=ZONE --command="cat /etc/os-release"
```

### 2. List available COS images
```bash
gcloud compute images list --project=cos-cloud --format="table(name,description)"
```

### 3. Create instance with specific COS version
```bash
gcloud compute instances create INSTANCE \
  --zone=ZONE \
  --image-family=cos-stable \
  --image-project=cos-cloud \
  --metadata=cos-update-strategy=update_disabled
```

### 4. Disable automatic updates
```bash
gcloud compute instances add-metadata INSTANCE \
  --zone=ZONE \
  --metadata=cos-update-strategy=update_disabled
```

### 5. Check update status
```bash
gcloud compute ssh INSTANCE --zone=ZONE --command="sudo update_engine_client --status"
```

## Examples

### Create COS instance with updates disabled
```bash
gcloud compute instances create container-vm \
  --zone=us-central1-a \
  --machine-type=e2-standard-2 \
  --image-family=cos-stable \
  --image-project=cos-cloud \
  --metadata=cos-update-strategy=update_disabled \
  --tags=http-server
```

### Pull container image on COS
```bash
gcloud compute ssh container-vm --zone=us-central1-a --command="
  sudo docker pull gcr.io/my-project/my-app:latest
  sudo docker run -d -p 8080:8080 gcr.io/my-project/my-app:latest
"
```

## Related Errors
- [GCP GKE Error](/cloud/gcp/gcp-gke-error/)
- [GCP Cloud Run Error](/cloud/gcp/gcp-cloud-run-error/)
- [GCP Compute Engine Error](/cloud/gcp/gcp-compute-error/)