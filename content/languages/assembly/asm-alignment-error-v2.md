---
title: "[Solution] SIGBUS: alignment error in assembly"
description: "Fix assembly SIGBUS errors caused by memory alignment violations when accessing unaligned addresses."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

SIGBUS (bus error) from alignment error occurs when assembly code attempts to access memory at an address that is not properly aligned for the data type. For example, accessing a 4-byte integer at an address not divisible by 4.

## Common Causes

- Accessing 4-byte value at odd address
- Incorrect pointer arithmetic
- Moving data to unaligned stack locations
- Network/file data not properly aligned
- Architecture-specific alignment requirements

## How to Fix

```asm
; WRONG: Unaligned access on strict alignment architecture
section .data
    unaligned_data db 0, 0, 0, 1, 2, 3, 4, 5

section .text
    lea rax, [rel unaligned_data + 1]  ; Not 4-byte aligned
    mov ebx, [rax]    ; SIGBUS on some architectures

; CORRECT: Ensure alignment
section .data
    align 4
    aligned_data dd 0x01020304, 0x05060708

section .text
    lea rax, [rel aligned_data]
    mov ebx, [rax]    ; Safe: properly aligned
```

```asm
; WRONG: Unaligned stack access
section .text
    sub rsp, 8
    mov rax, rsp
    inc rax           ; rax now unaligned
    mov [rax], 0      ; Potential SIGBUS

; CORRECT: Maintain stack alignment
section .text
    sub rsp, 16       ; Keep 16-byte alignment
    mov rax, rsp
    mov [rax], 0      ; Safe
    add rsp, 16
```

```asm
; CORRECT: Safe unaligned load (if architecture supports it)
section .text
    ; On x86-64 with REX prefix
    lea rsi, [rel unaligned_data + 1]
    movzx eax, byte [rsi]      ; Byte access - always safe
    movzx ebx, word [rsi]      ; May need alignment check
```

```asm
; CORRECT: Use memcpy for unaligned data
section .text
    ; Copy unaligned data to aligned buffer
    lea rsi, [rel unaligned_data]
    lea rdi, [rel aligned_buffer]
    mov rcx, 8
    rep movsb
```

## Related Errors

- [Segmentation Fault](asm-segmentation-fault-v2) - memory access
- [Page Fault](asm-page-fault-v2) - page errors
- [General Protection](asm-general-protection-v2) - protection faults
