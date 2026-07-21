---
title: "[Solution] AZURE VM Allocation Failed"
description: "AllocationFailed when Azure cannot allocate a VM."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `VM Allocation Failed` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- No capacity in the region/AZ
- Incorrect VM size selected
- Subscription quota insufficient
- Azure resource exhaustion

## How to Fix

### Check capacity

```bash
az vm list-skus --size Standard_DS2_v2 --region eastus
```

### Try different size

```bash
az vm create --name myVM --resource-group myRG --size Standard_DS3_v2 --image UbuntuLTS
```

## Examples

- Example scenario: no capacity in the region/az
- Example scenario: incorrect vm size selected
- Example scenario: subscription quota insufficient
- Example scenario: azure resource exhaustion

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
