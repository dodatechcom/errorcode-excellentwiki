---
title: "[Solution] Linux ENOSPC (errno 28) — No Space Left on Device Fix"
description: "Fix Linux ENOSPC (errno 28) No Space Left on Device error. Find large files, clean disk space, and manage storage."
platforms: ["linux"]
severities: ["error"]
error_types: ["runtime"]
weight: 60
---

# Linux ENOSPC (errno 28) — No Space Left on Device

ENOSPC (errno 28) means the filesystem has no remaining space for new data. This applies to both disk space and inodes — a filesystem can run out of either one independently. The error appears when writing files, creating directories, or even when running programs that need to write temporary data. On servers, this can cause cascading failures including database crashes and log loss.

## Common Causes

- Disk volume is full of data
- Inode table is exhausted (too many small files)
- Log files growing without rotation
- Deleted files still held open by processes
- Docker images and containers consuming disk
- Journal or temp files accumulating
- Snapshots or backups consuming space

## How to Fix ENOSPC

### 1. Check Disk Space Usage

First determine which filesystem is full:

```bash
# Show disk usage in human-readable format
df -h

# Show usage for a specific path
df -h /var
```

Example output:

```
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        50G   48G  0G  100% /
/dev/sdb1      200G  120G  80G   60% /data
```

### 2. Check Inode Usage

A filesystem can run out of inodes even with free disk space:

```bash
# Check inode usage
df -i
```

Example output:

```
Filesystem      Inodes  IUsed   IFree IUse% Mounted on
/dev/sda1      3276800 3276800      0  100% /
```

If IUse% is 100%, there are too many files. Find the directory with the most files:

```bash
# Find directories with the most files
sudo find / -xdev -type d -exec sh -c 'echo "$(find "$1" -maxdepth 1 | wc -l) $1"' _ {} \; | sort -rn | head -20
```

### 3. Find the Largest Files and Directories

Identify what is consuming disk space:

```bash
# Find the largest directories from root
sudo du -h --max-depth=1 / 2>/dev/null | sort -hr | head -20

# Find the largest files on the filesystem
sudo find / -xdev -type f -exec du -h {} + 2>/dev/null | sort -hr | head -20
```

For an interactive visual view:

```bash
# Install ncdu (NCurses Disk Usage)
sudo apt install ncdu    # Debian/Ubuntu
sudo dnf install ncdu    # RHEL/Fedora

# Scan and browse disk usage interactively
sudo ncdu /
```

### 4. Clean Log Files

Logs are a common cause of disk fill-up:

```bash
# Check log directory size
du -sh /var/log/

# Truncate the largest log file (keeps the file, frees space)
sudo truncate -s 0 /var/log/syslog

# Remove old rotated logs
sudo find /var/log -name "*.gz" -delete
sudo find /var/log -name "*.old" -delete

# Clean all old journal logs older than 3 days
sudo journalctl --vacuum-time=3d

# Limit journal size to 500MB
sudo journalctl --vacuum-size=500M
```

### 5. Remove Old Packages and Caches

Package managers cache downloaded archives:

```bash
# Clean apt cache (Debian/Ubuntu)
sudo apt clean
sudo apt autoclean

# Remove unused packages
sudo apt autoremove

# Clean dnf cache (RHEL/Fedora)
sudo dnf clean all

# Remove old kernels
sudo dnf remove $(dnf repoquery --installonly --latest-limit=-2)
```

### 6. Handle Deleted Files Still in Use

Files deleted with `rm` still consume space if a process holds them open:

```bash
# Find deleted files still held open by processes
sudo lsof | grep "(deleted)"

# Truncate a specific deleted file to free space
sudo truncate -s 0 /proc/<PID>/fd/<FD>

# Or restart the process holding the file
sudo systemctl restart service-name
```

### 7. Clean Docker Disk Usage

Docker can consume large amounts of disk:

```bash
# Check Docker disk usage
docker system df

# Remove unused containers, networks, images, and build cache
docker system prune -a

# Remove all unused volumes (careful — this deletes data)
docker volume prune
```

### 8. Free Space in /tmp

The temporary directory can fill up:

```bash
# Check /tmp size
du -sh /tmp

# Remove files older than 7 days
sudo find /tmp -type f -atime +7 -delete

# Remove old directory contents
sudo find /tmp -mindepth 1 -maxdepth 1 -exec rm -rf {} +
```

### 9. Find and Remove Large Core Dumps

Core dumps can be very large:

```bash
# Find core dumps
sudo find / -name "core" -o -name "core.*" 2>/dev/null

# Remove them
sudo find / -name "core" -o -name "core.*" -delete 2>/dev/null
```

### 10. Add More Disk Space

If cleanup is not enough, consider adding space:

```bash
# Add a new disk and create a partition
sudo fdisk /dev/sdb

# Format and mount
sudo mkfs.ext4 /dev/sdb1
sudo mkdir /mnt/extra
sudo mount /dev/sdb1 /mnt/extra

# Add to fstab for persistence
echo '/dev/sdb1 /mnt/extra ext4 defaults 0 2' | sudo tee -a /etc/fstab
```

## Prevention: Set Up Alerts

Monitor disk usage proactively:

```bash
# Simple cron job to alert when disk is above 85%
echo '*/30 * * * * root df -h / | awk "NR==2 && \$5+0 > 85 {print}" | mail -s "Disk Alert" admin@example.com' | sudo tee /etc/cron.d/disk-alert
```

## Related Error Codes

- [EIO (errno 5)](/os/linux/errno-5/) — Input/output error
- [ENOMEM (errno 12)](/os/linux/errno-12/) — Out of memory
- [EPERM (errno 1)](/os/linux/errno-1/) — Operation not permitted
