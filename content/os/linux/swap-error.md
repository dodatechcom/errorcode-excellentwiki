---
title: "[Solution] Linux Swap Not Working / swapon Failed — Fix"
description: "Fix Linux 'swap not working' and 'swapon failed' errors. Create swap files, enable swap partitions, and fix swap configuration issues."
platforms: ["linux"]
severities: ["error"]
error-types: ["system-error"]
weight: 5
---

# Linux: Swap not working / swapon failed

The `swap not working` or `swapon failed` error means the system cannot enable or use swap space. Swap is virtual memory on disk that supplements physical RAM. Without it, the system has no fallback when RAM is full, and the OOM killer will terminate processes instead of swapping them out. Common `swapon` failure messages include `swapon: /swapfile: swapon failed: Invalid argument` or `device or resource busy`.

## Common Causes

- Swap file has incorrect permissions (must be 600)
- Swap file is not formatted (missing mkswap)
- Swap partition is not in /etc/fstab
- Filesystem doesn't support swap (e.g., Btrfs, ZFS)
- Duplicate swap entries in /etc/fstab
- Swap file is too small or on a filesystem with nocont flag

## How to Fix

### 1. Check Current Swap Status

```bash
# Check if swap is enabled
sudo swapon --show
free -h

# Check all swap devices and files
cat /proc/swaps

# Check fstab for swap entries
grep swap /etc/fstab
```

### 2. Create a Swap File

```bash
# Create a 4GB swap file
sudo fallocate -l 4G /swapfile
# If fallocate doesn't work (e.g., on Btrfs), use dd:
# sudo dd if=/dev/zero of=/swapfile bs=1M count=4096

# Set correct permissions (critical!)
sudo chmod 600 /swapfile

# Format as swap
sudo mkswap /swapfile

# Enable swap
sudo swapon /swapfile

# Verify
sudo swapon --show
free -h
```

### 3. Make Swap Persistent in /etc/fstab

```bash
# Add to /etc/fstab
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab

# Or for a swap partition
echo '/dev/sda2 none swap sw 0 0' | sudo tee -a /etc/fstab

# Test the fstab entry
sudo mount -a
```

### 4. Fix Swap File on Btrfs

Btrfs requires special handling for swap files:

```bash
# Disable CoW on the swap file first
sudo chattr +C /swapfile

# Or create swap on a dedicated partition (preferred for Btrfs)
sudo mkswap /dev/sdb2
sudo swapon /dev/sdb2
```

### 5. Fix "Invalid Argument" Error

This usually means the swap file is corrupted or wrong size:

```bash
# Disable and recreate
sudo swapoff /swapfile
sudo rm /swapfile
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```

### 6. Fix "Device or Resource Busy"

```bash
# Find what's using the swap
sudo lsof /swapfile

# Stop any process using it, then:
sudo swapoff /swapfile
sudo swapon /swapfile
```

### 7. Enable Swap Partition

```bash
# List all partitions
lsblk

# Format as swap
sudo mkswap /dev/sdb2

# Enable
sudo swapon /dev/sdb2

# Add to fstab for persistence
echo '/dev/sdb2 none swap sw 0 0' | sudo tee -a /etc/fstab
```

### 8. Fix Duplicate Swap Entries

```bash
# Check for duplicates
grep -n swap /etc/fstab

# Remove duplicate lines, keeping only one valid swap entry
sudo nano /etc/fstab
```

### 9. Adjust Swappiness

Control how aggressively the kernel uses swap:

```bash
# Check current swappiness
cat /proc/sys/vm/swappiness

# Set to 10 (use swap less, prefer RAM)
sudo sysctl vm.swappiness=10

# Make persistent
echo "vm.swappiness=10" | sudo tee -a /etc/sysctl.conf
```

## Examples

```bash
$ sudo swapon /swapfile
swapon: /swapfile: swapon failed: Invalid argument

# Check permissions:
$ ls -la /swapfile
-rw-r--r-- 1 root root 4294967296 Jun 15 10:00 /swapfile

# Fix permissions:
$ sudo chmod 600 /swapfile
$ sudo mkswap /swapfile
$ sudo swapon /swapfile
$ free -h
              total        used        free      shared  buff/cache   available
Mem:           16Gi       8.0Gi       4.0Gi       200Mi       4.0Gi       7.5Gi
Swap:         4.0Gi         0B       4.0Gi
```

## Related Errors

- [Out of memory / OOM killer]({{< relref "/os/linux/oom-killer" >}}) — Process killed when swap is full
- [Cannot allocate memory]({{< relref "/os/linux/cannot-allocate-memory" >}}) — Memory allocation failure
- [No space left on device]({{< relref "/os/linux/no-space-left" >}}) — Disk full preventing swap creation
