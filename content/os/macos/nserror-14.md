---
title: "[Solution] macOS NSFileReadCorruptFile (NSCocoaErrorDomain Code 512) — Corrupt File Error"
description: "Fix macOS NSFileReadCorruptFile (NSCocoaErrorDomain Code 512). Resolve Foundation file read corrupt file errors in Core Services and Cocoa applications."
platforms: ["macos"]
severities: ["error"]
error_types: ["os-error"]
tags: ["nsfilereadcorruptfile", "nscocoaerrordomain", "code-512", "file-read", "corrupt", "cocoa", "foundation"]
weight: 5
---

# macOS NSFileReadCorruptFile (NSCocoaErrorDomain Code 512) — Corrupt File Error

NSFileReadCorruptFile (error code 512 in NSCocoaErrorDomain) indicates that the file being read is corrupted or does not contain valid data in the expected format. The file system or application has determined that the file's contents are not readable as a valid document or data structure.

## Common Causes

- The file was partially written due to an application crash or power loss during save
- The storage medium has bad sectors causing data corruption
- A download or transfer was interrupted, leaving an incomplete file
- The file was modified by an incompatible application or encoding conversion
- Disk-level corruption from a failing drive or improper ejection of removable media

## How to Fix NSFileReadCorruptFile

### 1. Verify File Integrity

Check whether the file is readable and inspect its contents:

```bash
# Check file size and type
file /path/to/file
ls -la /path/to/file

# Attempt to read the file
cat /path/to/file

# For binary files, check the header
xxd /path/to/file | head -5
```

### 2. Run Disk First Aid

If disk-level corruption is suspected, verify and repair the disk:

```bash
# Verify the disk
diskutil verifyVolume /

# Repair disk errors
diskutil repairVolume /
```

### 3. Restore from Backup

If the file is irrecoverably corrupted, restore from a backup:

```bash
# Time Machine restore (if available)
tmutil restore /path/to/backup/file /path/to/destination/
```

### 4. Use Data Recovery Tools

For partially recoverable files, use specialized recovery tools:

```bash
# TestDisk (install via brew)
brew install testdisk
testdisk /path/to/disk

# PhotoRec for specific file types
photorec /path/to/disk
```

### 5. Validate File Format in Code

Add validation before parsing file contents:

```swift
guard FileManager.default.fileExists(atPath: fileURL.path),
      let data = try? Data(contentsOf: fileURL),
      data.count > 0 else {
    print("File is missing or corrupt")
    return
}
```

## Examples

This error commonly occurs when:

- Opening a document saved by an application that crashed mid-write
- Attempting to read a file on a USB drive that was improperly ejected
- Opening a partially downloaded file
- Trying to parse a plist or JSON file that has been truncated

## Related Error Codes

- NSFileReadNoSuchFile (NSCocoaErrorDomain Code 260) — [File Not Found](/os/macos/nserror-6/)
- NSFileReadUnknownError (NSCocoaErrorDomain Code 256) — [Read Unknown Error](/os/macos/nserror-1/)
- NSFileReadUnsupportedEncoding (NSCocoaErrorDomain Code 261) — [Unsupported Encoding](/os/macos/nserror-13/)
- NSFileStreamErrorMinimum (NSCocoaErrorDomain Code 2048) — [Stream Error Minimum](/os/macos/nserror-15/)
