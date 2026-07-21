---
title: "[Solution] Azure Private DNS Resolution Error"
description: "Fix Azure Private DNS zone resolution failures for virtual network linked resources."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Private DNS resolution errors prevent VMs from resolving private DNS names within virtual networks. This breaks service discovery for private endpoints and internal load balancers.

## Common Causes

- Private DNS zone is not linked to the virtual network
- DNS forwarding rules override private DNS resolution
- Azure DNS Private Resolver is not configured for cross-vNet scenarios
- Host name resolution timeout is too short for internal DNS servers

## How to Fix

### Link private DNS zone to VNet

```bash
az network private-dns link vnet create \
  --resource-group myRG \
  --zone-name privatelink.blob.core.windows.net \
  --name myLink \
  --virtual-network myVNet \
  --registration-enabled false
```

### List linked virtual networks

```bash
az network private-dns zone list \
  --resource-group myRG \
  --query "[].{Name:name,Links:virtualNetworkLinks}"
```

### Configure DNS forwarding

```bash
az network private-dns resolver forwarding-rule create \
  --dns-resolver-name myResolver \
  --forwarding-ruleset-name myRuleset \
  --name myForwardingRule \
  --resource-group myRG \
  --domain-name "corp.example.com." \
  --forwarding-rule-state Enabled \
  --target-dns-servers "[{ipAddress:10.0.0.4,port:53}]"
```

### Verify DNS resolution from a VM

```bash
nslookup myserver.database.windows.net
```

## Examples

- VM cannot resolve `myserver.blob.core.windows.net` because the private DNS zone is not linked
- Cross-vNet DNS resolution fails because the private DNS resolver is not configured
- DNS forwarding rules conflict with private DNS zones and cause resolution loops

## Related Errors

- [Azure DNS Error]({{< relref "/cloud/azure/azure-dns-error" >}}) -- DNS issues.
- [Azure Private Link Error]({{< relref "/cloud/azure/azure-private-link-error" >}}) -- Private link issues.
