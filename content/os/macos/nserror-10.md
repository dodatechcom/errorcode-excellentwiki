---
title: "[Solution] macOS NSFileWriteOutOfSpace (NSCocoaErrorDomain Code 640) — Out of Disk Space"
description: "Fix macOS NSFileWriteOutOfSpace (NSCocoaErrorDomain Code 640). Resolve Foundation out of disk space errors in Core Services and Cocoa applications."
platforms: ["macos"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# macOS NSFileWriteOutOfSpace (NSCocoaErrorDomain Code 640) — Out of Disk Space

NSFileWriteOutOfSpace (error code 640 in NSCocoaErrorDomain) indicates that the write operation failed because the disk or volume does not have enough free space to accommodate the data. This error is the Foundation equivalent of the POSIX `ENOSPC` error and means the storage device is full.

## Common Causes

- The target disk or volume has insufficient free space for the file being written
- Disk quotas limit the amount of space available to the current user
- The volume is nearly full due to accumulated caches, logs, or temporary files
- A disk image or partition has reached its maximum capacity
- Time Machine snapshots or local snapshots are consuming available space

## How to Fix NSFileWriteOutOfSpace

### 1. Check Available Disk Space

Determine how much free space remains on the target volume:

```bash
# Check disk space for the root volume
df -h /

# Check disk space for a specific path
df -h /path/to/destination

# Show disk usage by directory
du -sh /path/to/directory/* | sort -rh | head -10
```

### 2. Free Up Disk Space

Remove unnecessary files to reclaim space:

```bash
# Empty the Trash
rm -rf ~/.Trash/*

# Clear system and user caches
rm -rf ~/Library/Caches/*
sudo rm -rf /Library/Caches/*

# Remove old log files
sudo rm -rf /var/log/*.gz
sudo rm -rf /private/var/log/asl/*.asl

# Clear Time Machine local snapshots
tmutil deletelocalsnapshots /
```

### 3. Use Optimized Storage

Enable macOS storage optimization features:

1. Open **Apple Menu** → **About This Mac** → **Storage**
2. Click **Manage** and enable recommendations
3. Enable "Store in iCloud" and "Optimize Storage"

### 4. Use Sparse Disk Images

For applications writing to custom volumes, use dynamically-sized sparse disk images:

```bash
# Create a sparse disk image that grows as needed
hdiutil create -type sparse -size 10G -fs HFS+ /path/to/volume
```

### 5. Write to a Different Volume

Redirect writes to a volume with more space:

```swift
let alternativeURL = URL(fileURLWithPath: "/Volumes/LargeDrive/backup/")
try data.write(to: alternativeURL.appendingPathComponent("output.dat"))
```

## Examples

This error commonly occurs when:

- Saving a large video file to a nearly full startup disk
- Writing a database export to a disk image that has reached capacity
- A build process generates more output than available disk space allows
- A backup operation fails because the destination volume is full

## Related Error Codes

- NSFileWriteNoPermission (NSCocoaErrorDomain Code 516) — [No Permission](/os/macos/nserror-4/)
- NSFileWriteUnknownError (NSCocoaErrorDomain Code 513) — [Unknown Write Error](/os/macos/nserror-2/)
- NSFileWriteFileExists (NSCocoaErrorDomain Code 516) — [File Exists](/os/macos/nserror-7/)
- NSFileWriteIncompatibleEncoding (NSCocoaErrorDomain Code 517) — [Incompatible Encoding](/os/macos/nserror-8/)
