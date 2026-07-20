---
title: "[Solution] GCP Preemptible VM Error — Spot VM preemption restart errors"
description: "Fix GCP Preemptible/Spot VM errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 110
---

Preemptible/Spot VM errors occur when instances are preempted before expected or fail to restart after preemption events.

## Common Causes
- Spot VM preempted due to capacity demand
- Preemption notice not handled gracefully
- Startup script failed after restart
- Stateful workloads lost after preemption
- Maximum runtime limit exceeded (24 hours for preemptible)

## How to Fix

### 1. Check preemption status
```bash
gcloud compute instances describe INSTANCE_NAME \
  --zone=ZONE \
  --format="yaml(scheduling,metadata)"
```

### 2. List preempted instances
```bash
gcloud compute instances list --filter="status=TERMINATED AND scheduling.preemptionPro=TERMINATED"
```

### 3. Create Spot VM with restart policy
```bash
gcloud compute instances create SPOT_VM_NAME \
  --zone=ZONE \
  --machine-type=MACHINE_TYPE \
  --provisioning-model=SPOT \
  --instance-termination-action=STOP \
  --restart-on-failure
```

### 4. Configure graceful shutdown handler
```bash
gcloud compute instances create VM_NAME \
  --zone=ZONE \
  --provisioning-model=SPOT \
  --metadata=startup-script='#!/bin/bash
echo "Handling shutdown..."
# Save state to Cloud Storage
gsutil cp /tmp/state gs://my-bucket/state/
shutdown -h +0.5'
```

### 5. Use managed instance group for auto-restart
```bash
gcloud compute instance-groups managed create MANAGED_GROUP \
  --zone=ZONE \
  --template=SPOT_TEMPLATE \
  --size=3 \
  --auto-restart
```

## Examples

### Create fault-tolerant Spot VMs
```bash
gcloud compute instances create spot-worker-1 \
  --zone=us-central1-a \
  --machine-type=e2-standard-4 \
  --provisioning-model=SPOT \
  --instance-termination-action=STOP \
  --metadata-from-file=startup-script=handle-preemption.sh
```

### Check preempted VMs
```bash
gcloud compute instances list \
  --filter="status=TERMINATED" \
  --format="table(name,zone,status,scheduling.provisioningModel)"
```

## Related Errors
- [GCP Compute Engine Error](/cloud/gcp/gcp-compute-error/)
- [GCP Instance Template Error](/cloud/gcp/gcp-instance-template-error/)
- [GCP GPU Error](/cloud/gcp/gcp-gpu-error/)