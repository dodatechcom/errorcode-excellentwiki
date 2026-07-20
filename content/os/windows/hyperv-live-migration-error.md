---
title: "[Solution] Hyper-V LIVE_MIGRATION — Live Migration Failed"
description: "Fix Hyper-V live migration error with these step-by-step solutions. Includes PowerShell commands and registry fixes."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime"]
weight: 1019
---

# [Solution] Hyper-V LIVE_MIGRATION — Live Migration Failed

The Hyper-V live migration error occurs when a virtual machine cannot be migrated from one host to another while running. This breaks cluster failover operations and planned maintenance workflows that rely on zero-downtime VM movement.

## Description

Live migration moves a running virtual machine from one Hyper-V host to another without noticeable downtime. When migration fails, the VM may be left in a partially migrated state or the operation may abort entirely. Error messages include:

> "Virtual machine migration operation failed at migration source."

> "Failed to authenticate the connection. A specified authentication package is not registered."

> "Live migration of virtual machine VMName failed."

## Common Causes

1. Insufficient network bandwidth for the migration traffic.
2. Credential delegation (CredSSP) is not configured.
3. The source and destination hosts are not in the same trust domain.
4. Kerberos constrained delegation is not set up.
5. Firewall rules block migration ports.
6. Insufficient resources on the destination host.
7. The VM uses devices that are not compatible with live migration.

## Solutions

### Solution 1: Enable Live Migration on Both Hosts

Ensure live migration is enabled:

```powershell
Enable-VMMigration
Set-VMMigrationNetwork "192.168.1.0/24"
Get-VMMigrationNetwork
```

### Solution 2: Configure Constrained Delegation

Set up Kerberos constrained delegation in Active Directory:

```powershell
# Check current delegation settings
Get-ADComputer -Identity "SourceHost" -Properties msDS-AllowedToDelegateTo
Get-ADComputer -Identity "DestinationHost" -Properties msDS-AllowedToDelegateTo
```

Configure delegation in Active Directory Users and Computers for both the source and destination computer accounts.

### Solution 3: Use CredSSP Authentication

Configure CredSSP for migration authentication:

```powershell
Enable-WSManCredSSP -Role Client -Delegate "DestinationHost.domain.com"
Enable-WSManCredSSP -Role Server
```

### Solution 4: Check Network Configuration

Verify migration network settings:

```powershell
Get-VMMigrationNetwork
Get-VMHost | Select-Object Name, MaximumVirtualMachineMigrationBandwidth, VirtualMachineMigrationAuthenticationType
Set-VMHost -VirtualMachineMigrationAuthenticationType CredSSP
```

### Solution 5: Open Migration Firewall Rules

Enable the required firewall rules:

```powershell
Enable-NetFirewallRule -DisplayGroup "Hyper-V Migration"
New-NetFirewallRule -DisplayName "Live Migration" -Direction Inbound -Protocol TCP -LocalPort 445, 2179, 50000-50100 -Action Allow
```

### Solution 6: Check Destination Host Resources

Ensure the destination has adequate resources:

```powershell
Invoke-Command -ComputerName "DestinationHost" -ScriptBlock {
    Get-CimInstance -ClassName Win32_OperatingSystem | Select-Object TotalVisibleMemorySize, FreePhysicalMemory
    Get-CimInstance -ClassName Win32_Processor | Select-Object NumberOfLogicalProcessors, LoadPercentage
}
```

### Solution 7: Perform Migration via PowerShell

Execute the migration using cmdlets:

```powershell
# Storage migration (same host)
Move-VMStorage -VMName "VMName" -DestinationStoragePath "E:\VMs"

# Live migration (different host)
Move-VM -Name "VMName" -DestinationHost "DestinationHost" -IncludeStorage -DestinationStoragePath "D:\VMs"
```

## Related Errors

- [Hyper-V VM Failed to Start]({{< relref "/os/windows/hyperv-vm-failed-to-start" >}}) — VM won't start
- [Hyper-V VM Connection Error]({{< relref "/os/windows/hyperv-vm-connection-error" >}}) — Cannot connect to VM
- [Hyper-V Virtual Switch Error]({{< relref "/os/windows/hyperv-virtual-switch-error" >}}) — Network not working
