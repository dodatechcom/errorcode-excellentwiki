---
title: "[Solution] Vagrant Hyper-V Error"
description: "Fix Vagrant hyper-v errors. Learn why this happens and how to resolve it quickly."
tools: ["vagrant"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Vagrant Hyper-V Error

Vagrant Hyper-V errors occur when Microsoft Hyper-V provider fails to work correctly.

## Why This Happens

- Hyper-V not enabled
- Permission denied
- VM failed to start
- Network adapter failed

## Common Error Messages

- `hyperv_not_enabled_error`
- `hyperv_permission_error`
- `hyperv_start_error`
- `hyperv_network_error`

## How to Fix It

### Solution 1: Enable Hyper-V

Enable Hyper-V in Windows Features.

### Solution 2: Run as administrator

Run Vagrant commands as Administrator.

### Solution 3: Configure Hyper-V

Set up Hyper-V in Vagrantfile:

```ruby
config.vm.provider "hyperv" do |hyperv|
  hyperv.memory = "1024"
end
```


## Common Scenarios

- **Hyper-V not enabled:** Enable Hyper-V in Windows.
- **Permission denied:** Run as Administrator.

## Prevent It

- Enable Hyper-V properly
- Run as admin
- Check Hyper-V status
