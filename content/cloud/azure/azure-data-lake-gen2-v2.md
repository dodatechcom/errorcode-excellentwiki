---
title: "[Solution] AZURE Data Lake Gen2"
description: "DataLakeGen2Error for ADLS Gen2."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Data Lake Gen2` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Hierarchical namespace not enabled
- Filesystem conflict with blob
- Permission ACL missing

## How to Fix

### Enable HNS

```bash
az storage account create -n mydatalake -g myRG --kind StorageV2 --hns
```

## Examples

- Example scenario: hierarchical namespace not enabled
- Example scenario: filesystem conflict with blob
- Example scenario: permission acl missing

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
