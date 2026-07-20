---
title: "[Solution] GCP Sole Tenant Node Error — node group reservation errors"
description: "Fix GCP Sole Tenant Node errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 111
---

Sole Tenant Node errors occur when there are issues with node group reservations, capacity planning, or node management.

## Common Causes
- Node group size exceeds available capacity
- Reservation already consumed by another node group
- Node template type unavailable in zone
- Active VMs preventing node group deletion
- Auto-scaling limits reached for node group

## How to Fix

### 1. List node groups and capacity
```bash
gcloud compute sole-tenant node-groups list --zone=ZONE
gcloud compute sole-tenant node-types list --zone=ZONE
```

### 2. Check node group details
```bash
gcloud compute sole-tenant node-groups describe NODE_GROUP --zone=ZONE \
  --format="yaml(name,size,autoscalingPolicy,nodeType)"
```

### 3. Resize node group
```bash
gcloud compute sole-tenant node-groups resize NODE_GROUP \
  --zone=ZONE \
  --size=5
```

### 4. Create reservation for sole tenant
```bash
gcloud compute reservations create RESERVATION_NAME \
  --zone=ZONE \
  --requirements=vm-count=2,vm-type=NODE_TYPE \
  --require-specific
```

### 5. Delete empty node group
```bash
gcloud compute sole-tenant node-groups delete NODE_GROUP \
  --zone=ZONE --quiet
```

## Examples

### Create node group with autoscaling
```bash
gcloud compute sole-tenant node-groups create autoscale-group \
  --zone=us-central1-a \
  --node-template=prod-template \
  --size=2 \
  --autoscaler-mode=only-scale-out \
  --min-nodes=1 \
  --max-nodes=10
```

### Check available node types
```bash
gcloud compute sole-tenant node-types list \
  --zone=us-central1-a \
  --format="table(name,cpu,scratchDisks,localSsd)"
```

## Related Errors
- [GCP Sole Tenant Error](/cloud/gcp/gcp-sole-tenant-error/)
- [GCP Compute Engine Error](/cloud/gcp/gcp-compute-error/)
- [GCP Commitment Error](/cloud/gcp/gcp-commitment-error/)