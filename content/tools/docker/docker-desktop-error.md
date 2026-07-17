---
title: "[Solution] Docker Desktop WSL2 / Virtual Machine Error"
description: "Fix Docker Desktop WSL2 and virtual machine errors. Resolve backend engine start failures on Windows and macOS."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker Desktop: WSL2 / Virtual Machine Error

Docker Desktop fails to start because WSL2 (Windows Subsystem for Linux 2) or the underlying virtual machine cannot initialize. This prevents the Docker daemon from running entirely.

## Common Causes

- WSL2 not enabled or not installed on Windows
- Hyper-V or virtual machine platform disabled in BIOS
- Virtualization not enabled in BIOS/UEFI settings
- Docker Desktop configuration pointing to wrong WSL distro

## How to Fix

### Enable WSL2 on Windows

```powershell
# In PowerShell as Administrator
wsl --install
wsl --set-default-version 2
```

### Enable Virtualization in BIOS

```
1. Restart computer and enter BIOS (usually Del, F2, or F12)
2. Find "Virtualization Technology" or "Intel VT-x" / "AMD-V"
3. Enable it
4. Save and exit
```

### Enable Required Windows Features

```powershell
# PowerShell as Administrator
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
# Restart required
```

### Reset Docker Desktop

```powershell
# Stop Docker Desktop
# Go to Troubleshoot > Reset to factory defaults
# Or delete config:
Remove-Item -Recurse ~\AppData\Local\Docker
```

## Examples

```powershell
# Example 1: WSL not installed
docker info
# error: WSL 2 installation is incomplete
# Fix: wsl --install and restart

# Example 2: Virtualization disabled
Docker Desktop shows "Docker Desktop starting..."
# Error: hardware assisted virtualization and data execution protection must be enabled
# Fix: enable VT-x/AMD-V in BIOS

# Example 3: Wrong WSL distro
docker context use default
# Fix: Settings > Resources > WSL Integration > select correct distro
```

## Related Errors

- [Docker Socket Error]({{< relref "/tools/docker/docker-socket" >}}) — cannot connect to Docker daemon
- [Docker BuildKit Error]({{< relref "/tools/docker/docker-buildkit" >}}) — BuildKit failed to solve
- [Build Failed]({{< relref "/tools/docker/build-failed2" >}}) — general build errors
