---
title: "[Solution] AZURE NSG Rule Error"
description: "InvalidRuleMatch or SecurityRuleInvalid when NSG rules fail."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `NSG Rule Error` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Priority conflicts with existing rule
- Source/destination address format invalid
- Port range invalid
- Rule references non-existent NSG

## How to Fix

### List NSG rules

```bash
az network nsg rule list --nsg-name myNSG --resource-group myRG --query "[].{Name:name,Priority:priority,Direction:direction}" --output table
```
### Create rule

```bash
az network nsg rule create --nsg-name myNSG --resource-group myRG --name AllowHTTP --priority 100 --direction Inbound --access Allow --protocol Tcp --destination-port-ranges 80 443
```
### Delete rule

```bash
az network nsg rule delete --nsg-name myNSG --resource-group myRG --name AllowHTTP
```

## Examples

- Priority 100 conflicts with existing rule
- Source address prefix is not valid CIDR

## Related Errors

- [Azure Networking Error]({{< relref "/cloud/azure/azure-nsg-error" >}}) -- NSG errors
- [Route Table]({{< relref "/cloud/azure/azure-vnet-route-table" >}}) -- Route table
