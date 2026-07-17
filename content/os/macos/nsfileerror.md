---
title: "[Solution] macOS NSFileError — File System Errors"
description: "Fix macOS NSFileError file system errors. Causes and solutions for Foundation file read/write failures and permission issues."
platforms: ["macos"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["nsfileerror", "file-system", "foundation", "permission", "io-error"]
weight: 5
---

# macOS NSFileError — File System Errors

NSFileError (domain: `NSCocoaErrorDomain`, codes 0–102) represents file system operation failures in the Foundation framework. These errors occur during file read, write, delete, copy, and move operations.

## What This Error Means

NSFileError codes cover file system operations:

- `NSFileReadNoSuchFile (260)` — File does not exist
- `NSFileReadCorruptFile (259)` — File is corrupted or unreadable
- `NSFileWriteNoPermission (516)` — Insufficient permissions to write
- `NSFileWriteFileExists (516)` — File already exists and cannot be overwritten
- `NSFileWriteOutOfSpace (640)` — Disk full
- `NSFileWriteUnknownError (513)` — Unknown write error

## Common Causes

- Insufficient file or directory permissions
- Disk is full or volume is read-only
- File is locked or in use by another process
- Sandbox restrictions preventing file access

## How to Fix

### Check and Fix Permissions

```bash
# Check file permissions
ls -la /path/to/file

# Fix permissions
chmod 644 /path/to/file
chown $(whoami) /path/to/file
```

### Verify Disk Space

```bash
# Check available disk space
df -h /

# Find large files
du -sh /path/to/folder/* | sort -rh | head -20
```

### Check for File Locks

```bash
# Check if file is locked
ls -lO /path/to/file

# Remove lock flag
chflags -nouchg /path/to/file
```

### Inspect Sandbox Entitlements

```xml
<key>com.apple.security.files.user-selected.read-write</key>
<true/>
```

## Related Errors

- [NSFileWriteUnknownError (NSCocoaErrorDomain Code 513)]({{< relref "/os/macos/nserror-2" >}}) — Unknown write error
- [NSFileWriteNoPermission (NSCocoaErrorDomain Code 516)]({{< relref "/os/macos/nserror-4" >}}) — No permission to write
- [NSFileReadNoSuchFile (NSCocoaErrorDomain Code 260)]({{< relref "/os/macos/nserror-1" >}}) — File not found
