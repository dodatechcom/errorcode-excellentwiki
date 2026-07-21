---
title: "[Solution] GCP Compute Engine SSH Key Error"
description: "Fix Compute Engine SSH key errors. Resolve SSH key generation, metadata, and OS Login access issues for GCP VM instances."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP Compute Engine SSH Key Error

The Compute Engine SSH Key error occurs when users cannot SSH into a VM instance due to SSH key configuration or metadata issues.

## Common Causes

- SSH key is not added to project or instance metadata
- OS Login is enabled but user is not in OS Login profile
- SSH key has incorrect permissions or format
- Instance does not have SSH access via firewall rules
- Project-wide SSH keys are disabled

## How to Fix

### 1. Generate SSH key
```bash
ssh-keygen -t rsa -b 4096 -f ~/.ssh/gcp_key -C user@example.com
```

### 2. Add SSH key to project metadata
```bash
gcloud compute project-info describe --format="value(commonInstanceMetadata.items[key])"
```

### 3. SSH into instance
```bash
gcloud compute ssh VM_NAME --zone=ZONE --ssh-key-file=~/.ssh/gcp_key
```

### 4. Add SSH key to instance metadata
```bash
gcloud compute instances add-metadata VM_NAME \
  --zone=ZONE \
  --metadata=ssh-keys="user:$(cat ~/.ssh/gcp_key.pub)"
```

### 5. Enable OS Login
```bash
gcloud compute project-info add-metadata \
  --metadata=enable-oslogin=TRUE
```

## Examples

### SSH with specific key
```bash
gcloud compute ssh VM_NAME --zone=ZONE --ssh-key-file=~/.ssh/custom_key
```

### Check OS Login profile
```bash
gcloud compute os-login profiles describe --project=PROJECT_ID
```

## Related Errors

- [GCP SSH Connection Error]({{< relref "/cloud/gcp/gcp-ssh-connection-error" >}})
- [GCP Serial Console]({{< relref "/cloud/gcp/gcp-serial-console" >}})
