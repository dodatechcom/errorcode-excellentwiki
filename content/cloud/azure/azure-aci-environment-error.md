---
title: "[Solution] Azure Container Instances Environment Error"
description: "Fix Azure Container Instances environment configuration errors for VNet and GPU deployments."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

ACI environment errors occur when container groups cannot be deployed to the specified subnet, region, or resource constraints. This blocks serverless container workloads.

## Common Causes

- Subnet is too small or already has too many container groups
- GPU SKU is not available in the target region
- VNet integration requires a delegated subnet that is not configured
- Container group requires a managed identity but the identity does not exist

## How to Fix

### Check subnet delegation

```bash
az network vnet subnet show \
  --vnet-name myVNet \
  --name aci-subnet \
  --resource-group myRG \
  --query "delegations"
```

### Delegate subnet to ACI

```bash
az network vnet subnet update \
  --vnet-name myVNet \
  --name aci-subnet \
  --resource-group myRG \
  --delegations "[{name:aciDelegation,properties:{serviceName:'Microsoft.ContainerInstance/containerGroups'}}]"
```

### Deploy a container group

```bash
az container create \
  --resource-group myRG \
  --name myContainer \
  --image myregistry.azurecr.io/myimage:latest \
  --vnet myVNet \
  --subnet aci-subnet \
  --cpu 2 --memory 4
```

### Check GPU availability

```bash
az vm list-sizes --location eastus --query "[?contains(name,'GPU')].name"
```

## Examples

- Container group fails with `SubnetDelegationAlreadyExists` because another service already delegated the subnet
- GPU container fails because `Standard_NC` SKUs are not available in the target region
- VNet-deployed container cannot reach the internet because NAT gateway is not configured

## Related Errors

- [Azure Container Instance]({{< relref "/cloud/azure/azure-container-instance" >}}) -- General ACI errors.
- [Azure VNet Error]({{< relref "/cloud/azure/azure-vnet-error" >}}) -- VNet configuration.
