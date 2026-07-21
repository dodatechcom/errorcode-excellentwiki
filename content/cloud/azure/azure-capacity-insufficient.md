---
title: "[Solution] AZURE Capacity Insufficient"
description: "Insufficient capacity for VM deployment."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Capacity Insufficient` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- No available resources in cluster
- VM size limited to a single region
- Azure RDMA/HPC capacity insufficient

## How to Fix

### Check SKU availability

```bash
az vm list-skus --size Standard_ND96asr_v4
```

## Examples

- Example scenario: no available resources in cluster
- Example scenario: vm size limited to a single region
- Example scenario: azure rdma/hpc capacity insufficient

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
