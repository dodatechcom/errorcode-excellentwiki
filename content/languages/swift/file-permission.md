---
title: "[Solution] Swift Error — POSIX Error: Permission Denied"
description: "Fix Swift POSIX error: Permission denied. Learn why file access fails with permission errors and how to handle file system permissions."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["posix", "permission", "file", "filesystem", "sandbox"]
weight: 5
---

# POSIX Error: Permission Denied

This error occurs when your app attempts to access a file or directory without the required permissions. The POSIX error code `EACCES` (13) is returned by file system operations.

## Description

Every file on Apple platforms has permissions that control read, write, and execute access. Apps run in a sandbox with limited access to the file system. Attempting to access files outside the sandbox, system-protected locations, or files owned by other processes triggers this error.

Common patterns:

- **Sandbox violation** — accessing files outside app sandbox.
- **System directories** — writing to `/System`, `/Library`, etc.
- **Protected files** — accessing files created with restricted permissions.
- **iCloud Drive** — sync-related permission issues.

## Common Causes

```swift
// Cause 1: Writing to system directory
let path = "/System/test.txt"
try "data".write(toFile: path, atomically: true, encoding: .utf8)
// POSIX error: Permission denied

// Cause 2: Reading restricted file
let url = URL(fileURLWithPath: "/etc/hosts")
let data = try Data(contentsOf: url)
// May fail with permission denied

// Cause 3: Creating file with wrong permissions
let fileManager = FileManager.default
let tempDir = fileManager.temporaryDirectory.appendingPathComponent("restricted")
try fileManager.createDirectory(at: tempDir, withIntermediateDirectories: true,
                                 attributes: [.protectionKey: FileProtectionType.complete])
// File may be inaccessible after device locks

// Cause 4: App sandbox restriction
let documents = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask).first!
let externalFile = documents.appendingPathComponent("../../other-app/data.txt")
try Data(contentsOf: externalFile) // Sandbox violation
```

## How to Fix

### Fix 1: Use appropriate app directories

```swift
let fileManager = FileManager.default

// Wrong
let path = "/Library/test.txt"

// Correct — use app-specific directories
let documents = fileManager.urls(for: .documentDirectory, in: .userDomainMask).first!
let caches = fileManager.urls(for: .cachesDirectory, in: .userDomainMask).first!
let temp = fileManager.temporaryDirectory
```

### Fix 2: Check file accessibility before operations

```swift
let fileURL = documents.appendingPathComponent("data.txt")

if FileManager.default.isReadableFile(atPath: fileURL.path) {
    let data = try Data(contentsOf: fileURL)
} else {
    print("File not readable — check permissions")
}
```

### Fix 3: Use proper file protection

```swift
let fileManager = FileManager.default
let fileURL = documents.appendingPathComponent("sensitive.dat")

// Create with appropriate protection
try "data".write(to: fileURL, options: .completeFileProtection)

// Check if file is accessible (may be locked when device is locked)
if FileManager.default.isReadableFile(atPath: fileURL.path) {
    // File is accessible
}
```

### Fix 4: Request appropriate entitlements

```swift
// For accessing Health data, Photos, etc., request proper entitlements
// For iCloud Drive, enable iCloud Documents capability
// For arbitrary file access (iOS 11+), use document picker
```

## Examples

```swift
// Example 1: Writing outside sandbox
let path = URL(fileURLWithPath: "/tmp/test.txt")
try "data".write(to: path)
// Permission denied — outside sandbox

// Example 2: File protection when locked
let fileURL = documents.appendingPathComponent("protected.dat")
try "secret".write(to: fileURL, options: .completeFileProtection)
// When device is locked, file is unreadable
// Attempting to read returns permission error
```

## Related Errors

- [File Not Found]({{< relref "/languages/swift/file-not-found" >}}) — file doesn't exist (different from permission denied).
- [Disk Full]({{< relref "/languages/swift/disk-full" >}}) — no space left on device.
- [Security Error]({{< relref "/languages/swift/security-error" >}}) — OS-level security error.
