---
title: "[Solution] Heap Corruption Runtime Error — Fix Heap Memory Corruption"
description: "Fix heap corruption runtime errors on Windows. Resolve invalid heap operations, use-after-free, double-free, and heap validation failures."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["heap-corruption", "use-after-free", "double-free", "heap", "memory", "debug"]
weight: 5
---

# Heap Corruption Runtime Error — Heap Memory Corruption

A heap corruption runtime error occurs when a program corrupts the heap data structures used by the memory allocator. The crash dialog shows:

> "Windows has triggered a breakpoint in [program.exe]. This may be due to a corruption of the heap."

Or:

> "HEAP_CORRUPTION_DETECTED at address 0x..."

## What This Error Means

The Windows heap manager maintains metadata for every heap allocation. When a program writes beyond the bounds of a heap buffer, frees memory twice, or uses memory after freeing it, it corrupts this metadata. The corruption may not be detected immediately — the crash often happens much later when the heap is next validated, making root cause analysis difficult.

## Common Causes

- Buffer overrun on a heap-allocated buffer (most common)
- Use-after-free (accessing memory after `free()` or `HeapFree`)
- Double-free (freeing the same allocation twice)
- Mismatched allocators (allocating with `new` and freeing with `free`)
- Thread safety issues (concurrent heap modifications without locks)
- Third-party DLL corrupting application heap

## How to Fix

### Enable Application Verifier

```cmd
# Enable heap checks for the application
appverif.exe /enable myapp.exe /rules Heaps
```

Application Verifier places guard pages around heap allocations and validates the heap on every allocation/deallocation.

### Enable Full Page Heap

```cmd
# Enable full page heap checking (catches overruns immediately)
gflags.exe /p /enable myapp.exe /full
```

### Use Debug CRT Heap

```c
#define _CRTDBG_MAP_ALLOC
#include <stdlib.h>
#include <crtdbg.h>

int main() {
    _CrtSetDbgFlag(_CRTDBG_ALLOC_MEM_DF | _CRTDBG_CHECK_ALWAYS_DF);
    // ... your code
    _CrtDumpMemoryLeaks();
}
```

### Run GFlags with Stack Traces

```cmd
# Enable stack trace logging for heap allocations
gflags.exe /p /enable myapp.exe /stacktrace /backtrace 16
```

This logs the call stack of every allocation, making it possible to identify the source of corruption.

### Use Address Sanitizer (Visual Studio 2019+)

```cmd
# Compile with ASan enabled
cl /fsanitize=address app.cpp
```

ASan detects overflows, use-after-free, and double-free immediately at the point of corruption.

### Check Event Viewer for Heap Error Details

```powershell
Get-WinEvent -LogName Application | Where-Object { $_.Message -like "*heap*" } | Select-Object -First 5 TimeCreated, Message | Format-List
```

## Related Errors

- [Access Violation 0xC0000005]({{< relref "/os/windows/runtime-error-access-violation" >}}) — General memory access violations
- [ntdll.dll Error]({{< relref "/os/windows/ntdll-dll" >}}) — Heap corruption often manifests as ntdll.dll crashes
- [Buffer Overrun]({{< relref "/os/windows/runtime-error-buffer-overrun" >}}) — Stack buffer overflow (different from heap overrun)
