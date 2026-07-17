---
title: "[Solution] Linux No Space Left on Device — Disk Full Fix v2"
description: "Fix Linux 'No space left on device' errors. Free disk space, remove large files, clean package cache, and expand filesystems."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["disk-full", "no-space", "inode-exhaustion", "filesystem", "disk-usage"]
weight: 5
---

# Linux: No space left on device

The `No space left on device` error means the filesystem has run out of space or inodes. Even if a disk has free space, a full filesystem will refuse all write operations — no new files can be created, logs cannot be written, and applications may crash or fail to start.

## Common Causes

- Log files consuming all available disk space
- Package manager cache not cleaned regularly
- Large temporary files in `/tmp` or `/var/tmp`
- Database transaction logs growing unchecked
- Docker images and containers accumulating
- Inode exhaustion (many small files)
- Root filesystem full due to user data

## How to Fix

### 1. Check Disk Usage

```bash
# Check overall disk usage
df -h

# Check inode usage
df -i

# Find largest directories
du -sh /* 2>/dev/null | sort -rh | head -10
du -sh /var/* 2>/dev/null | sort -rh | head -10
du -sh /home/* 2>/dev/null | sort -rh | head -10
```

### 2. Clean Package Cache

```bash
# Debian/Ubuntu
sudo apt clean
sudo apt autoremove --purge

# Fedora/RHEL
sudo dnf clean all
sudo dnf autoremove

# Arch
sudo pacman -Sc
sudo pacman -Scc   # More aggressive
```

### 3. Clean Log Files

```bash
# Check log sizes
du -sh /var/log/*

# Truncate large logs safely
sudo truncate -s 0 /var/log/syslog
sudo truncate -s 0 /var/log/auth.log
sudo truncate -s 0 /var/log/kern.log

# Rotate logs manually
sudo logrotate -f /etc/logrotate.conf

# Clean journal logs (systemd)
sudo journalctl --vacuum-time=7d
sudo journalctl --vacuum-size=500M
```

### 4. Clean Docker (if installed)

```bash
# Check Docker disk usage
docker system df

# Remove unused containers, images, and volumes
docker system prune -a --volumes

# Remove stopped containers
docker container prune

# Remove unused images
docker image prune -a
```

### 5. Clean /tmp and Cache

```bash
# Remove temporary files (safe on reboot)
sudo rm -rf /tmp/*
sudo rm -rf /var/tmp/*

# Clean user cache
rm -rf ~/.cache/*
sudo rm -rf /root/.cache/*

# Clean thumbnail cache
rm -rf ~/.thumbnails/*
rm -rf ~/.cache/thumbnails/*
```

### 6. Check for Large Old Files

```bash
# Find files larger than 1GB
find / -type f -size +1G -exec ls -lh {} \; 2>/dev/null | sort -rh | head -20

# Find files modified over 90 days ago in /var
find /var -type f -mtime +90 -exec ls -lh {} \; 2>/dev/null | sort -rh | head -20

# Find core dumps
find / -name "core.*" -o -name "*.core" 2>/dev/null
```

### 7. Expand Filesystem (LVM)

```bash
# Check if using LVM
sudo lvdisplay

# Extend logical volume
sudo lvextend -L +10G /dev/vgname/lvname

# Resize filesystem
sudo resize2fs /dev/vgname/lvname   # ext4
sudo xfs_growfs /mount/point         # XFS
```

### 8. Handle Inode Exhaustion

```bash
# Check inode usage
df -i /dev/sda1

# Find directories with many small files
find / -xdev -type d -exec sh -c 'echo "$(ls -1A "$1" | wc -l) $1"' _ {} \; | sort -rn | head -20

# Clean up mail spools
sudo find /var/spool/mail -type f -delete
```

## Examples

```bash
$ df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        50G   50G     0 100% /

$ df -i
Filesystem     Inodes IUsed IFree IUse% Mounted on
/dev/sda1      3.2M  2.1M  1.1M   66% /

$ du -sh /var/log/* | sort -rh | head -5
4.5G    /var/log/syslog
1.2G    /var/log/journal
800M    /var/log/apache2

$ sudo truncate -s 0 /var/log/syslog
$ df -h
/dev/sda1        50G   45G   5G  90% /
```

## Related Errors

- [Read-only file system]({{< relref "/os/linux/readonly-filesystem" >}}) — Filesystem remounted read-only
- [Too many open files]({{< relref "/os/linux/too-many-open-files" >}}) — File descriptor exhaustion
- [Swap error]({{< relref "/os/linux/swap-error" >}}) — Swap space issues
