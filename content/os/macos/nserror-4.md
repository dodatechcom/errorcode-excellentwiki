---
title: "[Solution] macOS NSFileWriteNoPermission (NSCocoaErrorDomain Code 516) — No Permission to Write"
description: "Fix macOS NSFileWriteNoPermission (NSCocoaErrorDomain Code 516). Resolve Foundation file write permission denied errors in Core Services and Cocoa applications."
platforms: ["macos"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# macOS NSFileWriteNoPermission (NSCocoaErrorDomain Code 516) — No Permission to Write

NSFileWriteNoPermission (error code 516 in NSCocoaErrorDomain) indicates that the application does not have permission to write to the specified file or directory. This error occurs when the operating system denies write access due to Unix file permissions, ACL restrictions, file ownership, or sandbox constraints.

## Common Causes

- The file or parent directory does not have write permission for the current user
- The file is owned by root or another user, and the process runs as a regular user
- Access Control Lists (ACLs) explicitly deny write access
- The application sandbox does not include the target path in its write scope
- The volume is mounted read-only

## How to Fix NSFileWriteNoPermission

### 1. Check and Modify File Permissions

Inspect and adjust Unix permissions on the target path:

```bash
# View file permissions and ownership
ls -la /path/to/destination/

# Grant write permission to the current user
chmod u+w /path/to/destination/

# Grant full read-write to owner
chmod u+rw /path/to/destination/
```

### 2. Change File or Directory Ownership

Take ownership of the file or directory:

```bash
# Change ownership to current user
sudo chown $(whoami) /path/to/destination/

# Recursively change ownership of a directory
sudo chown -R $(whoami) /path/to/destination/
```

### 3. Inspect and Modify ACLs

Check and adjust Access Control Lists:

```bash
# View ACLs
ls -le /path/to/destination/

# Remove a restrictive ACL
chmod -a "group:everyone deny delete" /path/to/destination/
```

### 4. Grant Full Disk Access

For applications that need to write to system-level locations:

1. Open **System Settings** → **Privacy & Security** → **Full Disk Access**
2. Click the **+** button and add your application
3. Enable the toggle for the application

### 5. Verify Sandbox Entitlements

For sandboxed applications, ensure the entitlements file includes the appropriate scope:

```xml
<key>com.apple.security.files.user-selected.read-write</key>
<true/>
```

### 6. Check Volume Mount Options

Ensure the target volume is not mounted read-only:

```bash
# Check mount options
mount | grep "/Volumes/YourVolume"

# Remount as read-write if necessary
sudo mount -u -w /Volumes/YourVolume
```

## Examples

This error commonly occurs when:

- Saving a file to a directory owned by root without proper privileges
- Writing to a read-only disk image or external drive
- A sandboxed application attempts to write outside its container
- Modifying a file protected by System Integrity Protection (SIP)

## Related Error Codes

- NSFileReadNoPermission (NSCocoaErrorDomain Code 257) — [Read No Permission](/os/macos/nserror-3/)
- NSFileWriteUnknownError (NSCocoaErrorDomain Code 513) — [Write Unknown Error](/os/macos/nserror-2/)
- NSFileWriteFileExists (NSCocoaErrorDomain Code 516) — [File Exists](/os/macos/nserror-7/)
- NSFileWriteOutOfSpace (NSCocoaErrorDomain Code 640) — [Out of Space](/os/macos/nserror-10/)
