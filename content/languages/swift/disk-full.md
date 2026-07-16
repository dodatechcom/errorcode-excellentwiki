---
title: "[Solution] Swift Error — POSIX Error: No Space Left on Device"
description: "Fix Swift disk full errors. Learn why ENOSPC occurs and how to handle insufficient disk space in Swift applications."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["posix", "disk", "space", "enosp", "storage"]
weight: 5
---

# POSIX Error: No Space Left on Device

This error occurs when a file system operation fails because the device has no free disk space. The POSIX error code `ENOSPC` (28) is returned.

## Description

Every write operation — file creation, database saves, cache storage — requires free disk space. When the device is full, all write operations fail with `ENOSPC`. This is common with large downloads, cache accumulation, and database growth.

Common patterns:

- **Cache accumulation** — app cache growing without cleanup.
- **Large downloads** — downloading files when storage is low.
- **Database growth** — Core Data or Realm database expanding.
- **Logging** — excessive log file creation filling storage.

## Common Causes

```swift
// Cause 1: Writing large file without checking space
let largeData = Data(repeating: 0, count: 1_000_000_000) // 1GB
try largeData.write(to: fileURL) // ENOSPC if device is full

// Cause 2: Unbounded cache growth
func cache(_ data: Data, forKey key: String) {
    let cacheDir = FileManager.default.urls(for: .cachesDirectory, in: .userDomainMask).first!
    let fileURL = cacheDir.appendingPathComponent(key)
    try data.write(to: fileURL) // May fill disk over time
}

// Cause 3: Database without size limits
// Core Data or Realm databases growing without cleanup

// Cause 4: Temporary file accumulation
for i in 0..<10000 {
    let tempURL = FileManager.default.temporaryDirectory.appendingPathComponent("file\(i)")
    try "data".write(to: tempURL) // Accumulates until system cleans up
}
```

## How to Fix

### Fix 1: Check available space before writing

```swift
func availableDiskSpace() -> Int64? {
    let fileURL = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask).first!
    do {
        let values = try fileURL.resourceValues(forKeys: [.volumeAvailableCapacityForImportantUsageKey])
        return values.volumeAvailableCapacityForImportantUsage
    } catch {
        return nil
    }
}

func writeIfSpaceAvailable(_ data: Data, to url: URL) throws {
    guard let available = availableDiskSpace(), available > Int64(data.count) else {
        throw NSError(domain: NSPOSIXErrorDomain, code: Int(ENOSPC))
    }
    try data.write(to: url)
}
```

### Fix 2: Implement cache cleanup

```swift
func cleanOldCache(olderThan days: Int = 7) {
    let cacheDir = FileManager.default.urls(for: .cachesDirectory, in: .userDomainMask).first!
    guard let files = try? FileManager.default.contentsOfDirectory(at: cacheDir,
                                                                    includingPropertiesForKeys: [.creationDateKey]) else { return }
    let cutoff = Date().addingTimeInterval(-Double(days * 86400))
    for file in files {
        if let date = try? file.resourceValues(forKeys: [.creationDateKey]).creationDate,
           date < cutoff {
            try? FileManager.default.removeItem(at: file)
        }
    }
}
```

### Fix 3: Monitor disk space

```swift
class DiskSpaceMonitor {
    static let lowSpaceNotification = Notification.Name("DiskSpaceLow")

    static func startMonitoring() {
        Timer.scheduledTimer(withTimeInterval: 60, repeats: true) { _ in
            if let available = availableDiskSpace(), available < 100_000_000 {
                NotificationCenter.default.post(name: lowSpaceNotification, object: nil)
            }
        }
    }
}
```

### Fix 4: Use streaming for large data

```swift
// Wrong — loads everything into memory
let data = try Data(contentsOf: largeFileURL)
try data.write(to: destination)

// Correct — stream in chunks
let inputStream = InputStream(url: largeFileURL)!
let outputStream = OutputStream(url: destination, append: false)
var buffer = [UInt8](repeating: 0, count: 1024 * 1024)
inputStream.open()
outputStream.open()
while inputStream.hasBytesAvailable {
    let bytesRead = inputStream.read(&buffer, maxLength: buffer.count)
    if bytesRead > 0 {
        outputStream.write(buffer, maxLength: bytesRead)
    }
}
inputStream.close()
outputStream.close()
```

## Examples

```swift
// Example 1: Download without space check
let task = URLSession.shared.downloadTask(with: largeFileURL) { tempURL, _, _ in
    let destination = documents.appendingPathComponent("largefile.zip")
    try FileManager.default.moveItem(at: tempURL!, to: destination)
    // ENOSPC if device full
}

// Example 2: Database without cleanup
func saveToDatabase(_ records: [Record]) {
    for record in records {
        context.insert(record) // Database grows unbounded
    }
    try? context.save() // May fail with ENOSPC
}
```

## Related Errors

- [File Permission Denied]({{< relref "/languages/swift/file-permission" >}}) — permission issues.
- [File Not Found]({{< relref "/languages/swift/file-not-found" >}}) — missing file errors.
- [Core Data Error]({{< relref "/languages/swift/coredata-error" >}}) — database storage issues.
