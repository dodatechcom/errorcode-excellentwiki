---
title: "[Solution] Linux /etc/fstab Mount Failed — Boot Fix"
description: "Fix Linux '/etc/fstab: mount failed' errors. Recover from boot-time mount failures, fix fstab entries, and enter emergency mode."
platforms: ["linux"]
severities: ["critical"]
error-types: ["system-error"]
weight: 5
---

# Linux: /etc/fstab: mount failed

The `/etc/fstab: mount failed` error occurs during boot when the system tries to mount filesystems listed in `/etc/fstab` and one or more fail. The system may drop into emergency mode or recovery shell, requiring manual intervention.

## Common Causes

- Disk or partition no longer exists (device name changed)
- Filesystem not formatted or corrupted
- Incorrect filesystem type in fstab
- Network filesystem (NFS, CIFS) unavailable at boot time
- Incorrect UUID or device path
- Filesystem needs fsck (forced check)
- `nofail` option missing for non-critical mounts

## How to Fix

### 1. Enter Emergency Mode and Get a Shell

```bash
# When the system drops to emergency mode:
# Press Enter to get a shell
# Or enter root password
# Then remount root as read-write
mount -o remount,rw /
```

### 2. Identify the Failed Mount

```bash
# Check the mount status
mount -a -v 2>&1 | tail -20

# Check fstab entries
cat /etc/fstab

# Check what's currently mounted
mount

# Check kernel messages for mount errors
dmesg | tail -30
journalctl -xb | grep -i "mount"
```

### 3. Fix Invalid Device or UUID

```bash
# Find the correct UUID
blkid /dev/sda1

# Update /etc/fstab with the correct UUID
# Change:
# /dev/sda1 /boot ext4 defaults 0 2
# To:
# UUID=<correct-uuid> /boot ext4 defaults 0 2
```

### 4. Comment Out or Fix the Problematic Entry

```bash
# Edit fstab
nano /etc/fstab

# Comment out the problematic line with #
# For example:
# /dev/sdb1 /mnt/data ext4 defaults 0 2

# Or fix the device path or UUID
```

### 5. Add nofail for Non-Critical Mounts

```bash
# Add nofail option to prevent boot failure
# /mnt/data ext4 defaults,nofail 0 2
```

### 6. Check and Repair Filesystem

```bash
# Unmount the partition first (if possible)
umount /dev/sdb1

# Run fsck
fsck -f /dev/sdb1

# For ext4
e2fsck -f -y /dev/sdb1
```

### 7. Remove fstab Entry for Removed Drives

```bash
# If a drive was removed, delete the corresponding fstab line
# Or just comment it out with #
# Then run:
mount -a
# If no errors, the fix is complete
```

### 8. Fix Network Mounts (NFS, CIFS)

```bash
# For NFS mounts, add _netdev option
nfsserver:/export /mnt/nfs nfs defaults,_netdev,nofail 0 0

# For CIFS/SMB shares
//server/share /mnt/share cifs credentials=/etc/smbcreds,_netdev,nofail 0 0
```

## Examples

```bash
# Boot drops to emergency mode
# After entering root password:
mount -o remount,rw /
cat /etc/fstab | grep -v "^#"

# Found the bad entry:
# /dev/sdb1 /mnt/data ext4 defaults 0 2

blkid | grep sdb1
# No output — drive is missing

# Comment out the entry:
sed -i 's|^/dev/sdb1|#/dev/sdb1|' /etc/fstab

mount -a
# No errors — system can boot normally
```

```bash
# Incorrect UUID
cat /etc/fstab
UUID=wrong-uuid / ext4 defaults 0 1

# Find correct UUID
blkid /dev/sda2
/dev/sda2: UUID="correct-uuid" BLOCK_SIZE="4096" TYPE="ext4"

# Fix fstab
sed -i 's/wrong-uuid/correct-uuid/' /etc/fstab
mount -a
# Success
```

## Related Errors

- [GRUB errors]({{< relref "/os/linux/grub-error" >}}) — Boot-level failures
- [initramfs error]({{< relref "/os/linux/linux-initramfs-error" >}}) — Initial ramdisk mount failures
- [Read-only file system]({{< relref "/os/linux/readonly-filesystem" >}}) — Filesystem remounted read-only
