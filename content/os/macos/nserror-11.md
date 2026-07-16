---
title: "[Solution] macOS NSFileWriteUnknownError (NSCocoaErrorDomain Code 513) — Unknown Write Error"
description: "Fix macOS NSFileWriteUnknownError (NSCocoaErrorDomain Code 513). Resolve Foundation file write unknown errors in Core Services and Cocoa applications."
platforms: ["macos"]
severities: ["error"]
error_types: ["os-error"]
tags: ["nsfilewriteunknownerror", "nscocoaerrordomain", "code-513", "file-write", "cocoa", "foundation"]
weight: 5
---

# macOS NSFileWriteUnknownError (NSCocoaErrorDomain Code 513) — Unknown Write Error

NSFileWriteUnknownError (error code 513 in NSCocoaErrorDomain) indicates that an unspecified error occurred during a file write operation. This generic Foundation error does not provide a specific reason for the failure, requiring investigation into disk space, permissions, file system integrity, and sandbox constraints.

## Common Causes

- The destination disk or volume is full or has insufficient space
- The file or directory is read-only or locked by another process
- The application lacks write permissions for the target directory
- A sandbox restriction prevents the application from writing to the specified location
- The file system is experiencing I/O errors or corruption

## How to Fix NSFileWriteUnknownError

### 1. Check Available Disk Space

Verify sufficient space on the target volume:

```bash
# Check available disk space
df -h /path/to/destination

# Identify large files consuming space
du -sh /path/to/folder/* | sort -rh | head -20
```

### 2. Verify Write Permissions

Ensure the process can write to the target directory:

```bash
# Check directory permissions
ls -la /path/to/destination/

# Test write access
touch /path/to/destination/testfile && rm /path/to/destination/testfile

# Fix permissions if needed
chmod u+w /path/to/destination/
```

### 3. Check Volume Mount Status

If writing to an external or network volume, verify it is mounted and writable:

```bash
# List mounted volumes
mount | grep /Volumes

# Check if volume is read-only
mount | grep "/Volumes/YourVolume"
```

### 4. Inspect Sandbox Entitlements

For sandboxed applications, ensure the entitlements file includes the required file-access scope:

```xml
<key>com.apple.security.files.user-selected.read-write</key>
<true/>
```

### 5. Log Detailed Error Information

Use code to capture diagnostic details:

```swift
do {
    try data.write(to: fileURL)
} catch let error as NSError {
    print("Write failed — domain: \(error.domain), code: \(error.code)")
    print("userInfo: \(error.userInfo)")
}
```

## Examples

This error commonly occurs when:

- Saving a document to a read-only disk image
- Writing to a network share that has become disconnected
- An application tries to save outside its sandbox container
- The target directory was deleted after the file handle was obtained

## Related Error Codes

- NSFileWriteNoPermission (NSCocoaErrorDomain Code 516) — [No Permission](/os/macos/nserror-4/)
- NSFileWriteFileExists (NSCocoaErrorDomain Code 516) — [File Exists](/os/macos/nserror-7/)
- NSFileWriteOutOfSpace (NSCocoaErrorDomain Code 640) — [Out of Space](/os/macos/nserror-10/)
- NSFileReadUnknownError (NSCocoaErrorDomain Code 256) — [Read Unknown Error](/os/macos/nserror-1/)
