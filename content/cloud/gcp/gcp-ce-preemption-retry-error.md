---
title: "[Solution] GCP Compute Engine Preemption Retry Error"
description: "Fix Compute Engine preemption retry errors. Handle VM preemption recovery, retry logic, and spot instance management in GCP."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP Compute Engine Preemption Retry Error

The Compute Engine Preemption Retry error occurs when preemptible or spot VMs are terminated and retry mechanisms fail to properly recover workloads.

## Common Causes

- Workload does not handle SIGTERM gracefully
- No retry logic for preempted instances
- Dependent resources are not cleaned up after preemption
- State is lost when VM is terminated
- Managed instance group does not auto-heal

## How to Fix

### 1. Check preemption events
```bash
gcloud logging read "resource.type=gce_instance \
  AND jsonPayload.event_subtype=~\"preempt\"" \
  --limit=20
```

### 2. Enable auto-healing in MIG
```bash
gcloud compute instance-groups managed update MIG_NAME \
  --zone=ZONE \
  --auto-healing-policies=max-unavailable=1 \
  --initial-delay=300
```

### 3. Implement graceful shutdown handler
```python
import signal
import sys

def handle_sigterm(*args):
    save_work()
    sys.exit(0)

signal.signal(signal.SIGTERM, handle_sigterm)
```

### 4. Use managed instance groups with auto-restart
```bash
gcloud compute instance-groups managed set-autoscaling MIG_NAME \
  --zone=ZONE \
  --min-num-replicas=1 \
  --max-num-replicas=10
```

## Examples

### Monitor preemption rate
```bash
gcloud monitoring time-series list \
  --filter='metric.type="compute.googleapis.com/instance/preemption_count"' \
  --interval-start-time=$(date -u -d "24 hours ago" +%Y-%m-%dT%H:%M:%SZ)
```

### Create preemptible VM with startup script
```bash
gcloud compute instances create spot-vm \
  --zone=us-central1-a \
  --machine-type=e2-medium \
  --provisioning-model=SPOT \
  --metadata-from-file=startup-script=recovery.sh
```

## Related Errors

- [GCP Preemptible VM Error]({{< relref "/cloud/gcp/gcp-preemptible-vm-error" >}})
- [GCP CE Preemptible VM Eviction]({{< relref "/cloud/gcp/gcp-ce-preemptible-vm-eviction" >}})
