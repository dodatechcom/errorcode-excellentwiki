---
title: "[Solution] Azure Key Vault Firewall Error"
description: "Fix Azure Key Vault firewall errors that block access from approved networks and services."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Firewall errors occur when Key Vault network rules reject connections from approved IP addresses or virtual networks. This is common in locked-down environments.

## Common Causes

- Default network action is set to Deny and no IP or VNet rules are added
- Client IP address is not in the allowed IP ranges
- Service endpoint is not configured on the subnet accessing Key Vault
- Trusted Microsoft services bypass is not enabled for required services

## How to Fix

### Check current network rules

```bash
az keyvault show \
  --name myKeyVault \
  --query "properties.networkAcls"
```

### Add an IP rule

```bash
az keyvault update \
  --name myKeyVault \
  --set properties.networkAcls.defaultAction=Deny \
  --set properties.networkAcls.ipRules="[{ipAddress:203.0.113.0/24}]"
```

### Add a VNet rule

```bash
az keyvault network-rule add \
  --name myKeyVault \
  --vnet-name myVNet \
  --subnet mySubnet
```

### Enable trusted Microsoft services

```bash
az keyvault update \
  --name myKeyVault \
  --set properties.networkAcls.defaultAction=Deny \
  --set properties.networkAcls.bypass=AzureServices
```

## Examples

- Key Vault returns `RequestDisallowedByNspolicy` when accessed from a non-approved IP
- Azure Functions cannot read secrets because the Key Vault firewall does not allow Azure services
- Service endpoint is configured on the subnet but Key Vault still rejects the connection

## Related Errors

- [Azure Key Vault Error]({{< relref "/cloud/azure/azure-key-vault-error" >}}) -- General Key Vault errors.
- [Azure NSG Rule]({{< relref "/cloud/azure/azure-nsg-rule" >}}) -- Network security group issues.
