---
title: "[Solution] Linux ENOENT (errno 2) — No Such File or Directory Fix"
description: "Fix Linux ENOENT (errno 2) No Such File or Directory error. Troubleshoot missing files, incorrect paths, and broken symlinks."
platforms: ["linux"]
severities: ["error"]
error_types: ["runtime"]
tags: ["enoent", "errno-2", "file-not-found", "path"]
weight: 20
---

# Linux ENOENT (errno 2) — No Such File or Directory

ENOENT (errno 2) is returned when the kernel cannot find a file or directory at the path you specified. This is one of the most common errors in Linux and can be triggered by typos, missing mount points, broken symlinks, incorrect working directories, or programs referencing files that have been removed. The error applies to both files and directories — including parent directories in the path.

## Common Causes

- Typo in the file or directory name
- Incorrect absolute or relative path
- File was deleted or moved
- Broken symbolic link
- Working directory changed unexpectedly in a script
- Network mount or NFS share not mounted
- Mount point does not exist

## How to Fix ENOENT

### 1. Verify the File Path Exists

Double-check the exact path. Use `ls` to inspect each directory component:

```bash
ls -la /path/to/problem/file
```

If the path contains multiple directories, check each one:

```bash
ls -la /path/to/
ls -la /path/to/problem/
```

### 2. Use find to Locate the File

If you know the filename but not the location:

```bash
# Search the entire filesystem
sudo find / -name "filename" 2>/dev/null

# Search only in /home
find /home -name "filename" 2>/dev/null

# Case-insensitive search
find / -iname "filename" 2>/dev/null

# Search by partial name using wildcard
find / -name "*.conf" -path "*/nginx/*" 2>/dev/null
```

### 3. Check for Typos

Use `tab` completion in the terminal to auto-complete paths. This prevents typos:

```bash
# Instead of typing the full path, type the first few characters and press Tab
cat /etc/na<Tab>
```

Verify the exact filename with:

```bash
# List files matching a pattern
ls /etc/na*
```

### 4. Check if the File Is a Broken Symlink

Symbolic links can point to targets that no longer exist:

```bash
# Check if a path is a symlink
ls -la /path/to/link

# Find broken symlinks in a directory
find /path/to/dir -type l ! -exec test -e {} \; -print
```

Fix broken symlinks by recreating them:

```bash
# Remove the broken link
rm /path/to/broken/link

# Recreate it with the correct target
ln -s /correct/target/path /path/to/new/link
```

### 5. Verify the Working Directory

Scripts often use relative paths. Make sure the working directory is what you expect:

```bash
# Print current directory
pwd

# Change to the expected directory before running commands
cd /path/to/expected/directory
ls -la
```

In scripts, use absolute paths or set the working directory explicitly:

```bash
#!/bin/bash
cd /path/to/project || exit 1
make
```

### 6. Check Mount Points and Network Filesystems

If the file lives on a mounted filesystem, verify the mount is active:

```bash
# Show all mounted filesystems
df -h

# Check if a specific mount point is active
mountpoint -q /mnt/data && echo "Mounted" || echo "Not mounted"
```

Mount missing network filesystems:

```bash
# Mount an NFS share
sudo mount -t nfs server:/share /mnt/nfs

# Mount an SMB/CIFS share
sudo mount -t cifs //server/share /mnt/smb -o username=user
```

### 7. Check PATH for Missing Binaries

When you get ENOENT running a command (not a file operation), the binary may not be in your `$PATH`:

```bash
# Check if the command exists
which command_name

# Search for it in PATH
type command_name

# Check your PATH variable
echo $PATH
```

Install missing packages:

```bash
# Debian/Ubuntu
sudo apt install package-name

# RHEL/CentOS/Fedora
sudo dnf install package-name
```

### 8. Use strace to Diagnose the Exact Path

Trace system calls to see exactly which path the program tried to access:

```bash
strace -e openat failing_command 2>&1 | grep ENOENT
```

This shows the exact filename or directory the process looked for.

## Verification

After fixing the issue, confirm the file is accessible:

```bash
# Test that the file is readable
cat /path/to/fixed/file

# Test that a command runs without ENOENT
command_name --version
```

## Related Error Codes

- [EACCES (errno 13)](/os/linux/errno-13/) — Permission denied
- [EPERM (errno 1)](/os/linux/errno-1/) — Operation not permitted
- [ENOSPC (errno 28)](/os/linux/errno-28/) — No space left on device
