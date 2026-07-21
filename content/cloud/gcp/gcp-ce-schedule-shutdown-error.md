---
title: "[Solution] GCP Compute Engine Scheduled Shutdown Error"
description: "Fix Compute Engine scheduled shutdown errors. Resolve instance auto-shutdown, scheduling, and lifecycle management issues in GCP."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP Compute Engine Scheduled Shutdown Error

The Compute Engine Scheduled Shutdown error occurs when VM instances fail to start or stop according to their configured schedules.

## Common Causes

- Startup/shutdown script has errors or hangs
- Instance metadata does not contain correct schedule
- Required APIs are not enabled for lifecycle management
- Shutdown script takes longer than the allowed timeout
- IAM permissions prevent script from executing

## How to Fix

### 1. Check instance metadata
```bash
gcloud compute instances describe VM_NAME --zone=ZONE \
  --format="yaml(metadata.items)"
```

### 2. Add startup script
```bash
gcloud compute instances add-metadata VM_NAME \
  --zone=ZONE \
  --metadata-from-file=startup-script=startup.sh
```

### 3. Add shutdown script
```bash
gcloud compute instances add-metadata VM_NAME \
  --zone=ZONE \
  --metadata-from-file=shutdown-script=shutdown.sh
```

### 4. Check script execution logs
```bash
gcloud logging read "resource.type=gce_instance \
  AND jsonPayload.event_type=startup" \
  --limit=20
```

## Examples

### Startup script example
```bash
#!/bin/bash
apt-get update
apt-get install -y nginx
systemctl start nginx
```

### Shutdown script example
```bash
#!/bin/bash
systemctl stop nginx
echo "VM shutting down at $(date)" >> /var/log/shutdown.log
```

## Related Errors

- [GCP CE Instance Not Found]({{< relref "/cloud/gcp/gcp-ce-instance-not-found" >}})
- [GCP Instance Stop Error]({{< relref "/cloud/gcp/gcp-instance-stop-error" >}})
