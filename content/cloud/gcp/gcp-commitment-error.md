---
title: "[Solution] GCP Committed Use Discount Error -- plan resource errors"
description: "Fix GCP Committed Use Discount errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 113
---

Committed Use Discount errors occur when there are issues with CUD plans, resource assignment, or discount application.

## Common Causes
- Committed use plan expired or not yet active
- Resource type does not match commitment
- Region mismatch between commitment and resource
- Insufficient commitment coverage for running instances
- Plan modification not supported for commitment type

## How to Fix

### 1. List active commitments
```bash
gcloud compute commitments list --region=REGION
```

### 2. Describe commitment details
```bash
gcloud compute commitments describe COMMITMENT_NAME --region=REGION
```

### 3. Create new commitment
```bash
gcloud compute commitments create COMMITMENT_NAME \
  --region=REGION \
  --resources=VCPU=16 \
  --resource-type=VCPU \
  --plan=ONE_YEAR \
  --machine-series=N2
```

### 4. View commitment utilization
```bash
gcloud compute commitments list --region=REGION \
  --format="table(name,status,plan,resources)"
```

### 5. Create memory commitment
```bash
gcloud compute commitments create MEMORY_COMMITMENT \
  --region=REGION \
  --resources=MEMORY=64 \
  --resource-type=MEMORY \
  --plan=THREE_YEARS
```

## Examples

### Create CUD for N2 instances
```bash
gcloud compute commitments create n2-cud-1yr \
  --region=us-central1 \
  --resources=VCPU=32 \
  --resource-type=VCPU \
  --plan=ONE_YEAR \
  --machine-series=N2
```

### Check commitment status
```bash
gcloud compute commitments list --region=us-central1 \
  --format="yaml(name,status,creationTimestamp,expiresAt)"
```

## Related Errors
- [GCP Quota Error](/cloud/gcp/quota-exceeded/)
- [GCP Compute Engine Error](/cloud/gcp/gcp-compute-error/)
- [GCP Unused Reservation Error](/cloud/gcp/gcp-unused-reservation-error/)