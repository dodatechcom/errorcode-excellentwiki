---
title: "[Solution] GCP Unused Reservation Error — reservation in-use consume errors"
description: "Fix GCP Unused Reservation errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 115
---

Unused Reservation errors occur when compute reservations are not being consumed by VMs or are underutilized.

## Common Causes
- Reservation created but no matching VMs running
- VM machine type does not match reservation
- Zone mismatch between reservation and VM
- Reservation specific flags not matching instance config
- Reservation approaching expiration

## How to Fix

### 1. List reservations and status
```bash
gcloud compute reservations list --zone=ZONE
```

### 2. Check reservation utilization
```bash
gcloud compute reservations describe RESERVATION_NAME --zone=ZONE \
  --format="yaml(name,status,specificReservation,specificReservationRequired)"
```

### 3. Create matching reservation
```bash
gcloud compute reservations create RESERVATION_NAME \
  --zone=ZONE \
  --requirements=vm-count=5,vm-type=e2-standard-4 \
  --require-specific
```

### 4. Create VM consuming reservation
```bash
gcloud compute instances create VM_NAME \
  --zone=ZONE \
  --machine-type=e2-standard-4 \
  --reservation-affinity=consume=RESERVATION_NAME
```

### 5. Delete unused reservation
```bash
gcloud compute reservations delete RESERVATION_NAME --zone=ZONE --quiet
```

## Examples

### Create and consume reservation
```bash
gcloud compute reservations create web-reservation \
  --zone=us-central1-a \
  --requirements=vm-count=3,vm-type=e2-standard-4 \
  --require-specific

gcloud compute instances create web-1 \
  --zone=us-central1-a \
  --machine-type=e2-standard-4 \
  --reservation-affinity=consume=web-reservation
```

### View reservation coverage
```bash
gcloud compute reservations list --zone=us-central1-a \
  --format="table(name,status,specificReservation.vmCount,specificReservation.countRemaining)"
```

## Related Errors
- [GCP Quota Error](/cloud/gcp/quota-exceeded/)
- [GCP Commitment Error](/cloud/gcp/gcp-commitment-error/)
- [GCP Compute Engine Error](/cloud/gcp/gcp-compute-error/)