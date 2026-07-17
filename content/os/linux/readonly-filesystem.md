---
title: "[Solution] Linux Read-Only File System — Remount Read-Write Fix"
description: "Fix Linux 'Read-only file system' errors. Remount filesystems as read-write, fix filesystem errors, and resolve mount issues."
platforms: ["linux"]
severities: ["error"]
error-types: ["system-error"]
weight: 5
---

# Linux: Read-Only File System

The `Read-only file system` error (EROFS) means the system tried to write to a filesystem that is mounted as read-only. This can happen because the filesystem was explicitly mounted read-only, the kernel detected corruption and remounted it read-only for safety, or a hardware issue prevented writes. Until the underlying cause is fixed, all write operations to that filesystem will fail.

## Common Causes

- Filesystem has errors and was remounted read-only by the kernel
- Explicit mount option `ro` was used
- Disk hardware failure triggering read-only fallback
- NFS or network filesystem server unreachable
- `/etc/fstab` misconfiguration
- Filesystem corruption from power loss

## How to Fix

### 1. Check Which Filesystems Are Read-Only

```bash
# Check mount status
mount | grep "ro,"

# Or check specific mount points
mount | grep " / "
```

Example output:

```
/dev/sda1 on / type ext4 (ro,relatime,errors=remount-ro)
```

The `ro` flag confirms the filesystem is read-only.

### 2. Remount as Read-Write

```bash
# Remount root filesystem as read-write
sudo mount -o remount,rw /

# Remount a specific partition
sudo mount -o remount,rw /home
```

If this fails with errors, the filesystem likely has corruption — proceed to step 3.

### 3. Run Filesystem Check

**Boot from a live USB for the root filesystem.** For non-root partitions:

```bash
# Unmount first
sudo umount /dev/sda1

# Run filesystem check
sudo fsck -f /dev/sda1

# Remount after repair
sudo mount /dev/sda1 /mount/point
```

For ext4 filesystems with specific repair options:

```bash
sudo e2fsck -f -y /dev/sda1
```

### 4. Check for Hardware Issues

```bash
# Check disk health
sudo smartctl -H /dev/sda

# Check kernel logs for disk errors
dmesg | grep -iE 'error|readonly|read.only|i/o|ata'
```

If the disk is failing, back up data immediately and replace it.

### 5. Check NFS / Network Filesystems

If the read-only filesystem is NFS:

```bash
# Check NFS server status
showmount -e nfsserver

# Check NFS mount options
mount | grep nfs

# Try remounting with hard,intr options
sudo mount -o remount,rw,nfs nfsserver:/exported/path /mnt/nfs
```

### 6. Fix /etc/fstab Errors

If the wrong mount options were set in fstab:

```bash
# Edit fstab
sudo nano /etc/fstab

# Ensure the options field uses "rw" for writable partitions
# Example:
# /dev/sda1 / ext4 defaults,rw 0 1

# Test fstab without rebooting
sudo mount -a
```

### 7. Enable Writing on Protected Filesystems

For filesystems that should be read-only by design (like SquashFS):

```bash
# These cannot be made writable — check if you need a different filesystem type
# Or use overlayfs for temporary writable layer
sudo mount -t overlay overlay -o lowerdir=/squashfs,upperdir=/tmp/upper,workdir=/tmp/work /mnt/overlay
```

## Examples

```bash
$ touch /tmp/test.txt
touch: cannot touch '/tmp/test.txt': Read-only file system

$ mount | grep " / "
/dev/sda2 on / type ext4 (ro,relatime,errors=remount-ro)

$ sudo mount -o remount,rw /

$ touch /tmp/test.txt
$ echo "success" > /tmp/test.txt
```

## Related Errors

- [Disk I/O error]({{< relref "/os/linux/disk-full2" >}}) — Physical disk failure causing read-only fallback
- [Permission denied]({{< relref "/os/linux/permission-denied10" >}}) — Permission issues (not filesystem-level)
- [NFS not responding]({{< relref "/os/linux/nfs-error" >}}) — Network filesystem server down
