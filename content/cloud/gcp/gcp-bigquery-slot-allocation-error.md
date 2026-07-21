---
title: "[Solution] GCP BigQuery Slot Allocation Error"
description: "Resolve BigQuery slot allocation errors. Troubleshoot capacity reservations, slot sharing, and Flex/FlatRate pricing issues in GCP BigQuery."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP BigQuery Slot Allocation Error

The BigQuery Slot Allocation error occurs when queries cannot access sufficient BigQuery slots for execution, causing delays or failures.

## Common Causes

- FlatRate reservation has no available slots
- Flex Slots are not provisioned in the required region
- Slot assignment is not linked to the correct project or dataset
- Edition-based reservations do not match the query workload
- Concurrent query count exceeds slot pool capacity

## How to Fix

### 1. Check current slot usage
```bash
bq --format=prettyjson show --project=PROJECT_ID \
  --location=REGION ReservationName > reservation.json
```

### 2. Create a capacity reservation
```bash
bq mk --location=REGION \
  --reservation \
  --slots=100 \
  --edition=ENTERPRISE \
  ReservationName
```

### 3. Assign reservation to a project
```bash
bq update --reservation ReservationName \
  --assign_project=PROJECT_ID
```

### 4. Monitor slot utilization
```bash
bq --format=prettyjson show --project=PROJECT_ID \
  --location=REGION --reservation ReservationName
```

## Examples

### Create flex slots for burst capacity
```bash
bq mk --flex --location=REGION \
  --reservation \
  --slots=500 \
  FlexSlots
```

### Query using reservation
```sql
SELECT * FROM my_dataset.my_table
-- Uses assigned reservation automatically
```

## Related Errors

- [GCP BigQuery Error]({{< relref "/cloud/gcp/gcp-bigquery-error" >}})
- [GCP Query Exceeded]({{< relref "/cloud/gcp/gcp-query-exceeded" >}})
