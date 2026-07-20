---
title: "[Solution] GCP Network Tier Error — Network Tier premium standard egress errors"
description: "Fix GCP Network Tier errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 104
---

Network Tier errors occur when there are issues with premium or standard network tier configurations affecting egress traffic and performance.

## Common Causes
- Invalid network tier specified for resources
- Unsupported region for standard tier
- Network tier mismatch between load balancer and backend
- Quota limits on network tier resources
- Legacy network tier references

## How to Fix

### 1. Check network tier support
```bash
gcloud compute regions describe REGION --format="value(supportedNetworkTiers[])"
```

### 2. List resources by network tier
```bash
gcloud compute addresses list --filter="networkTier:PREMIUM"
gcloud compute forwarding-rules list --filter="networkTier:STANDARD"
```

### 3. Update address network tier
```bash
gcloud compute addresses update ADDRESS_NAME \
  --network-tier=PREMIUM \
  --region=REGION
```

### 4. Create address with specific tier
```bash
gcloud compute addresses create ADDRESS_NAME \
  --region=REGION \
  --network-tier=STANDARD
```

### 5. Update forwarding rule tier
```bash
gcloud compute forwarding-rules update RULE_NAME \
  --network-tier=PREMIUM \
  --region=REGION
```

## Examples

### Create standard tier external IP
```bash
gcloud compute addresses create standard-ip \
  --region=us-central1 \
  --network-tier=STANDARD
```

### Check tier availability
```bash
gcloud compute regions describe us-central1 --format="yaml(supportedNetworkTiers)"
```

## Related Errors
- [GCP VPC Network Error](/cloud/gcp/gcp-vpc-error/)
- [GCP Cloud Load Balancing Error](/cloud/gcp/gcp-cloud-load-balancing-error/)
- [GCP Cloud NAT Error](/cloud/gcp/gcp-cloud-nat-error/)