---
title: "[Solution] Vagrant Mount CIFS Error"
description: "Fix Vagrant CIFS/SMB mount errors when mounting Windows shares from a Linux VM."
tools: ["vagrant"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vagrant Mount CIFS Error

Vagrant fails to mount CIFS/SMB shares from the host.

```
mount error(13): Permission denied
```

## Common Causes

- SMB credentials not provided
- Windows firewall blocking SMB
- CIFS utilities not installed
- Share path incorrect
- Protocol version mismatch

## How to Fix

### Configure SMB Sync

```ruby
Vagrant.configure("2") do |config|
  config.vm.synced_folder ".", "/vagrant", type: "smb",
    smb_username: "user",
    smb_password: "password"
end
```

### Install CIFS Utilities

```bash
# Inside VM
sudo apt install cifs-utils
```

### Use SMB with Guest

```ruby
config.vm.synced_folder ".", "/vagrant", type: "smb",
  mount_options: ["vers=3.0", "sec=ntlm"]
```

### Fix Permission Denied

```bash
# Ensure correct mount point
sudo mkdir -p /mnt/share
sudo chmod 755 /mnt/share

# Test mount manually
sudo mount -t cifs //host/share /mnt/share -o username=user,password=pass
```

### Use rsync Fallback

```ruby
# If SMB does not work
config.vm.synced_folder ".", "/vagrant", type: "rsync",
  rsync__exclude: [".git/", "node_modules/"]
```

## Examples

```ruby
# SMB sync with options
Vagrant.configure("2") do |config|
  config.vm.synced_folder ".", "/vagrant", type: "smb",
    smb_username: ENV["SMB_USER"],
    smb_password: ENV["SMB_PASS"],
    mount_options: ["vers=3.0"]
end
```
