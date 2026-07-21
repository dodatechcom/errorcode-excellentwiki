---
title: "[Solution] Vagrant Shared Folder Permission Error"
description: "Fix Vagrant shared folder permission errors when the guest cannot access mounted directories."
tools: ["vagrant"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Vagrant Shared Folder Permission Error

A Vagrant shared folder permission error occurs when the guest VM cannot read or write to the synced folder.

## Why This Happens

- Incorrect folder ownership
- VirtualBox Guest Additions mismatch
- Sync type does not support permissions
- SELinux/AppArmor blocking access
- Folder not mounted properly

## Common Error Messages

- `vagrant_shared_folder_permission_error`
- `vagrant_synced_folder_access_denied`
- `vagrant_mount_permission_denied`
- `vagrant_shared_folder_not_mounted`

## How to Fix It

### Solution 1: Set Correct Ownership

```ruby
Vagrant.configure("2") do |config|
  config.vm.synced_folder ".", "/vagrant",
    owner: "vagrant",
    group: "vagrant",
    mount_options: ["dmode=755", "fmode=644"]
end
```

### Solution 2: Use NFS Sync

NFS preserves permissions better:

```ruby
config.vm.synced_folder ".", "/vagrant", type: "nfs"
```

### Solution 3: Fix SELinux Context

```bash
sudo setenforce 0  # Temporarily disable
# Or
sudo chcon -R -t httpd_sys_content_t /var/www
```

### Solution 4: Manually Mount

```bash
# On guest
sudo mount -t vboxsf -o uid=1000,gid=1000 vagrant /vagrant
```

## Common Scenarios

- **Read-only folder:** Check mount_options permissions
- **Ownership mismatch:** Set owner and group
- **SELinux blocks:** Adjust SELinux context

## Prevent It

- Specify owner/group in synced_folder config
- Use appropriate sync type for your needs
- Test folder access after vagrant up
