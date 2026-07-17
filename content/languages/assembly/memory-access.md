---
title: "Invalid memory access"
description: "An invalid memory access error occurs when a program attempts to read or write to a memory address that is not mapped or permitted."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An invalid memory access occurs when the program attempts to read from or write to a memory address that is not mapped in the process's virtual address space, or where the page permissions do not allow the requested operation (e.g., writing to read-only memory). This is closely related to a segmentation fault but specifically refers to address-level violations.

## Common Causes

- Accessing memory beyond the end of an allocated segment
- Writing to read-only data sections (e.g., `.rodata`)
- Using a freed or deallocated memory pointer
- Incorrect offset calculations in addressing modes

## How to Fix

```asm
; WRONG: Writing to read-only data section
section .rodata
    msg db "Hello", 0

section .text
    mov byte [msg], 'h'    ; cannot write to .rodata - invalid access

; CORRECT: Use writable data section
section .data
    msg db "Hello", 0

section .text
    mov byte [msg], 'h'    ; .data is writable
```

```asm
; WRONG: Accessing memory with incorrect offset
lea rax, [rbx + rcx*8]     ; if rcx is negative, offset underflows
mov rdx, [rax]              ; may access invalid memory

; CORRECT: Validate index before computing address
test rcx, rcx
js .invalid_index
cmp rcx, array_size
jge .invalid_index
lea rax, [rbx + rcx*8]
mov rdx, [rax]              ; safe access
```

## Examples

```asm
section .data
    buffer db 64 dup(0)

section .text
    global _start

_start:
    ; WRONG: Accessing beyond allocated buffer
    mov rdi, buffer
    mov byte [rdi + 256], 'X'   ; 256 bytes past buffer end
                               ; invalid memory access

    ; WRONG: Accessing uninitialized/NULL pointer
    xor rax, rax
    mov rbx, [rax + 8]         ; accessing address 0x08 - invalid

    mov rax, 60
    xor rdi, rdi
    syscall
```

## Related Errors

- [Segmentation fault](/languages/assembly/segfault-error)
- [Stack overflow](/languages/assembly/stack-overflow6)
