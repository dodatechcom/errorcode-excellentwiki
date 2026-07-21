---
title: "[Solution] GCP Reservation"
description: "ReservationError for reservations."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Reservation` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Reservation name taken
- Resource count exceeds limit
- Term (1/3 year) mismatch

## How to Fix

### Create reservation

```bash
gcloud compute reservations create myReservation --vm-count=1 --machine-type=n1-standard-1
```

## Examples

- Example scenario: reservation name taken
- Example scenario: resource count exceeds limit
- Example scenario: term (1/3 year) mismatch

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
