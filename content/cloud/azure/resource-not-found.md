---
title: "Azure Resource Not Found"
description: "ResourceNotFound - The resource was not found"
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `ResourceNotFound` error occurs when an Azure Resource Manager (ARM) API request references a resource that does not exist in the specified subscription or resource group.

## Common Causes

- The resource was deleted or never created
- Incorrect resource group name or subscription ID in the request
- Resource exists in a different region than expected
- Typo in the resource name or type

## How to Fix

List resources in a resource group to verify:

```bash
az resource list \
  --resource-group myResourceGroup \
  --output table
```

Check a specific resource:

```bash
az resource show \
  --resource-group myResourceGroup \
  --name myVM \
  --resource-type Microsoft.Compute/virtualMachines
```

## Examples

- Querying a virtual machine that was deleted in a previous deployment
- Using `az network vnet show` with a wrong virtual network name
- Accessing a resource from a different subscription than the one where it was created

## Related Errors

- [Azure Authentication Failed]({{< relref "/cloud/azure/authentication-failed" >}})
- [AWS S3 Access Denied]({{< relref "/cloud/aws/s3-access-denied" >}})
- [GCP Permission Denied]({{< relref "/cloud/gcp/permission-denied" >}})
