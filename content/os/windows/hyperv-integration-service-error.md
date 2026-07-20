---
title: "[Solution] Hyper-V INTEGRATION_SERVICE — Guest Integration Failed"
description: "Fix Hyper-V integration service error with these step-by-step solutions. Includes PowerShell commands and registry fixes."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime"]
weight: 1020
---

# [Solution] Hyper-V INTEGRATION_SERVICE — Guest Integration Failed

The Hyper-V integration service error occurs when the services that enable communication between the Hyper-V host and the guest operating system fail to function correctly. This impacts time synchronization, data exchange, shutdown operations, and heartbeat monitoring.

## Description

Hyper-V Integration Services are a set of services installed in the guest operating system that provide enhanced functionality between the VM and the host. When these services fail, you lose features like clean shutdown, time sync, OS shutdown signaling, and backup integration. Common errors include:

> "The integration services for this virtual machine are not working properly."

> "Hyper-V Integration Service is not running in the guest."

> "Heartbeat is not detected. The virtual machine may have stopped responding."

## Common Causes

1. Integration Services are not installed in the guest OS.
2. The Integration Services version is outdated or incompatible.
3. The Integration Services service is stopped or disabled in the guest.
4. The VM is running a Linux guest with missing Linux Integration Services (LIS).
5. A Windows update in the guest broke Integration Services.
6. The Hyper-V host and guest have incompatible versions.
7. The guest operating system is not supported for Integration Services.

## Solutions

### Solution 1: Check Integration Services Status

Verify the status of all Integration Services:

```powershell
Get-VMIntegrationService -VMName "VMName" | Format-Table Name, Enabled, OperationalStatus
Get-VMIntegrationService -VMName "VMName" | Where-Object OperationalStatus -ne "OK"
```

### Solution 2: Enable All Integration Services

Enable all Integration Services for the VM:

```powershell
Get-VMIntegrationService -VMName "VMName" | ForEach-Object {
    if (-not $_.Enabled) {
        Enable-VMIntegrationService -VMName "VMName" -Name $_.Name
        Write-Output "Enabled: $($_.Name)"
    }
}
```

### Solution 3: Update Integration Services

Update Integration Services from the Hyper-V host:

```powershell
# Mount the integration services setup ISO
$vm = Get-VM -Name "VMName"
$integrationServicesPath = "${env:ProgramFiles}\Common Files\Hyper-V\Virtual Machine Integration Services"
Get-ChildItem $integrationServicesPath
```

Inside the guest, run the Integration Services installer:

```cmd
:: Run inside the guest OS
vmguestsetup.exe
```

### Solution 4: Restart Integration Services in the Guest

Restart the Hyper-V services inside the guest:

```powershell
# Run inside the guest
Get-Service -Name "vmicexchange", "vmicshutdown", "vmictimesync", "vmicheartbeat", "vmickvpexchange", "vmicvss" |
    Restart-Service -Force
```

### Solution 5: Verify Heartbeat Monitoring

Check if the host is receiving heartbeat signals from the VM:

```powershell
Get-VM -Name "VMName" | Select-Object Name, Heartbeat
Get-VMIntegrationService -VMName "VMName" | Where-Object Name -like "*Heartbeat*"
```

### Solution 6: Check Guest OS Compatibility

Verify the guest OS is supported for Integration Services:

```powershell
Get-VM -Name "VMName" | Select-Object Name, GuestOperatingSystem, Generation, Version
```

### Solution 7: Reinstall Integration Services

Remove and reinstall Integration Services in the guest:

```powershell
# Inside the guest, uninstall via Programs and Features, then reinstall
# Or use DISM to remove the component
dism /online /disable-feature /featurename:Microsoft-Hyper-V-Guest-Integration-Service-Files
```

Then mount the Integration Services ISO from the host:

```powershell
Add-VMDvdDrive -VMName "VMName" -Path "${env:ProgramFiles}\Common Files\Hyper-V\Virtual Machine Integration Services\VMGuest.iso"
```

## Related Errors

- [Hyper-V VM Connection Error]({{< relref "/os/windows/hyperv-vm-connection-error" >}}) — Cannot connect to VM
- [Hyper-V VM Failed to Start]({{< relref "/os/windows/hyperv-vm-failed-to-start" >}}) — VM won't start
- [Hyper-V Live Migration Error]({{< relref "/os/windows/hyperv-live-migration-error" >}}) — Migration failed
