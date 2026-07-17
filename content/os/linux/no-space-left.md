---
title: "[Solution] Linux 'No Space Left on Device' — ENOSPC Fix"
description: "Fix Linux 'No space left on device' (ENOSPC) error. Find and remove large files, clear logs, and free disk space with these solutions."
platforms: ["linux"]
severities: ["critical"]
error-types: ["system-error"]
weight: 5
---

# Linux: No Space Left on Device (ENOSPC)

The error `No space left on device` (errno 28, ENOSPC) means the filesystem has run out of available space. This can be either disk blocks or inodes. When a filesystem fills up, you cannot write new files, and many system services will fail. This is a critical error that requires immediate attention.

## Common Causes

- Disk partition has reached 100% usage
- Inode exhaustion (too many small files even if disk space is available)
- Log files growing unbounded
- Large files in /var/log, /tmp, or /home
- Docker images or containers accumulating disk usage

## How to Fix

### 1. Check Disk Usage

First, identify which filesystem is full:

```bash
df -h
```

Example output:

```
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        50G   50G     0 100% /
tmpfs           3.9G     0  3.9G   0% /dev/shm
```

### 2. Find Large Files and Directories

Locate what's consuming the most space:

```bash
# Find the largest directories under root
sudo du -sh /* 2>/dev/null | sort -rh | head -20

# Find files larger than 100MB
sudo find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null

# Find files larger than 1GB
sudo find / -type f -size +1G -exec ls -lh {} \; 2>/dev/null
```

### 3. Clean Up Common Offenders

```bash
# Clear package manager cache (Debian/Ubuntu)
sudo apt clean
sudo apt autoclean

# Clear package manager cache (RHEL/CentOS/Fedora)
sudo dnf clean all

# Clear old journal logs
sudo journalctl --vacuum-size=100M

# Remove old log files
sudo truncate -s 0 /var/log/syslog
sudo find /var/log -name "*.gz" -delete

# Clear /tmp
sudo find /tmp -type f -atime +7 -delete
```

### 4. Check Inode Usage

If disk space is available but you still get ENOSPC, you may have inode exhaustion:

```bash
df -i
```

Fix inode exhaustion by removing large numbers of small files:

```bash
# Find directories with many files
sudo find /var/spool -type f | wc -l
sudo find /var/mail -type f | wc -l
```

### 5. Remove Old Kernels (Ubuntu/Debian)

```bash
# List installed kernels
dpkg --list 'linux-image*' | grep ^ii

# Remove old kernels (keep the current one)
sudo apt autoremove --purge
```

### 6. Expand the Filesystem

If you have available space on the disk but the partition is full:

```bash
# For LVM partitions
sudo lvextend -l +100%FREE /dev/mapper/vg-root
sudo resize2fs /dev/mapper/vg-root   # ext4
sudo xfs_growfs /                     # xfs
```

## Examples

```bash
$ df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        20G   20G     0 100% /

$ sudo du -sh /var/log
12G     /var/log

$ sudo journalctl --vacuum-size=100M
Vacuuming done, freed 11.5G of archived journals from /var/log/journal.

$ df -h /dev/sda1
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        20G  8.5G   11G  44% /
```

## Related Errors

- [Disk I/O error]({{< relref "/os/linux/disk-full2" >}}) — Physical disk failure or corruption
- [Read-only file system]({{< relref "/os/linux/readonly-filesystem" >}}) — Filesystem remounted read-only
- [Cannot allocate memory]({{< relref "/os/linux/cannot-allocate-memory" >}}) — System out of memory
