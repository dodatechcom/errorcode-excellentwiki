---
title: "Alignment error in Assembly"
description: "Alignment errors in Assembly occur when accessing memory at addresses that are not properly aligned for the data type."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["alignment", "memory", "sse", "avx", "bus-error"]
weight: 5
---

## What This Error Means

Many CPU instructions require memory operands to be aligned to specific boundaries. SSE/AVX instructions require 16/32-byte alignment. Unaligned access can cause performance penalties or hardware exceptions.

## Common Causes

- SSE/AVX instructions on unaligned addresses
- Stack not aligned to 16-byte boundary before CALL
- Struct members at unaligned offsets
- Casting pointer to different alignment

## How to Fix

```asm
; WRONG: Unaligned SSE access
section .data
    buffer db 0, 0, 0, 0, 1.0, 0.0, 0.0, 0.0  ; Not 16-byte aligned

section .text
    movaps xmm0, [buffer]   ; Error: requires 16-byte alignment

; CORRECT: Use aligned data or movups
section .data
    align 16
    buffer dd 1.0, 0.0, 0.0, 0.0

section .text
    movaps xmm0, [buffer]   ; Works with aligned data
    ; Or use movups for unaligned access
    movups xmm0, [buffer]   ; Slower but works
```

```asm
; WRONG: Stack not aligned before call
push rax
push rbx
call my_function   ; RSP not 16-byte aligned

; CORRECT: Align stack before call
push rax
push rbx
and rsp, -16      ; Align to 16 bytes
call my_function
```

## Examples

```asm
section .data
    unaligned db 7 dup(0), 0
    ; offset 7 is not 16-byte aligned

section .text
    movdqu xmm0, [unaligned]  ; Use unaligned variant
```

## Related Errors

- [Page Fault](/languages/assembly/asm-page-fault) - memory page errors
- [Segmentation Fault](/languages/assembly/segmentation-fault) - memory access violations
