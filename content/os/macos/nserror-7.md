---
title: "[Solution] macOS NSFileWriteFileExists (NSCocoaErrorDomain Code 516) — File Already Exists"
description: "Fix macOS NSFileWriteFileExists (NSCocoaErrorDomain Code 516). Resolve Foundation file already exists errors in Core Services and Cocoa applications."
platforms: ["macos"]
severities: ["error"]
error_types: ["os-error"]
tags: ["nsfilewritefileexists", "nscocoaerrordomain", "code-516", "file-write", "file-already-exists", "cocoa", "foundation"]
weight: 5
---

# macOS NSFileWriteFileExists (NSCocoaErrorDomain Code 516) — File Already Exists

NSFileWriteFileExists (error code 516 in NSCocoaErrorDomain) indicates that the write operation failed because a file already exists at the specified path and the creation options do not permit overwriting. This error typically occurs when using `FileManager.createFile(atPath:contents:options:)` without specifying the `.forOverwriting` option.

## Common Causes

- The write operation was attempted without the `.forOverwriting` creation option
- A file or directory with the same name already exists at the target path
- The application uses atomic writing, which creates a temporary file that conflicts with an existing file
- A previous save operation left a residual file that was not cleaned up

## How to Fix NSFileWriteFileExists

### 1. Check for Existing Files

Determine if a file already exists at the target path:

```bash
# Check if a file exists
ls -la /path/to/file

# Check for both files and directories
ls -la /path/to/target/
```

### 2. Remove or Rename the Existing File

Clear the way for the new write operation:

```bash
# Remove the existing file
rm /path/to/file

# Or rename it as a backup
mv /path/to/file /path/to/file.bak
```

### 3. Use the Overwrite Option in Code

Specify the `.forOverwriting` option when creating files:

```swift
let fileManager = FileManager.default
fileManager.createFile(
    atPath: filePath,
    contents: fileData,
    attributes: [.posixPermissions: 0o644]
)
```

### 4. Use Atomic Writes with Unique Names

Generate unique file names to avoid conflicts:

```swift
let uniqueName = UUID().uuidString + ".dat"
let fileURL = directoryURL.appendingPathComponent(uniqueName)
try data.write(to: fileURL, options: .atomic)
```

### 5. Use Temporary Directories for Atomic Saves

Write to a temporary location first, then move the file:

```swift
let tempURL = FileManager.default.temporaryDirectory.appendingPathComponent(UUID().uuidString)
try data.write(to: tempURL, options: .atomic)
try FileManager.default.moveItem(at: tempURL, to: destinationURL)
```

## Examples

This error commonly occurs when:

- A "Save As" dialog tries to save a file with a name that already exists
- An application attempts to create a cache file that was not previously deleted
- A backup script tries to write a snapshot to a fixed filename
- An atomic write creates a temporary file that collides with an existing one

## Related Error Codes

- NSFileWriteNoPermission (NSCocoaErrorDomain Code 516) — [No Permission](/os/macos/nserror-4/)
- NSFileWriteUnknownError (NSCocoaErrorDomain Code 513) — [Unknown Write Error](/os/macos/nserror-2/)
- NSFileWriteOutOfSpace (NSCocoaErrorDomain Code 640) — [Out of Space](/os/macos/nserror-10/)
- NSFileWriteIncompatibleEncoding (NSCocoaErrorDomain Code 517) — [Incompatible Encoding](/os/macos/nserror-8/)
