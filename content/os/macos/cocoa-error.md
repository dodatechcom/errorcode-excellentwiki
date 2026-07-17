---
title: "[Solution] macOS Cocoa Error Codes (1–713)"
description: "Fix macOS Cocoa error codes in the 1-713 range. Causes and solutions for NSCocoaErrorDomain file and data operation failures."
platforms: ["macos"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["cocoa", "nscocoaerrordomain", "error-codes", "foundation", "file-operation"]
weight: 5
---

# macOS Cocoa Error Codes (1–713)

Cocoa error codes in the `NSCocoaErrorDomain` cover file operations, data parsing, migration, and general Foundation framework failures. These codes range from 1 to 713 and are the most common errors in macOS applications.

## What This Error Means

Key error ranges in NSCocoaErrorDomain:

- **0–102**: File system operations (read, write, delete, copy)
- **256–512**: File read errors (corrupt file, format issues)
- **512–768**: File write errors (permissions, disk full, unknown)
- **640–896**: File coordination and protection errors
- **1024–1280**: Migration and validation errors

## Common Causes

- Insufficient file system permissions for the operation
- Disk is full or the target volume is read-only
- File format is incompatible with the expected type
- Sandbox restrictions blocking file access

## How to Fix

### Check Error Code Specifics

```swift
do {
    try FileManager.default.contentsOfDirectory(at: url, includingPropertiesForKeys: nil)
} catch let error as NSError {
    print("Error domain: \(error.domain)")
    print("Error code: \(error.code)")
    print("UserInfo: \(error.userInfo)")
}
```

### Handle File Permission Errors

```bash
# Check and fix file permissions
ls -la /path/to/problem/file
chmod 644 /path/to/problem/file
```

### Verify Disk Space

```bash
df -h /
```

### Reset File Coordination

```bash
# Force kill file coordination daemon
sudo killall filecoordinationd
```

### Implement Error Recovery in Code

```swift
func performFileOperation() {
    do {
        try data.write(to: fileURL, options: .atomic)
    } catch CocoaError.fileWriteOutOfSpace {
        // Handle disk full
    } catch CocoaError.fileWriteNoPermission {
        // Handle permission denied
    } catch {
        // Handle other errors
    }
}
```

## Related Errors

- [NSFileError]({{< relref "/os/macos/nsfileerror" >}}) — Detailed file system error codes
- [Core Data Errors]({{< relref "/os/macos/core-data" >}}) — Core Data persistence layer errors
- [Launch Services Errors]({{< relref "/os/macos/launch-services-error" >}}) — Application launch failures
