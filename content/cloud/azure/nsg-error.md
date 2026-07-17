---
title: "Azure NetworkSecurityGroup Rule Denied Traffic"
description: "NSG rule denied traffic — Fix Azure Network Security Group configuration errors."
error-types: ["api-error"]
severities: ["error"]
weight: 5
---

The NSG rule denied traffic error occurs when Azure Network Security Group rules block inbound or outbound network traffic to or from a VM. NSGs act as firewalls at the subnet and NIC level.

## Common Causes

- Default NSG rules deny all inbound traffic except from the VNet and load balancer
- Custom NSG rules explicitly deny traffic on required ports
- NSG rules are evaluated in priority order — a deny rule may match before an allow rule
- The NSG is associated with the wrong subnet or NIC

## How to Fix

List NSG rules for a resource:

```bash
az network nsg rule list --nsg-name my-nsg --resource-group my-rg --query '[].{Priority:priority,Name:name,Direction:direction,Access:access,Protocol:protocol,Port:destinationPortRange}'
```

Add an inbound allow rule:

```bash
az network nsg rule create \
  --nsg-name my-nsg \
  --resource-group my-rg \
  --name AllowSSH \
  --priority 100 \
  --direction Inbound \
  --access Allow \
  --protocol Tcp \
  --destination-port-ranges 22 \
  --source-address-prefixes 10.0.0.0/8
```

Check which NSG is associated with a NIC:

```bash
az network nic show \
  --name my-nic \
  --resource-group my-rg \
  --query 'networkSecurityGroup.id'
```

## Examples

- Cannot SSH into a VM because no NSG rule allows port 22 inbound
- Application on port 8080 is unreachable because the NSG only allows port 80
- Outbound traffic to an external API on port 8443 is blocked by an outbound deny rule

## Related Errors

- [Azure Disk Error]({{< relref "/cloud/azure/disk-error" >}}) — disk I/O failure.
- [Azure VM Not Found]({{< relref "/cloud/azure/vm-not-found" >}}) — VM resource not found.
- [AWS VPC Error]({{< relref "/cloud/aws/vpc-error" >}}) — VPC configuration issues.
