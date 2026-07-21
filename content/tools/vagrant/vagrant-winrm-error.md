---
title: "[Solution] Vagrant WinRM Error"
description: "Fix Vagrant WinRM connection errors when Windows VMs cannot be managed via WinRM."
tools: ["vagrant"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vagrant WinRM Error

Vagrant fails to connect to Windows VM via WinRM.

```
Unable to connect to WinRM, retrying...
```

## Common Causes

- WinRM not enabled in Windows VM
- Firewall blocking WinRM port
- HTTPS certificate not trusted
- Credentials incorrect
- WinRM service not running

## How to Fix

### Enable WinRM in Windows

```powershell
# Inside Windows VM
Enable-PSRemoting -Force
winrm set winrm/config/service '@{AllowUnencrypted="true"}'
winrm set winrm/config/service/auth '@{Basic="true"}'
```

### Configure WinRM in Vagrantfile

```ruby
Vagrant.configure("2") do |config|
  config.vm.communicator = "winrm"
  config.winrm.username = "vagrant"
  config.winrm.password = "vagrant"
  config.winrm.transport = :plaintext
  config.winrm.basic_auth_only = true
end
```

### Open Firewall Port

```powershell
# Inside Windows VM
New-NetFirewallRule -DisplayName "WinRM" -Direction Inbound -LocalPort 5985,5986 -Protocol TCP -Action Allow
```

### Check WinRM Service

```powershell
# Inside Windows VM
Get-Service winrm
Start-Service winrm
```

### Use WinRM with HTTPS

```ruby
config.winrm.transport = :ssl
config.winrm.port = 5986
```

## Examples

```ruby
# Full WinRM configuration
Vagrant.configure("2") do |config|
  config.vm.box = "gusztavvargadr/windows-server-2022-standard"
  config.vm.communicator = "winrm"
  
  config.winrm.username = "vagrant"
  config.winrm.password = "vagrant"
  config.winrm.transport = :plaintext
  config.winrm.basic_auth_only = true
  
  config.vm.provision "shell", inline: <<-SHELL
    Write-Host "Provisioning..."
  SHELL
end
```
