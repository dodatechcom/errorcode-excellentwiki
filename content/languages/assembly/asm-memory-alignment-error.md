---
title: "[Solution] Assembly Memory Alignment Error -- Unaligned Access"
description: "Fix assembly memory alignment errors when accessing data at unaligned addresses."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Assembly Memory Alignment Error

This error occurs when memory is accessed at addresses that are not properly aligned for the data type.

## Common Causes

- Accessing 4-byte value at non-4-byte-aligned address
- SSE/AVX instructions requiring 16/32-byte alignment
- Structure packing causing misaligned fields
- Stack frame not properly aligned

## How to Fix

### Align data properly

```asm
; WRONG: unaligned data
section .data
    byte_val db 1
    dword_val dd 42  ; may not be 4-byte aligned

; CORRECT: align directives
section .data
    byte_val db 1
    align 4
    dword_val dd 42  ; guaranteed 4-byte aligned
```

### Use aligned instructions

```asm
; Use MOVUPS for unaligned SSE access
movups xmm0, [rdi]  ; works on unaligned address

; Use MOVAPS for aligned (faster)
movaps xmm0, [rdi]  ; requires 16-byte alignment
```

## Examples

```asm
section .data
    align 16
    vector dd 1.0, 2.0, 3.0, 4.0  ; 16-byte aligned for SSE

section .text
    movaps xmm0, [vector]  ; safe, aligned
```
