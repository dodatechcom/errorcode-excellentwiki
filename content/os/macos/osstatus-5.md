---
title: "[Solution] macOS OSStatus -2 (dsBusError) — Bus Error"
description: "Fix macOS OSStatus -2 (dsBusError). Resolve bus errors in Core Services, Carbon, and legacy Mac framework applications."
platforms: ["macos"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# macOS OSStatus -2 (dsBusError) — Bus Error

OSStatus -2 (dsBusError) indicates that the processor attempted to access memory in an invalid or unmapped way, resulting in a bus error. This error is triggered at the hardware or virtual memory level when a program tries to read or write to an address that is not properly aligned, not mapped, or otherwise inaccessible. On macOS, this is equivalent to the `SIGBUS` signal.

## Common Causes

- A pointer references memory that has been unmapped or paged out
- An attempt is made to access memory at an address that is not properly aligned
- A memory-mapped file was truncated or changed while being accessed
- A dangling pointer references memory that was freed or deallocated
- The process tried to access memory beyond the end of an allocated block

## How to Fix dsBusError

### 1. Identify the Faulting Address

Determine which memory address caused the bus error:

```bash
# Run the application in a debugger to capture the crash
lldb ./YourApp

# Or use dtrace to trace bus errors
sudo dtrace -n 'proc:::signal-send /args[2] == SIGBUS/ { printf("%s -> %s\n", execname, args[1]->pr_fname); }'
```

### 2. Check for Memory Alignment Issues

Ensure data structures are properly aligned in memory:

```c
// Properly aligned structure
struct __attribute__((aligned(8))) DataBlock {
    uint64_t value;
    char buffer[256];
};

// Avoid casting misaligned pointers
void* ptr = malloc(sizeof(DataBlock));
DataBlock* block = (DataBlock*)ptr; // Ensure ptr is aligned
```

### 3. Validate Memory-Mapped File Access

If using memory-mapped files, ensure the mapping is consistent:

```swift
// Memory-map a file safely
let fileHandle = try FileHandle(forReadingFrom: fileURL)
let data = try fileHandle.readDataToEndOfFile()
fileHandle.closeFile()
```

### 4. Enable Guard Malloc for Detection

Use Guard Malloc to detect invalid memory accesses:

```bash
# Enable Guard Malloc
DYLD_INSERT_LIBRARIES=/usr/lib/libgmalloc.dylib ./YourApp

# Increase guard pages for more thorough checking
export MALLOC_GUARDED_PAGES=1
```

### 5. Check for Use-After-Free

Use Address Sanitizer to detect use-after-free and other memory errors:

```bash
# Build with Address Sanitizer
clang -fsanitize=address -g YourFile.c -o YourApp
./YourApp
```

## Examples

This error commonly occurs when:

- A program accesses a memory-mapped file after it has been truncated
- A pointer is cast to a misaligned address and then dereferenced
- A buffer overflow corrupts adjacent memory, leading to an invalid access
- A freed memory block is accessed after deallocation

## Related Error Codes

- dsHeapErr (OSStatus -109) — [Heap Error](/os/macos/osstatus-4/)
- dsMemoryError (OSStatus -110) — [Memory Error](/os/macos/osstatus-7/)
- dsBadRoute (OSStatus -3) — [Bad Route](/os/macos/osstatus-6/)
- memErr (OSStatus -10) — [Memory Error](/os/macos/osstatus-3/)
