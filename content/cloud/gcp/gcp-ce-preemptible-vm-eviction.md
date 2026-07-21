---
title: "[Solution] GCP Compute Engine Preemptible VM Eviction"
description: "Fix preemptible VM eviction errors. Handle GCP preemptible instance shutdown, check, and workload migration for cost-efficient compute."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP Compute Engine Preemptible VM Eviction

The Preemptible VM Eviction error occurs when a preemptible (spot) VM instance is terminated by Google Cloud, often mid-workload, with a 30-second warning.

## Common Causes

- Preemptible VM has been running for over 24 hours
- Google Cloud needs the capacity for other workloads
- Instance was not designed for graceful shutdown handling
- Workload checkpoints are not being saved
- VM has no shutdown handler to save state

## How to Fix

### 1. Check preemptible VM status
```bash
gcloud compute instances describe VM_NAME --zone=ZONE \
  --format="yaml(scheduling,metadata.items)"
```

### 2. Handle shutdown signal
```python
import signal, sys

def shutdown_handler(signum, frame):
    save_checkpoint()
    sys.exit(0)

signal.signal(signal.SIGTERM, shutdown_handler)
```

### 3. Use managed instance groups for auto-restart
```bash
gcloud compute instance-groups managed create MIG_NAME \
  --base-instance-name=app \
  --template=TEMPLATE_NAME \
  --size=5 \
  --zone=ZONE
```

### 4. Set up checkpoint to Cloud Storage
```python
import json
from google.cloud import storage

def save_checkpoint():
    state = {"progress": get_progress()}
    client = storage.Client()
    bucket = client.bucket("checkpoint-bucket")
    blob = bucket.blob("checkpoint.json")
    blob.upload_from_string(json.dumps(state))
```

## Examples

### Deploy with graceful shutdown
```bash
gcloud compute instances create preemptible-vm \
  --zone=us-central1-a \
  --machine-type=e2-medium \
  --provisioning-model=SPOT \
  --metadata-from-file=startup-script=startup.sh,shutdown-script=shutdown.sh
```

### Monitor eviction events
```bash
gcloud logging read "resource.type=gce_instance \
  AND jsonPayload.event_subtype=~\"preempted\"" \
  --limit=20
```

## Related Errors

- [GCP Preemptible VM Error]({{< relref "/cloud/gcp/gcp-preemptible-vm-error" >}})
- [GCP CE Instance Not Found]({{< relref "/cloud/gcp/gcp-ce-instance-not-found" >}})
