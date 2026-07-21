---
title: "[Solution] Hyper-V Live Migration Failed Error Fix"
description: "Fix Hyper-V live migration failed error on Windows Server when virtual machines cannot be migrated between hosts without downtime."
platforms: ["windows"]
severities: ["error"]
error_types: ["os-error"]
weight: 10
---

# [Solution] Hyper-V Live Migration Failed Error Fix

Hyper-V live migration failures prevent moving running virtual machines between hosts without downtime. The migration process fails partway through, leaving the VM in an inconsistent state.

## Common Causes
- Insufficient memory on the destination host
- Network bandwidth limitation for migration traffic
- Kerberos delegation not configured for migration
- Virtual switch name mismatch between hosts
- Storage not accessible from both hosts

## How to Fix

### Solution 1: Check Available Memory on Destination

```powershell
Get-VMHost -ComputerName destination-host | Select-Object ComputerName, @{N='AvailableMemoryGB';E={[math]::Round($_.MemoryAvailable/1GB,2)}}
```

### Solution 2: Configure Live Migration Network

```powershell
Enable-VMMigration -VirtualMachineMigrationPerformanceOption Compression
Set-VMMigrationNetwork 10.0.0.0/24
```

### Solution 3: Verify Kerberos Delegation

```powershell
Set-ADComputer -Identity source-host -PrincipalsAllowedToDelegateToAccount destination-host$
```

### Solution 4: Test VM Migration

```powershell
Test-VMStartVMigration -VMName "VMName" -DestinationHost "destination-host"
```

### Solution 5: Check Storage Accessibility

Ensure both hosts have access to the same storage (SAN, CSV, or SMB share).

## Examples
```powershell
Get-VMMigrationNetwork
Get-VMHost | Select-Object ComputerName, MemoryAvailable
```
