---
title: "[Solution] Azure Service Endpoint Error"
description: "Fix Azure service endpoint configuration failures that block private access to Azure services."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Service endpoint errors prevent resources in a VNet from accessing Azure services through private endpoints. This causes traffic to route through public IPs instead of the Azure backbone.

## Common Causes

- Service endpoint is not enabled on the target subnet
- The service endpoint does not match the Azure service namespace
- Subnet is too small and has no available IPs for the endpoint
- Service endpoint was removed during a VNet update

## How to Fix

### Check existing service endpoints

```bash
az network vnet subnet show \
  --vnet-name myVNet \
  --name mySubnet \
  --resource-group myRG \
  --query "serviceEndpoints"
```

### Add a service endpoint

```bash
az network vnet subnet update \
  --vnet-name myVNet \
  --name mySubnet \
  --resource-group myRG \
  --service-endpoints "Microsoft.Storage" "Microsoft.KeyVault"
```

### List available service endpoints

```bash
az network list-service-endpoints --location eastus
```

### Verify service endpoint on subnet

```bash
az network vnet subnet list \
  --vnet-name myVNet \
  --resource-group myRG \
  --query "[].{Name:name,Endpoints:serviceEndpoints}"
```

## Examples

- Storage account returns `403 Forbidden` because the subnet lacks a Microsoft.Storage service endpoint
- Key Vault with VNet rules rejects connections from a subnet that has no service endpoint
- Service endpoint was added to a different subnet than the one used by the VM

## Related Errors

- [Azure VNet Error]({{< relref "/cloud/azure/azure-vnet-error" >}}) -- VNet configuration issues.
- [Azure Storage Firewall]({{< relref "/cloud/azure/azure-storage-firewall" >}}) -- Storage firewall errors.
