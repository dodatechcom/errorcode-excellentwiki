---
title: "[Solution] Azure NIC Attach Error"
description: "Fix Azure network interface card attachment failures preventing VM connectivity."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

NIC attachment errors prevent virtual machines from connecting to networks. This blocks all network communication including management access.

## Common Causes

- NIC is already attached to another VM in a different state
- Subnet does not have available IP addresses for the NIC
- Network security group on the subnet blocks the required traffic
- Accelerated networking is enabled but the VM size does not support it

## How to Fix

### Check NIC status and attachments

```bash
az network nic show \
  --name myNIC \
  --resource-group myRG \
  --query "{State:virtualMachine,id:virtualMachine.id}"
```

### Detach NIC from current VM

```bash
az vm network nic remove \
  --vm-name myVM \
  --resource-group myRG \
  --nic myNIC
```

### Attach NIC to a new VM

```bash
az vm network nic add \
  --vm-name myVM \
  --resource-group myRG \
  --nic myNIC
```

### Check subnet address availability

```bash
az network vnet list-available-ips \
  --resource-group myRG \
  --vnet-name myVNet
```

## Examples

- VM creation fails because the NIC is still attached to a deleted VM's network interface
- NIC attachment fails with `InvalidSubnet` when the subnet is full
- Accelerated networking is not available on Standard_B1s VMs but was enabled on the NIC

## Related Errors

- [Azure VM Error]({{< relref "/cloud/azure/azure-vm-error" >}}) -- General VM errors.
- [Azure VNet Error]({{< relref "/cloud/azure/azure-vnet-error" >}}) -- VNet issues.
