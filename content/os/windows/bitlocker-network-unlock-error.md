---
title: "[Solution] BitLocker Network Unlock Error Fix"
description: "Fix BitLocker Network Unlock failure on Windows when the network unlock key cannot be retrieved from the server during startup."
platforms: ["windows"]
severities: ["error"]
error_types: ["os-error"]
weight: 10
---

# [Solution] BitLocker Network Unlock Error Fix

BitLocker Network Unlock allows domain-joined PCs to unlock BitLocker-encrypted volumes over the network without entering a PIN. When this fails, the PC cannot boot without manual intervention.

## Common Causes
- Network adapter not available during boot (DHCP not configured)
- WDS server hosting the unlock key is unreachable
- TPM and network unlock keys not properly configured
- Group Policy not deployed correctly for network unlock
- BIOS/UEFI network stack not enabled

## How to Fix

### Solution 1: Enable Network Stack in BIOS

Enter BIOS/UEFI and enable PXE boot and the network stack.

### Solution 2: Verify WDS Server Status

```powershell
Get-Service -Name WDSServer | Select-Object Status
Start-Service -Name WDSServer
```

### Solution 3: Check BitLocker Network Unlock Certificate

```powershell
Get-BitLockerVolume | Select-Object MountPoint, VolumeStatus, ProtectionStatus
```

### Solution 4: Re-add Network Unlock Key

```powershell
Manage-BDE -Protectors -Get C:
```

### Solution 5: Configure DHCP for Network Boot

Ensure DHCP options 60, 66, and 67 are configured for PXE boot on your network.

## Examples
```powershell
Manage-BDE -Protectors -Get C:
```
