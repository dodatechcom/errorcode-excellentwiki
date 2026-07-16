---
title: "[Solution] Linux EACCES (errno 13) — Permission Denied Fix"
description: "Fix Linux EACCES (errno 13) Permission Denied error. Fix file permissions, ownership, and access control issues with these solutions."
platforms: ["linux"]
severities: ["error"]
error_types: ["runtime"]
tags: ["eacces", "errno-13", "permission-denied"]
weight: 30
---

# Linux EACCES (errno 13) — Permission Denied

EACCES (errno 13) means the kernel denied access to a file or directory because the calling process lacks the necessary permissions. Unlike EPERM (errno 1), which indicates you need root or special capabilities, EACCES specifically means the file or directory exists but your user account does not have the right access bits set. This is the "Permission denied" error most users encounter in daily Linux use.

## Common Causes

- File permissions do not include read, write, or execute for your user
- Directory execute permission is missing (needed to traverse into it)
- File or directory is owned by another user
- Access Control Lists (ACLs) are blocking access
- Filesystem mounted with restrictive options like `noexec` or `nosuid`
- Sticky bit is set on a shared directory

## How to Fix EACCES

### 1. Check Current File Permissions

Always start by inspecting the permissions of the target file or directory:

```bash
ls -la /path/to/problem/file
```

Example output:

```
-rw-r--r-- 1 alice developers 4096 Jun 15 10:00 report.txt
-rwxr-x--- 1 bob    developers 4096 Jun 15 10:00 script.sh
drwxr-xr-x 2 root   root       4096 Jun 15 10:00 system_dir
```

The first character block shows the type and permissions: owner (rwx), group (rwx), others (rwx).

### 2. Change Permissions with chmod

Grant the access your user needs:

```bash
# Give owner full permissions, group and others read+execute
chmod 755 /path/to/directory

# Give owner read/write, group read, others nothing
chmod 640 /path/to/file

# Make a script executable
chmod +x /path/to/script.sh

# Recursive permission change (use with caution)
chmod -R u+rwx /path/to/directory
```

### 3. Change File Ownership with chown

If the file is owned by another user, change ownership:

```bash
# Change owner
sudo chown alice /path/to/file

# Change owner and group
sudo chown alice:developers /path/to/file

# Recursive ownership change
sudo chown -R alice:developers /path/to/directory
```

### 4. Fix Directory Execute Permission

To access files inside a directory, you need execute (`x`) permission on every parent directory in the path:

```bash
# You need +x on each directory to reach the file
chmod +x /path
chmod +x /path/to
chmod +x /path/to/directory
```

Without execute on a directory, you cannot list its contents or enter it, even if you have read permission.

### 5. Check and Modify Access Control Lists (ACLs)

ACLs provide fine-grained permissions beyond standard Unix permissions:

```bash
# View ACLs on a file
getfacl /path/to/file

# Grant a specific user read access
setfacl -m u:alice:r /path/to/file

# Grant a specific user full access
setfacl -m u:alice:rwx /path/to/file

# Remove all ACLs
setfacl -b /path/to/file
```

### 6. Check Filesystem Mount Options

A filesystem mounted with restrictive options can cause EACCES regardless of file permissions:

```bash
# Check mount options for the filesystem containing the file
mount | grep "$(df /path/to/file | tail -1 | awk '{print $1}')"
```

Common restrictive options:

| Option | Effect |
|--------|--------|
| `noexec` | Cannot execute files on the filesystem |
| `nosuid` | Ignores SUID/SGID bits |
| `ro` | Read-only mount |

Remount with permissive options if appropriate:

```bash
sudo mount -o remount,rw /mount/point
```

### 7. Check the Sticky Bit

In directories with the sticky bit set (like `/tmp`), only the file owner, directory owner, or root can delete files:

```bash
# Check if sticky bit is set
ls -ld /path/to/directory

# Remove sticky bit (requires root)
sudo chmod -t /path/to/directory

# Set sticky bit back
sudo chmod +t /path/to/directory
```

### 8. Temporarily Elevate with sudo

For one-time fixes, use `sudo` to perform the operation as root:

```bash
sudo chmod 755 /path/to/directory
sudo chown alice:developers /path/to/file
```

## Troubleshooting Workflow

```bash
# Step 1: Check permissions
ls -la /path/to/problem

# Step 2: Check if you are in the correct group
groups $(whoami)

# Step 3: Check ACLs
getfacl /path/to/problem

# Step 4: Check mount options
mount | grep "$(df /path/to/problem | tail -1 | awk '{print $1}')"

# Step 5: Apply the appropriate fix
sudo chmod / chown / setfacl as needed
```

## Related Error Codes

- [EPERM (errno 1)](/os/linux/errno-1/) — Operation not permitted (privilege issue)
- [ENOENT (errno 2)](/os/linux/errno-2/) — File not found
- [EIO (errno 5)](/os/linux/errno-5/) — Input/output error
