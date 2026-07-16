---
title: "[Solution] Linux EBUSY (errno 16) — Device or Resource Busy Fix"
description: "Fix Linux EBUSY (errno 16) Device or Resource Busy error. Find locking processes, unmount devices, and release file locks."
platforms: ["linux"]
severities: ["error"]
error_types: ["runtime"]
tags: ["ebusy", "errno-16", "device-busy", "resource-busy", "umount"]
weight: 60
---

# Linux EBUSY (errno 16) — Device or Resource Busy

EBUSY (errno 16) means you tried to use a resource that is currently locked or in use by another process. This error appears when attempting to unmount a filesystem, remove a disk, delete a file held open by a running program, or modify a device that is actively being written to. On servers, EBUSY is a frequent obstacle during deployments, log rotation, and disk maintenance.

## Common Causes

- Filesystem is still mounted or has active file handles
- Another process has the file or device open
- Disk or partition is in use by a mounted filesystem
- Swap partition is active and cannot be modified
- Device mapper or LVM has the volume claimed
- NFS or network filesystem is still exported and in use
- Container (Docker) holding a volume lock

## How to Fix EBUSY

### 1. Find the Process Using the Resource

Identify which process is blocking the operation:

```bash
# Find processes using a specific file or directory
lsof /path/to/resource

# Find processes using a specific device
lsof /dev/sdb1

# Find processes using a mount point
lsof +D /mnt/data

# Alternative: use fuser to find processes using a file
sudo fuser -v /path/to/resource
```

### 2. Unmount the Filesystem

Ensure nothing is using the mount before unmounting:

```bash
# Check what is using the mount point
lsof +D /mnt/data

# Force unmount if nothing is using it
sudo umount /mnt/data

# Force unmount even if busy (use with caution)
sudo umount -l /mnt/data
```

The `-l` flag performs a lazy unmount, detaching the filesystem now and cleaning up references later.

### 3. Kill Blocking Processes

If a process is holding the resource open:

```bash
# Find the process
lsof /path/to/file

# Kill the process gracefully
kill <PID>

# Force kill if it won't terminate
kill -9 <PID>

# Or use fuser to kill all processes using a file
sudo fuser -k /path/to/file
```

### 4. Remove File Locks

Check for advisory locks on the file:

```bash
# List all locks on the system
sudo lslocks

# Check locks on a specific file
sudo flock -n /path/to/file echo "no lock" || echo "locked"

# Remove a lock by killing the holding process
sudo kill -9 $(sudo lsof -t /path/to/file)
```

### 5. Handle Device Mapper and LVM Busy State

LVM or device mapper may hold the device:

```bash
# Check device mapper status
sudo dmsetup status

# Check LVM volume group usage
sudo vgdisplay
sudo lvdisplay

# Deactivate an LV before removal
sudo lvchange -a n /dev/vgname/lvname

# Remove the device mapper entry
sudo dmsetup remove /dev/mapper/name
```

### 6. Handle Swap Partition Busy

If you need to modify or remove a swap partition:

```bash
# Check current swap usage
swapon --show

# Disable the swap partition
sudo swapoff /dev/sdb2

# Now you can modify or remove it
sudo fdisk /dev/sdb
```

### 7. Handle Docker Volume Locks

Docker containers can hold volume locks:

```bash
# Find containers using a volume
docker ps -a

# Stop all containers
docker stop $(docker ps -q)

# Prune unused volumes
docker volume prune

# Force remove a specific volume
docker volume rm -f volume_name
```

### 8. Handle NFS and Network Filesystem

NFS exports may keep filesystems busy:

```bash
# Check which NFS clients are using the export
sudo exportfs -v

# Show active NFS connections
sudo nfsstat -s

# Unexport and stop NFS
sudo exportfs -u /path/to/export
sudo systemctl stop nfs-server
```

### 9. Use fuser to Identify and Resolve

The `fuser` utility is purpose-built for this error:

```bash
# Show processes using a file (verbose)
sudo fuser -v /mnt/data

# Kill all processes using a mount point
sudo fuser -km /mnt/data

# Then unmount
sudo umount /mnt/data
```

### 10. Prevent Future EBUSY Errors

Plan operations to avoid resource contention:

```bash
# Use flock to serialize access to critical resources
flock /tmp/my.lock -c "my-command"

# Check before attempting unmount
lsof +D /mnt/data && echo "Resource in use" || umount /mnt/data
```

## Related Error Codes

- [EBADF (errno 9)](/os/linux/errno-9/) — Bad file descriptor
- [ENODEV (errno 19)](/os/linux/errno-19/) — No such device
- [ENOSYS (errno 38)](/os/linux/errno-38/) — Function not implemented
