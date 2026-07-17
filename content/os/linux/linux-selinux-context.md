---
title: "[Solution] Linux SELinux Context Error — Wrong Label Fix"
description: "Fix Linux SELinux context errors. Correct file labels, set security contexts, and resolve 'file has an invalid context' warnings."
platforms: ["linux"]
severities: ["error"]
error-types: ["system-error"]
tags: ["selinux", "context", "file-context", "security", "label"]
weight: 5
---

# Linux: SELinux context error

SELinux context errors occur when a file or process has an incorrect or missing security context label. Every file, process, and port in SELinux has a context consisting of user:role:type:level. When the type doesn't match what the policy expects, access is denied.

## Common Causes

- Files copied or moved from a non-standard location (lost context)
- Restored backup files without SELinux labels
- Files created in a directory without proper default context
- Incorrect manual context assignment
- Application installed to a non-default path
- Files transferred from another system via rsync/scp (lost context)

## How to Fix

### 1. Check the Current Context

```bash
# View SELinux context of a file
ls -Z /path/to/file
# Example output: unconfined_u:object_r:httpd_sys_content_t:s0

# View context of a process
ps axZ | grep httpd
```

### 2. Restore Default Context

```bash
# Restore default context recursively
sudo restorecon -Rv /var/www/html

# Preview what would change (dry run)
sudo restorecon -nv /var/www/html

# Restore context of a single file
sudo restorecon -v /etc/myapp.conf
```

### 3. Set Context for Custom Paths

```bash
# Set default context for a custom directory
sudo semanage fcontext -a -t httpd_sys_content_t "/srv/web(/.*)?"

# Apply the context
sudo restorecon -Rv /srv/web

# Set context for a specific file type
sudo semanage fcontext -a -t httpd_sys_content_t "/srv/web/.*\.html"

# Apply
sudo restorecon -Rv /srv/web
```

### 4. Fix Context After Copy or Move

```bash
# Files copied with cp preserve context (use cp -Z to set as target)
# Files moved with mv preserve context

# After copying, restore context
sudo restorecon -Rv /destination/path

# Copy with new context
cp -Z /source/file /destination/

# Or set context explicitly
sudo chcon -t httpd_sys_content_t /path/to/file
```

### 5. Check SELinux File Context Definitions

```bash
# List all file context definitions
sudo semanage fcontext -l | grep httpd

# List contexts for a specific directory
sudo matchpathcon /var/www/html/index.html
```

### 6. Create Custom File Context Policy

```bash
# If a non-standard path needs a specific label
sudo semanage fcontext -a -t myservice_var_t "/opt/myapp/data(/.*)?"
sudo restorecon -Rv /opt/myapp/data

# Check if the type exists
seinfo -tmyservice_var_t 2>/dev/null || echo "Type exists"
```

### 7. Fix Labeled NFS or Samba Mounts

```bash
# For NFS mounts with SELinux
sudo setsebool -P nfs_export_all_rw 1

# For Samba
sudo setsebool -P samba_export_all_rw 1

# Set context for mount point
sudo semanage fcontext -a -t public_content_rw_t "/mnt/nfs(/.*)?"
sudo restorecon -Rv /mnt/nfs
```

## Examples

```bash
$ ls -Z /var/www/html/index.html
-rw-r--r--. root root unconfined_u:object_r:user_home_t:s0 /var/www/html/index.html

# Wrong context — should be httpd_sys_content_t for web content

$ sudo restorecon -v /var/www/html/index.html
restorecon reset /var/www/html/index.html context unconfined_u:object_r:user_home_t:s0->unconfined_u:object_r:httpd_sys_content_t:s0

$ ls -Z /var/www/html/index.html
-rw-r--r--. root root unconfined_u:object_r:httpd_sys_content_t:s0 /var/www/html/index.html
```

```bash
# Setting up a custom web directory
$ sudo semanage fcontext -a -t httpd_sys_content_t "/opt/webapp(/.*)?"
$ sudo restorecon -Rv /opt/webapp
```

## Related Errors

- [SELinux denied]({{< relref "/os/linux/selinux-denied" >}}) — Access denied by SELinux policy
- [Permission denied]({{< relref "/os/linux/permission-denied10" >}}) — Unix permission issues
- [NFS mount error]({{< relref "/os/linux/linux-nfs-mount-error" >}}) — Mount failures with SELinux interactions
