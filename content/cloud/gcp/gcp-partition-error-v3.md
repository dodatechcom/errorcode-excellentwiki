---
title: "[Solution] GCP Partition Error"
description: "PartitionError for partitioned tables."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Partition Error` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Partition filter required over unpartitioned
- Deletion/merge target not a partition
- Cross-partition UPDATE not supported

## How to Fix

### List partitions

```bash
bq query 'SELECT _PARTITIONTIME FROM myDataset.myTable GROUP BY _PARTITIONTIME'
```

## Examples

- Example scenario: partition filter required over unpartitioned
- Example scenario: deletion/merge target not a partition
- Example scenario: cross-partition update not supported

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
