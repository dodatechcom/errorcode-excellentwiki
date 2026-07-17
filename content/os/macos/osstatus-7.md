---
title: "[Solution] macOS OSStatus -110 (dsMemoryError) — Memory Error"
description: "Fix macOS OSStatus -110 (dsMemoryError). Resolve memory errors in Core Services, Carbon, and legacy Mac framework applications."
platforms: ["macos"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# macOS OSStatus -110 (dsMemoryError) — Memory Error

OSStatus -110 (dsMemoryError) is a low-level memory error returned by the Device Manager and legacy Core Services APIs. It indicates that a memory-related operation at the device or hardware driver level has failed, typically due to corrupted memory blocks, invalid memory addresses, or inaccessible hardware buffers.

## Common Causes

- A device driver or hardware abstraction layer accessed invalid memory
- A DMA (Direct Memory Access) buffer has been corrupted or deallocated
- The system's low-memory heap (used by Device Manager) is corrupted
- A hardware device reported a memory access error during I/O operations
- A legacy driver references memory that has been remapped or freed

## How to Fix dsMemoryError

### 1. Check System Logs

Review system logs for memory-related errors:

```bash
# Check system log for memory errors
log show --predicate 'eventMessage contains "memory"' --last 1h

# Check for kernel panics or memory issues
log show --predicate 'subsystem == "com.apple.memory"' --last 24h
```

### 2. Run Memory Diagnostics

Test system memory for hardware errors:

```bash
# Run Apple Diagnostics (restart required)
# Hold D during startup

# Check memory status
top -l 1 -s 0 | head -12

# Check for ECC errors (if supported)
system_profiler SPMemoryDataType
```

### 3. Reset the SMC

If the error is hardware-related, reset the System Management Controller:

```bash
# For Macs with Apple silicon: restart the Mac
# For Intel Macs with T2 chip:
# Shut down, hold Control+Option+Shift for 7 seconds, then press power for 7 more

# For older Intel Macs:
# Shut down, hold left Shift+Control+Option for 10 seconds, then press power
```

### 4. Use Memory Debugging Tools

Identify memory corruption in application code:

```bash
# Enable Guard Malloc
DYLD_INSERT_LIBRARIES=/usr/lib/libgmalloc.dylib ./YourApp

# Use Instruments Allocations
open -a Instruments YourApp
```

### 5. Update or Reinstall Drivers

If a third-party driver is causing the error, update or reinstall it:

```bash
# Check installed kernel extensions
kextstat | grep -v com.apple

# Remove problematic kext
sudo rm -rf /Library/Extensions/ProblematicDriver.kext
sudo touch /System/Library/Extensions
```

## Examples

This error commonly occurs when:

- A legacy Device Manager driver accesses a deallocated DMA buffer
- A USB or FireWire device reports a memory access error
- A kernel extension references invalid memory after a system sleep/wake cycle
- The low-memory heap used by the Device Manager becomes corrupted

## Related Error Codes

- dsHeapErr (OSStatus -109) — [Heap Error](/os/macos/osstatus-4/)
- memErr (OSStatus -10) — [Memory Error](/os/macos/osstatus-3/)
- memFullErr (OSStatus -108) — [Memory Full](/os/macos/osstatus-1/)
- dsBusError (OSStatus -2) — [Bus Error](/os/macos/osstatus-5/)
