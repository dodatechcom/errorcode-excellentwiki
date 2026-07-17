---
title: "[Solution] macOS NSFileReadNoSuchFile (NSCocoaErrorDomain Code 260) — File Not Found"
description: "Fix macOS NSFileReadNoSuchFile (NSCocoaErrorDomain Code 260). Resolve Foundation file not found errors in Core Services and Cocoa applications."
platforms: ["macos"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# macOS NSFileReadNoSuchFile (NSCocoaErrorDomain Code 260) — File Not Found

NSFileReadNoSuchFile (error code 260 in NSCocoaErrorDomain) indicates that the file specified for reading does not exist at the given path. This error is the Foundation equivalent of the POSIX `ENOENT` error and occurs when the path is incorrect, the file was deleted, or a symlink target is broken.

## Common Causes

- The file path is incorrect or contains a typo
- The file was deleted or moved before the read operation
- A symbolic link in the path points to a non-existent target
- The application is looking for a file in a sandboxed container that does not exist
- The file resides on a volume that is not currently mounted

## How to Fix NSFileReadNoSuchFile

### 1. Verify the File Path

Confirm the file exists at the exact path being used:

```bash
# Check if the file exists
ls -la /path/to/file

# Check parent directories
ls -la /path/to/parent/

# Check for hidden characters in filename
ls -la /path/to/ | cat -v
```

### 2. Check for Broken Symlinks

Identify and fix broken symbolic links:

```bash
# Find broken symlinks in a directory
find /path/to/directory -xtype l

# Check if a specific symlink is broken
ls -la /path/to/symlink
readlink -f /path/to/symlink
```

### 3. Confirm Volume Mount Status

If the file is on an external or network volume, verify it is mounted:

```bash
# List mounted volumes
ls /Volumes/

# Mount a volume if not already mounted
diskutil mount /dev/diskN
```

### 4. Resolve Sandbox Path Issues

For sandboxed applications, use the container-relative path:

```swift
let containerURL = FileManager.default.urls(for: .applicationSupportDirectory, in: .userDomainMask).first
let fileURL = containerURL?.appendingPathComponent("myfile.dat")
```

### 5. Use Bundle Resources Correctly

If reading from an application bundle, use `Bundle.main`:

```swift
if let fileURL = Bundle.main.url(forResource: "myfile", withExtension: "txt") {
    let data = try Data(contentsOf: fileURL)
}
```

## Examples

This error commonly occurs when:

- An application references a configuration file that was never created
- A file path includes a typo or incorrect directory name
- A symlink points to a file on an ejected external drive
- A sandboxed app tries to access a file outside its container

## Related Error Codes

- NSFileReadNoPermission (NSCocoaErrorDomain Code 257) — [No Permission](/os/macos/nserror-3/)
- NSFileReadUnknownError (NSCocoaErrorDomain Code 256) — [Read Unknown Error](/os/macos/nserror-1/)
- NSFileReadCorruptFile (NSCocoaErrorDomain Code 512) — [Corrupt File](/os/macos/nserror-5/)
- macOS error -43 (FNFErr) — [File Not Found (POSIX)](/os/macos/-43/)
