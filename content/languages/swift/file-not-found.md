---
title: "[Solution] Swift Error — POSIX Error: No Such File or Directory"
description: "Fix Swift file not found errors. Learn why POSIX ENOENT occurs and how to handle missing files and directories gracefully."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["posix", "file", "not-found", "directory", "filesystem"]
weight: 5
---

# POSIX Error: No Such File or Directory

This error occurs when your code tries to access a file or directory that doesn't exist. The POSIX error code `ENOENT` (2) is returned by file system operations.

## Description

Every file path reference in Swift can fail if the target doesn't exist. This is one of the most common file system errors, occurring with incorrect paths, deleted files, or uninitialized directories. Unlike permission denied, this error specifically means the path itself has no matching file system entry.

Common patterns:

- **Incorrect path** — typo in file name or directory.
- **File deleted** — referencing a file that was removed.
- **Missing directory** — parent directory not created before file creation.
- **Bundle resource missing** — resource file not included in the app bundle.

## Common Causes

```swift
// Cause 1: Incorrect file path
let url = URL(fileURLWithPath: "/Documents/myfile.txt") // Wrong path
let data = try Data(contentsOf: url)
// ENOENT: No such file or directory

// Cause 2: Missing parent directory
let fileManager = FileManager.default
let dir = documents.appendingPathComponent("subdir/deep/file.txt")
try "data".write(to: dir)
// ENOENT: subdirectory doesn't exist

// Cause 3: Deleted file
let tempFile = fileManager.temporaryDirectory.appendingPathComponent("cache.dat")
let data = try Data(contentsOf: tempFile)
// Fails if file was cleaned up

// Cause 4: Missing bundle resource
if let url = Bundle.main.url(forResource: "config", withExtension: "json") {
    let data = try Data(contentsOf: url)
} else {
    print("config.json not found in bundle")
}
```

## How to Fix

### Fix 1: Verify file exists before accessing

```swift
let fileURL = documents.appendingPathComponent("data.txt")

if FileManager.default.fileExists(atPath: fileURL.path) {
    let data = try Data(contentsOf: fileURL)
} else {
    print("File does not exist")
}
```

### Fix 2: Create directories before writing files

```swift
let fileManager = FileManager.default
let dir = documents.appendingPathComponent("subdir")
let file = dir.appendingPathComponent("data.txt")

if !fileManager.fileExists(atPath: dir.path) {
    try fileManager.createDirectory(at: dir, withIntermediateDirectories: true)
}
try "data".write(to: file)
```

### Fix 3: Handle missing bundle resources

```swift
struct Config {
    let settings: [String: String]

    init?() {
        guard let url = Bundle.main.url(forResource: "config", withExtension: "json") else {
            print("config.json not found — using defaults")
            settings = ["theme": "light"]
            return
        }
        guard let data = try? Data(contentsOf: url),
              let decoded = try? JSONDecoder().decode([String: String].self, from: data) else {
            return nil
        }
        settings = decoded
    }
}
```

### Fix 4: Use temporary files with cleanup

```swift
func writeTemporarily(_ data: Data, named name: String) throws -> URL {
    let tempDir = FileManager.default.temporaryDirectory
    let fileURL = tempDir.appendingPathComponent(name)
    try data.write(to: fileURL)
    return fileURL
}

// File will be cleaned up by the system eventually
```

## Examples

```swift
// Example 1: Path typo
let path = "/var/mobile/Containers/Data/Application/.../Documents/myfile.txt"
// Path may be wrong after app update

// Example 2: Resource not added to target
if let url = Bundle.main.url(forResource: "data", withExtension: "csv") {
    let data = try Data(contentsOf: url)
} else {
    // ENOENT — file exists on disk but not in app bundle
    // Check Build Phases > Copy Bundle Resources
}
```

## Related Errors

- [File Permission Denied]({{< relref "/languages/swift/file-permission" >}}) — file exists but can't access.
- [Disk Full]({{< relref "/languages/swift/disk-full" >}}) — can't write due to no space.
- [Core Data Error]({{< relref "/languages/swift/coredata-error" >}}) — missing Core Data store file.
