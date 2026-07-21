---
title: "[Solution] GCP Compute Engine External IP Error"
description: "Fix Compute Engine external IP errors. Resolve IP allocation, static IP assignment, and external access issues in GCP Compute Engine."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP Compute Engine External IP Error

The Compute Engine External IP error occurs when VM instances cannot obtain or retain external IP addresses due to quota or configuration issues.

## Common Causes

- External IP quota is exhausted for the project
- Static IP is not reserved and ephemeral IP was released
- Instance was created without external IP (no-nat)
- VPC firewall rules block external access
- Ephemeral external IP is not available in the region

## How to Fix

### 1. Check external IP quota
```bash
gcloud compute project-info describe --format="yaml(quotas)" \
  | grep -A2 "IN_USE_ADDRESSES"
```

### 2. Reserve static IP
```bash
gcloud compute addresses create my-static-ip \
  --region=REGION
```

### 3. Assign static IP to instance
```bash
gcloud compute instances add-access-config VM_NAME \
  --access-config-name=my-static-ip \
  --address=STATIC_IP_ADDRESS \
  --zone=ZONE
```

### 4. List all external IPs
```bash
gcloud compute addresses list --format="table(name,address,status)"
```

## Examples

### Create instance with static IP
```bash
gcloud compute instances create my-vm \
  --zone=us-central1-a \
  --address=my-static-ip \
  --machine-type=e2-medium
```

### Release ephemeral IP
```bash
gcloud compute instances delete-access-config VM_NAME \
  --access-config-name="external-nat" \
  --zone=ZONE
```

## Related Errors

- [GCP Instance Create Error]({{< relref "/cloud/gcp/gcp-instance-create-error" >}})
- [GCP CE Instance Not Found]({{< relref "/cloud/gcp/gcp-ce-instance-not-found" >}})
