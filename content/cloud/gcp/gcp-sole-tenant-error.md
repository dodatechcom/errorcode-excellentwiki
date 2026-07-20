---
title: "[Solution] GCP Sole Tenant Error — node affinity host errors"
description: "Fix GCP Sole Tenant errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 109
---

Sole Tenant errors occur when there are issues with sole-tenant node groups, host affinity policies, or dedicated host configurations.

## Common Causes
- Sole tenant node group creation failed due to insufficient capacity
- Host affinity policy conflict with existing VMs
- Instance template incompatible with sole tenant node
- Node group size exceeds maximum limit
- Zone does not support sole tenant nodes

## How to Fix

### 1. List sole tenant node groups
```bash
gcloud compute sole-tenant node-groups list --zone=ZONE
```

### 2. Describe node group
```bash
gcloud compute sole-tenant node-groups describe NODE_GROUP_NAME --zone=ZONE
```

### 3. Create sole tenant node group
```bash
gcloud compute sole-tenant node-groups create NODE_GROUP_NAME \
  --zone=ZONE \
  --node-template=NODE_TEMPLATE_NAME \
  --size=2
```

### 4. Create node template
```bash
gcloud compute sole-tenant node-templates create NODE_TEMPLATE_NAME \
  --region=REGION \
  --node-type-cpu=NODE_TYPE \
  --node-affinity-labels=key=value
```

### 5. Set host affinity policy
```bash
gcloud compute sole-tenant node-groups update NODE_GROUP_NAME \
  --zone=ZONE \
  --node-affinity-labels=key=value
```

## Examples

### Create sole tenant node group for compliance
```bash
gcloud compute sole-tenant node-templates create compliance-template \
  --region=us-central1 \
  --node-type-cpu=n2-node-60-128

gcloud compute sole-tenant node-groups create compliance-nodes \
  --zone=us-central1-a \
  --node-template=compliance-template \
  --size=3
```

### Attach VM to sole tenant node
```bash
gcloud compute instances create dedicated-vm \
  --zone=us-central1-a \
  --machine-type=n2-custom-8-32 \
  --node-affinity-labels=compute.googleapis.com sole-tenant-node-group:compliance-nodes
```

## Related Errors
- [GCP Compute Engine Error](/cloud/gcp/gcp-compute-error/)
- [GCP Instance Template Error](/cloud/gcp/gcp-instance-template-error/)
- [GCP GPU Error](/cloud/gcp/gcp-gpu-error/)