---
title: "[Solution] macOS OSStatus -3 (dsBadRoute) — Bad Route Error"
description: "Fix macOS OSStatus -3 (dsBadRoute). Resolve bad route errors in Core Services, Carbon, and legacy Mac framework applications."
platforms: ["macos"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# macOS OSStatus -3 (dsBadRoute) — Bad Route Error

OSStatus -3 (dsBadRoute) indicates that the system encountered an invalid or malformed routing entry when attempting to locate or access a resource. This error is returned by legacy Core Services and Carbon resource manager APIs when the system cannot resolve a path, alias, or resource reference to a valid destination.

## Common Causes

- A file alias or resource fork contains a corrupted or invalid routing path
- The target volume or disk referenced by the route is not mounted
- A network resource path points to a non-existent server or share
- The resource fork of a file has been corrupted or stripped
- An application tries to access a resource using an outdated or invalid path

## How to Fix dsBadRoute

### 1. Verify the Resource Path

Ensure the file or resource path is valid and accessible:

```bash
# Check if the file exists
ls -la /path/to/file

# Resolve aliases
open /path/to/file

# Check resource forks
ls -l@ /path/to/file
```

### 2. Check Volume Mount Status

Ensure all volumes referenced in the route are mounted:

```bash
# List mounted volumes
ls /Volumes/

# Mount a disk if needed
diskutil mount /dev/diskN
```

### 3. Validate Network Paths

If the route references a network resource, verify connectivity:

```bash
# Check network mount
mount | grep smbfs
mount | grep nfs

# Ping the server
ping -c 3 server.example.com

# List SMB shares
smbclient -L //server.example.com
```

### 4. Repair File Aliases

Recreate broken aliases that reference moved or deleted files:

```bash
# Find and list broken aliases
find /path/to/directory -type l -exec test ! -e {} \; -print

# Remove broken aliases
find /path/to/directory -type l -exec test ! -e {} \; -delete
```

### 5. Use Absolute Paths in Code

Avoid relying on relative paths or aliases when possible:

```swift
// Use absolute URLs for resource access
let baseURL = URL(fileURLWithPath: "/Applications/MyApp.app/Contents/Resources/")
let resourceURL = baseURL.appendingPathComponent("data.plist")
```

## Examples

This error commonly occurs when:

- A Carbon application tries to open a file using a stale alias
- A resource fork path references a volume that was ejected
- An application bundle contains references to moved framework paths
- A network share used for resources becomes unavailable

## Related Error Codes

- dsBusError (OSStatus -2) — [Bus Error](/os/macos/osstatus-5/)
- dsMemoryError (OSStatus -110) — [Memory Error](/os/macos/osstatus-7/)
- osLogicError (OSStatus -66) — [Logic Error](/os/macos/osstatus-8/)
- errNoSuchName (OSStatus -41) — [No Such Name](/os/macos/osstatus-12/)
