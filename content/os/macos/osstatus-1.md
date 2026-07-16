---
title: "[Solution] macOS OSStatus -108 (memFullErr) — Memory Full Error"
description: "Fix macOS OSStatus -108 (memFullErr). Resolve memory full errors in Core Services, Carbon, and legacy Mac framework applications."
platforms: ["macos"]
severities: ["error"]
error_types: ["os-error"]
tags: ["memfullerr", "osstatus-108", "memory", "core-services", "carbon", "out-of-memory"]
weight: 5
---

# macOS OSStatus -108 (memFullErr) — Memory Full Error

OSStatus -108 (memFullErr) indicates that the system or application has exhausted available memory. This error is returned by legacy Core Services and Carbon APIs when a memory allocation fails. On modern macOS, this error is rare because the virtual memory system handles most memory pressure, but it can still occur in 32-bit processes, embedded systems, or when the system is under extreme memory pressure.

## Common Causes

- The application or system has exhausted available physical and virtual memory
- A 32-bit process has hit its 4 GB address space limit
- A memory leak has accumulated over time, consuming all available memory
- The system is running too many memory-intensive applications simultaneously
- A large data structure or buffer allocation request exceeds available contiguous memory

## How to Fix memFullErr

### 1. Check System Memory Usage

Identify memory pressure on the system:

```bash
# Check memory usage
top -l 1 -s 0 | head -12

# Check for memory-heavy processes
ps aux --sort=-%mem | head -20

# Check swap usage
sysctl vm.swapusage
```

### 2. Reduce Application Memory Usage

Optimize memory consumption in your application:

```bash
# Check your application's memory footprint
ps -o pid,rss,command -p $(pgrep YourApp)

# Monitor memory in Instruments
# Open Instruments.app → Allocations template
```

### 3. Increase Available Memory

Close unnecessary applications to free up memory:

```bash
# List running applications
ps aux | grep -i "Applications/"

# Force-quit a specific process
kill -9 <PID>
```

### 4. Use Memory-Mapped Files

For large data sets, use memory-mapped files instead of loading everything into memory:

```swift
// Memory-mapped file read
let data = try Data(contentsOf: fileURL, options: .mappedIfSafe)
```

### 5. Migrate to 64-bit

If the application is still 32-bit, rebuild it as 64-bit to access a larger address space:

```bash
# Check if the binary is 32-bit or 64-bit
file /path/to/binary

# Check architecture
lipo -info /path/to/binary
```

## Examples

This error commonly occurs when:

- A legacy Carbon application tries to allocate a large block of memory
- A 32-bit application reaches its address space limit
- The system runs out of swap space and cannot page out additional memory
- A script or tool processes an extremely large file entirely in memory

## Related Error Codes

- memBadSize (OSStatus -109) — [Bad Memory Size](/os/macos/osstatus-2/)
- memErr (OSStatus -10) — [Memory Error](/os/macos/osstatus-3/)
- dsHeapErr (OSStatus -109) — [Heap Error](/os/macos/osstatus-4/)
- paramErr (OSStatus -50) — [Parameter Error](/os/macos/osstatus-9/)
