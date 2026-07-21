---
title: "[Solution] GCP Compute Engine Snapshot Error"
description: "Fix Compute Engine snapshot errors. Troubleshoot snapshot creation failures, quotas, and disk snapshot issues in GCP Compute Engine."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP Compute Engine Snapshot Error

The Compute Engine Snapshot error occurs when disk snapshots cannot be created due to quota, disk state, or configuration issues.

## Common Causes

- Snapshot quota exceeded for the project
- Source disk has unflushed write buffers
- Source disk is larger than the snapshot size limit
- Disk encryption key is not accessible
- Snapshot is being created from a disk in use by a running VM

## How to Fix

### 1. Check snapshot quota
```bash
gcloud compute project-info describe --format="yaml(quotas)" \
  | grep -A2 "SNAPSHOTS"
```

### 2. Create a snapshot
```bash
gcloud compute disks snapshot DISK_NAME \
  --snapshot-names=SNAPSHOT_NAME \
  --zone=ZONE
```

### 3. Check snapshot status
```bash
gcloud compute snapshots describe SNAPSHOT_NAME \
  --format="yaml(status,diskSizeGb,storageBytes)"
```

### 4. Request quota increase
```bash
gcloud alpha quota requests submit \
  --service=compute.googleapis.com \
  --quota=SNAPSHOTS \
  --value=50
```

## Examples

### Snapshot with labels
```bash
gcloud compute disks snapshot my-disk \
  --snapshot-names=backup-$(date +%Y%m%d) \
  --labels=backup=daily,type=full \
  --zone=us-central1-a
```

### List snapshots
```bash
gcloud compute snapshots list --format="table(name,status,diskSizeGb)"
```

## Related Errors

- [GCP Snapshot Error]({{< relref "/cloud/gcp/gcp-snapshot-error" >}})
- [GCP CE Disk Not Found]({{< relref "/cloud/gcp/gcp-ce-disk-not-found" >}})
