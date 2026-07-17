---
title: "[Solution] macOS NSFileWriteNoPermission (NSCocoaErrorDomain Code 516) — No Permission to Write"
description: "Fix macOS NSFileWriteNoPermission (NSCocoaErrorDomain Code 516). Resolve Foundation file write permission errors in Core Services and Cocoa applications."
platforms: ["macos"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# macOS NSFileWriteNoPermission (NSCocoaErrorDomain Code 516) — No Permission to Write

NSFileWriteNoPermission (error code 516 in NSCocoaErrorDomain) indicates that the application does not have permission to write to the specified file or directory. This error is raised when the operating system denies write access due to Unix permissions, ACL restrictions, file ownership, or sandbox constraints.

## Common Causes

- The file or parent directory lacks write permission for the current user
- The file is owned by root or another user, and the process runs as a regular user
- Access Control Lists (ACLs) explicitly deny write access to the file
- The application sandbox does not include the target path in its writable scope
- The target volume is mounted read-only

## How to Fix NSFileWriteNoPermission

### 1. Inspect and Modify Permissions

Check and update Unix permissions on the target path:

```bash
# View permissions
ls -la /path/to/destination/

# Grant write permission to the owner
chmod u+w /path/to/destination/

# Grant full read-write access
chmod 644 /path/to/file
```

### 2. Change Ownership

Take ownership of the file or directory:

```bash
# Change ownership to current user
sudo chown $(whoami) /path/to/destination/

# Recursively change ownership
sudo chown -R $(whoami) /path/to/destination/
```

### 3. Inspect and Adjust ACLs

Review and modify Access Control Lists:

```bash
# View ACLs
ls -le /path/to/destination/

# Remove a restrictive ACL
chmod -a "group:everyone deny delete" /path/to/destination/
```

### 4. Grant Full Disk Access

For system-level locations, grant Full Disk Access in System Settings:

1. Open **System Settings** → **Privacy & Security** → **Full Disk Access**
2. Click the **+** button and add the application
3. Enable the toggle for the application

### 5. Verify Sandbox Entitlements

For sandboxed applications, include the appropriate write entitlement:

```xml
<key>com.apple.security.files.user-selected.read-write</key>
<true/>
```

### 6. Check Volume Mount Status

Ensure the volume is writable:

```bash
# Check mount options
mount | grep "/Volumes/YourVolume"

# Remount read-write if needed
sudo mount -u -w /Volumes/YourVolume
```

## Examples

This error commonly occurs when:

- Saving a document to a directory owned by root without proper privileges
- Writing to a read-only disk image or external drive
- A sandboxed app attempts to write outside its container
- Modifying a file protected by System Integrity Protection (SIP)

## Related Error Codes

- NSFileReadNoPermission (NSCocoaErrorDomain Code 257) — [Read No Permission](/os/macos/nserror-3/)
- NSFileWriteUnknownError (NSCocoaErrorDomain Code 513) — [Unknown Write Error](/os/macos/nserror-2/)
- NSFileWriteFileExists (NSCocoaErrorDomain Code 516) — [File Exists](/os/macos/nserror-7/)
- NSFileWriteOutOfSpace (NSCocoaErrorDomain Code 640) — [Out of Space](/os/macos/nserror-10/)
