---
title: "[Solution] Azure VM Extensions Failed"
description: "Fix Azure VM extension provisioning failures with actionable Azure CLI commands and troubleshooting steps."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

The VM extension provisioning error occurs when Azure cannot successfully install or configure a VM extension on a virtual machine. This blocks monitoring, configuration, and management capabilities.

## Common Causes

- VM agent is not running or is out of date
- Extension installation timed out due to slow network or high VM load
- Conflicting extensions installed simultaneously on the same VM
- VM OS disk is full and cannot write extension files
- Extension version is incompatible with the VM operating system

## How to Fix

### Check VM agent status

```bash
az vm get-instance-view \
  --name myVM \
  --resource-group myRG \
  --query "instanceView.extensions"
```

### Reinstall the VM agent

```bash
az vm extension set \
  --resource-group myRG \
  --vm-name myVM \
  --name VMAccessForLinux \
  --publisher Microsoft.OSTCExtensions \
  --version 2.0 \
  --force-update
```

### View extension provisioning state

```bash
az vm extension list \
  --resource-group myRG \
  --vm-name myVM \
  --query "[].{Name:name,State:provisioningState,Code:code}"
```

## Examples

- Custom script extension fails with `VMExtensionProvisioningTimeout` after 15 minutes
- Diagnostics extension reports `ProvisioningFailed` due to a missing configuration file
- Azure Disk Encryption extension conflicts with third-party encryption agent

## Related Errors

- [Azure VM Allocation Failed]({{< relref "/cloud/azure/azure-vm-allocation-failed" >}}) -- Resource allocation issues.
- [Azure Extension Failed]({{< relref "/cloud/azure/azure-extension-failed" >}}) -- General extension failures.
