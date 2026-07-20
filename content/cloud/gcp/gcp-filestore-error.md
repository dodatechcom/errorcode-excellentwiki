---
title: "[Solution] GCP Filestore Error — instance mount backup performance errors"
description: "Fix GCP Filestore errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 118
---

Filestore errors occur when there are issues with instance creation, NFS mounting, backup operations, or performance.

## Common Causes
- Instance capacity exceeded or insufficient IOPS
- NFS mount fails due to network/firewall issues
- Backup schedule conflicts with active operations
- Filestore API not enabled in project
- Zone does not support requested tier

## How to Fix

### 1. Enable Filestore API
```bash
gcloud services enable file.googleapis.com --project=PROJECT_ID
```

### 2. List Filestore instances
```bash
gcloud filestore instances list --location=ZONE
```

### 3. Create Filestore instance
```bash
gcloud filestore instances create INSTANCE_NAME \
  --location=ZONE \
  --tier=BASIC_HDD \
  --file-share=name=vol1,capacity=1TB \
  --network=name=NETWORK_NAME
```

### 4. Create backup
```bash
gcloud filestore backups create BACKUP_NAME \
  --instance=INSTANCE_NAME \
  --location=ZONE \
  --description="Daily backup"
```

### 5. Check instance performance
```bash
gcloud filestore instances describe INSTANCE_NAME --location=ZONE \
  --format="yaml(fileShares,performanceConfig)"
```

## Examples

### Mount Filestore on GCE instance
```bash
gcloud compute ssh VM_NAME --zone=ZONE --command="
  sudo apt-get update && sudo apt-get install -y nfs-common
  sudo mkdir -p /mnt/filestore
  sudo mount -o vers=3 IP_ADDRESS:/vol1 /mnt/filestore
  echo 'IP_ADDRESS:/vol1 /mnt/filestore nfs defaults 0 0' | sudo tee -a /etc/fstab
"
```

### Create high-performance instance
```bash
gcloud filestore instances create fast-store \
  --location=us-central1-a \
  --tier=ENTERPRISE \
  --file-share=name=data,capacity=10TB \
  --network=name=my-vpc
```

## Related Errors
- [GCP Cloud Storage Error](/cloud/gcp/gcp-storage-error/)
- [GCP GKE Error](/cloud/gcp/gcp-gke-error/)
- [GCP VPC Network Error](/cloud/gcp/gcp-vpc-error/)