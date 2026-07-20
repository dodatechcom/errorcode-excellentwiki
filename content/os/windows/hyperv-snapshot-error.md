---
title: "[Solution] Hyper-V SNAPSHOT — Snapshot Creation or Apply Error"
description: "Fix Hyper-V snapshot error with these step-by-step solutions. Includes PowerShell commands and registry fixes."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime"]
weight: 1017
---

# [Solution] Hyper-V SNAPSHOT — Snapshot Creation or Apply Error

The Hyper-V snapshot error prevents you from creating, applying, or deleting checkpoints (snapshots) of virtual machines. This affects backup workflows and the ability to revert VMs to a known good state.

## Description

Hyper-V checkpoints capture the state, data, and hardware configuration of a virtual machine at a specific point in time. When checkpoint operations fail, you may encounter:

> "The operation failed while creating a checkpoint of virtual machine VMName."

> "Failed to apply checkpoint. The virtual machine is in an invalid state."

> "Checkpoint operation failed. There is not enough disk space to create the checkpoint."

## Common Causes

1. Insufficient disk space on the checkpoint storage location.
2. The virtual machine is in a critical state or has crashed.
3. Checkpoint configuration is incompatible with the VM.
4. The VHDX is in a differencing chain that is too deep.
5. Antivirus or backup software locks the checkpoint files.
6. The VM generation type does not support the checkpoint type.
7. Storage I/O issues on the host system.

## Solutions

### Solution 1: Check Available Disk Space

Verify there is enough space for checkpoints:

```powershell
Get-VM -Name "VMName" | Get-VMCheckpoint
Get-VM -Name "VMName" | Select-Object Name, CheckpointType, SnapshotFileLocation

# Check disk space on the storage volume
Get-PSDrive -PSProvider FileSystem | Select-Object Name, @{N='FreeGB';E={[math]::Round($_.Free/1GB,2)}}
```

### Solution 2: Create a Standard Checkpoint

Create a checkpoint using PowerShell:

```powershell
Checkpoint-VM -Name "VMName" -SnapshotName "ManualCheckPoint_$(Get-Date -Format 'yyyyMMdd_HHmmss')"
```

### Solution 3: Check VM State

Ensure the VM is in a healthy state:

```powershell
Get-VM -Name "VMName" | Select-Object Name, State, Status, Heartbeat
```

If the VM is in a failed state, stop and restart it:

```powershell
Stop-VM -Name "VMName" -Force -TurnOff
Start-VM -Name "VMName"
```

### Solution 4: Verify Checkpoint Type

Check the checkpoint configuration type:

```powershell
Get-VM -Name "VMName" | Select-Object CheckpointType
```

Switch between standard and production checkpoints:

```powershell
Set-VM -Name "VMName" -CheckpointType Standard
Set-VM -Name "VMName" -CheckpointType Production
```

### Solution 5: Remove Old Checkpoints

Delete old checkpoints to free disk space:

```powershell
Get-VM -Name "VMName" | Get-VMCheckpoint | Remove-VMCheckpoint -Confirm:$false
```

### Solution 6: Move Checkpoint Storage

Change the checkpoint storage location to a volume with more space:

```powershell
Set-VM -Name "VMName" -CheckpointFileLocation "E:\HyperV\Checkpoints"
```

### Solution 7: Check Event Logs for Snapshot Errors

Review Hyper-V checkpoint events:

```powershell
Get-WinEvent -LogName "Microsoft-Windows-Hyper-V-VMMS-Admin" -MaxEvents 50 |
    Where-Object { $_.Message -like "*checkpoint*" -or $_.Message -like "*snapshot*" } |
    Format-Table TimeCreated, Id, Message -AutoSize
```

## Related Errors

- [Hyper-V VM Failed to Start]({{< relref "/os/windows/hyperv-vm-failed-to-start" >}}) — VM won't start
- [Hyper-V VM Connection Error]({{< relref "/os/windows/hyperv-vm-connection-error" >}}) — Cannot connect to VM
- [Hyper-V Live Migration Error]({{< relref "/os/windows/hyperv-live-migration-error" >}}) — Migration failed
