---
title: "[Solution] Linux SELinux Context Labeling Error"
description: "Fix Linux SELinux 'context labeling error' and AVC denial messages. Resolve SELinux context mismatches and restore file labels."
platforms: ["linux"]
severities: ["warning"]
error-types: ["system-error"]
tags: ["selinux", "context", "labeling", "avc", "policy"]
weight: 5
---

# Linux: SELinux — context labeling error

The `SELinux: context labeling error` or `AVC: denied` messages indicate that SELinux has denied an operation because the security context (label) of a file, process, or resource does not match the expected policy. SELinux uses Mandatory Access Control (MAC) to enforce strict rules on what processes can access.

## What This Error Means

Every file and process in an SELinux-enforced system has a security context consisting of `user:role:type:level`. When a process tries to access a resource, SELinux checks whether the process's type is permitted to access the resource's type according to the loaded policy. A context labeling error means a file was created or copied without the correct SELinux label, or the policy does not allow the access.

## Common Causes

- Files copied with `cp` instead of `cp --preserve=context`
- Files restored from backup without correct labels
- Custom applications running in non-standard directories
- SELinux policy does not account for the service or port
- Boolean settings not configured for the use case
- Container or Docker volumes with incorrect labels

## How to Fix

### 1. Identify the Denial

```bash
# View recent AVC denials
sudo ausearch -m AVC -ts recent

# Check the audit log
sudo grep 'avc: denied' /var/log/audit/audit.log

# Use ausearch with more context
sudo ausearch -m AVC -ts today --interpret
```

### 2. Restore File Contexts

```bash
# Restore default context for a file
sudo restorecon -v /path/to/file

# Restore recursively
sudo restorecon -Rv /var/www/html

# List current context
ls -Z /path/to/file

# Restore all mislabeled files
sudo restorecon -Rv /
```

### 3. Set Custom Contexts

```bash
# Set a specific context for a custom directory
sudo semanage fcontext -a -t httpd_sys_content_t '/srv/myapp(/.*)?'

# Apply the context
sudo restorecon -Rv /srv/myapp

# Verify
ls -Z /srv/myapp
```

### 4. Configure SELinux Booleans

```bash
# List booleans related to a service
getsebool -a | grep httpd

# Enable a boolean
sudo setsebool -P httpd_can_network_connect on

# Common booleans:
# httpd_can_network_connect   - Allow httpd to make network connections
# httpd_can_network_connect_db - Allow httpd to connect to databases
# ssh_use_password_auth        - Allow sshd password auth
# nfs_use_nfs                  - Allow NFS client usage
```

### 5. Fix Port Labeling

```bash
# If a service runs on a non-standard port
sudo semanage port -a -t http_port_t -p tcp 8080

# List current port labels
sudo semanage port -l | grep http

# Remove a port label
sudo semanage port -d -t http_port_t -p tcp 8080
```

### 6. Generate a Custom Policy Module

```bash
# Generate policy from denials
sudo ausearch -m AVC -ts today | audit2allow -M mymodule

# Review the generated policy
cat mymodule.te

# Install the module
sudo semodule -i mymodule.pp

# Remove later
sudo semodule -r mymodule
```

### 7. Disable SELinux Temporarily (Debugging Only)

```bash
# Check current mode
getenforce

# Set to permissive (logs but does not enforce)
sudo setenforce 0

# For persistent change, edit /etc/selinux/config
# SELINUX=permissive

# After debugging, re-enable
sudo setenforce 1
```

## Examples

```bash
$ sudo ausearch -m AVC -ts recent
type=AVC msg=audit(1721000000.123:456): avc: denied { read } for
  pid=1234 comm="httpd" name="index.html" dev="sda1" ino=789
  scontext=system_u:system_r:httpd_t:s0
  tcontext=unconfined_u:object_r:default_t:s0 tclass=file

$ ls -Z /srv/myapp/index.html
unconfined_u:object_r:default_t:s0 /srv/myapp/index.html

$ sudo semanage fcontext -a -t httpd_sys_content_t '/srv/myapp(/.*)?'
$ sudo restorecon -Rv /srv/myapp
$ ls -Z /srv/myapp/index.html
system_u:object_r:httpd_sys_content_t:s0 /srv/myapp/index.html
```

## Related Errors

- [SELinux denied]({{< relref "/os/linux/linux-selinux-denied" >}}) — SELinux access denials
- [Permission denied]({{< relref "/os/linux/permission-denied10" >}}) — General permission issues
- [Docker permission denied]({{< relref "/os/linux/linux-docker-error" >}}) — Docker access issues
