---
title: "[Solution] Assembly Cache Line Error -- False Sharing Issues"
description: "Fix assembly cache line errors when data causes false sharing between CPU cores."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["warning"]
---

# Assembly Cache Line Error

This error occurs when data accessed by different CPU cores shares the same cache line, causing performance degradation.

## Common Causes

- Frequently written variables adjacent in memory
- Per-CPU data not aligned to cache line boundaries
- Structure fields accessed by different threads in same cache line
- Missing padding between per-CPU data structures

## How to Fix

### Align to cache line boundary

```asm
; WRONG: per-CPU data not aligned
section .data
cpu_counter_0: dd 0
cpu_counter_1: dd 0  ; same cache line!

; CORRECT: align to 64-byte cache line
section .data
align 64
cpu_counter_0: dd 0
align 64
cpu_counter_1: dd 0
```

### Use padding

```asm
struc per_cpu_data
    .counter resd 1
    alignb 64  ; pad to cache line
endstruc
```

## Examples

```asm
; Per-CPU counter with proper alignment
section .data
align 64
global per_cpu_counter
per_cpu_counter: times 256 dq 0  ; 256 CPUs * 8 bytes, padded
```
