---
title: "[Solution] GCP Packet Mirroring Error — policy collector network errors"
description: "Fix GCP Packet Mirroring errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 106
---

Packet Mirroring errors occur when there are issues with mirroring policies, collector instances, or network configuration for traffic inspection.

## Common Causes
- Collector instance not in same VPC as mirrored instances
- Mirrored instance not on a supported network interface type
- Policy filter too restrictive or misconfigured
- Packet Mirroring API not enabled
- Collector instance lacks sufficient resources for mirrored traffic

## How to Fix

### 1. Enable Packet Mirroring API
```bash
gcloud services enable compute.googleapis.com --project=PROJECT_ID
```

### 2. List packet mirroring policies
```bash
gcloud compute packet-mirroring list --region=REGION
```

### 3. Create a packet mirroring policy
```bash
gcloud compute packet-mirroring create POLICY_NAME \
  --region=REGION \
  --network=NETWORK_NAME \
  --network-tags=TAG \
  --mirrored-instances-tags=INSTANCE_TAG \
  --collector-ilb=COLLECTOR_LB_NAME \
  --filter-includes-cidr-ranges=10.0.0.0/8 \
  --filter-direction=both
```

### 4. Update existing policy
```bash
gcloud compute packet-mirroring update POLICY_NAME \
  --region=REGION \
  --enable=true
```

### 5. Delete a policy
```bash
gcloud compute packet-mirroring delete POLICY_NAME --region=REGION --quiet
```

## Examples

### Mirror traffic for security inspection
```bash
gcloud compute packet-mirroring create security-mirror \
  --region=us-central1 \
  --network=prod-vpc \
  --mirrored-instances-tags=web-server \
  --collector-ilb=mirror-collector-lb \
  --filter-includes-cidr-ranges=0.0.0.0/0 \
  --filter-port-ranges=80-443 \
  --filter-direction=both
```

### List active policies
```bash
gcloud compute packet-mirroring list --region=us-central1 --format="table(name,region,network)"
```

## Related Errors
- [GCP VPC Network Error](/cloud/gcp/gcp-vpc-error/)
- [GCP Cloud Load Balancing Error](/cloud/gcp/gcp-cloud-load-balancing-error/)
- [GCP Cloud Armor Error](/cloud/gcp/gcp-cloud-armor-error/)