---
title: "[Solution] Vagrant SMB Mount Error"
description: "Fix Vagrant SMB mount errors when SMB shared folders fail to mount on macOS or Linux."
tools: ["vagrant"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vagrant SMB Mount Error

Vagrant SMB sync fails to mount on the guest VM.

```
Failed to mount SMB shared folders
```

## Common Causes

- SMB server not configured
- Firewall blocking SMB ports
- Credential issues
- SMB version mismatch
- macOS SIP blocking SMB

## How to Fix

### Configure SMB on macOS

```ruby
Vagrant.configure("2") do |config|
  config.vm.synced_folder ".", "/vagrant", type: "smb"
end
```

### Fix macOS SIP Issues

```bash
# Allow SMB sharing
# System Preferences > Sharing > File Sharing > Options
# Enable SMB sharing
```

### Provide Credentials

```ruby
config.vm.synced_folder ".", "/vagrant", type: "smb",
  smb_username: ENV["USER"],
  smb_password: "password"
```

### Use SMB3

```ruby
config.vm.synced_folder ".", "/vagrant", type: "smb",
  mount_options: ["vers=3.0"]
```

### Use rsync Fallback

```ruby
config.vm.synced_folder ".", "/vagrant", type: "rsync",
  rsync__auto: true
```

### Check SMB Status

```bash
# macOS
smb_status

# Linux
systemctl status smbd
```

## Examples

```ruby
# Full SMB configuration
Vagrant.configure("2") do |config|
  config.vm.synced_folder ".", "/vagrant", type: "smb",
    smb_username: "admin",
    smb_password: ENV["SMB_PASS"],
    mount_options: ["vers=3.0", "dir_mode=0775", "file_mode=0664"]
end
```
