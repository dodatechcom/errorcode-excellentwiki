---
title: "[Solution] Azure Public IP Error"
description: "Fix Azure public IP allocation, binding, and DNS resolution failures for VMs and services."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Public IP errors prevent resources from being reachable from the internet. This affects load balancers, VMs, and application gateways that require public endpoints.

## Common Causes

- Public IP address has been deleted but is still referenced by a resource
- Static public IP allocation failed because the region has no available IPs
- DNS label is not configured or conflicts with another resource's DNS
- Public IP SKU does not match the associated load balancer or VM

## How to Fix

### List public IP addresses

```bash
az network public-ip list \
  --resource-group myRG \
  --query "[].{Name:name,IP:ipAddress,Alloc:publicIpAllocationMethod}"
```

### Create a static public IP

```bash
az network public-ip create \
  --name myPublicIP \
  --resource-group myRG \
  --allocation-method Static \
  --sku Standard
```

### Set DNS label

```bash
az network public-ip update \
  --name myPublicIP \
  --resource-group myRG \
  --dns-name myapp
```

### Associate public IP with a VM

```bash
az vm open-port \
  --resource-group myRG \
  --name myVM \
  --port 80
```

## Examples

- VM cannot be reached from the internet because no public IP is associated
- Public IP allocation fails with `InvalidResourceReference` when the SKU is Basic but the LB requires Standard
- DNS resolution fails because the DNS label was not set during creation

## Related Errors

- [Azure Load Balancer Error]({{< relref "/cloud/azure/azure-load-balancer-error" >}}) -- Load balancer issues.
- [Azure DNS Error]({{< relref "/cloud/azure/azure-dns-error" >}}) -- DNS configuration.
