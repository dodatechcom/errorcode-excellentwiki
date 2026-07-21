---
title: "[Solution] Azure VM License Error"
description: "Resolve Azure VM licensing errors when deploying or migrating Windows and SQL Server virtual machines."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

License errors occur when Azure VMs cannot activate Windows or SQL Server licenses. This is common during migration scenarios or when Hybrid Benefit is misconfigured.

## Common Causes

- Hybrid Benefit is enabled but no eligible on-premises licenses exist
- License type does not match the VM image (e.g., SQL Server on a Windows-only license)
- Azure Hybrid Benefit activation key server is unreachable
- VM was deployed with incorrect license type and cannot be changed while running

## How to Fix

### Check current license type

```bash
az vm get-image \
  --resource-group myRG \
  --name myVM \
  --query licenseType
```

### Update license type on a running VM

```bash
az vm update \
  --resource-group myRG \
  --name myVM \
  --set licenseType=Windows_Server
```

### List eligible Hybrid Benefit licenses

```bash
az benefit list-eligible \
  --query "[].{ID:id,Type:type,Quantity:quantity}"
```

## Examples

- VM deployment fails with `LicenseTypeMismatch` when deploying SQL Server 2022 image
- Azure Hybrid Benefit reporting shows zero eligible licenses after on-premises decommission
- VM cannot be resized because the new size requires a different license type

## Related Errors

- [Azure VM Allocation Failed]({{< relref "/cloud/azure/azure-vm-allocation-failed" >}}) -- Allocation failures.
- [Azure Billing Error]({{< relref "/cloud/azure/azure-subscription-error" >}}) -- Billing and license issues.
