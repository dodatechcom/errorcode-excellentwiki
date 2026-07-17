---
title: "Segmentation fault"
description: "A segmentation fault occurs when a program attempts to access memory that it is not allowed to access."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A segmentation fault occurs when a program tries to read or write to a memory address that the operating system has not allocated for it, or that it does not have permission to access. In assembly, this is one of the most common runtime errors and typically results from incorrect pointer manipulation, stack corruption, or accessing uninitialized memory locations.

## Common Causes

- Dereferencing a null or uninitialized pointer register
- Writing beyond the bounds of an allocated buffer or stack frame
- Jumping to an invalid memory address (e.g., corrupted return address)
- Incorrect stack alignment before a `call` or `ret` instruction

## How to Fix

```asm
; WRONG: Accessing memory through a null pointer
mov rax, 0
mov rbx, [rax]       ; segfault - rax is NULL

; CORRECT: Ensure pointer is valid before dereferencing
mov rax, buffer
test rax, rax
jz .handle_error
mov rbx, [rax]       ; safe dereference
```

```asm
; WRONG: Calling a function without proper stack alignment
push rdi
push rsi
call printf           ; stack may be misaligned

; CORRECT: Align stack to 16 bytes before call
push rdi
push rsi
and rsp, -16         ; align to 16-byte boundary
call printf
```

## Examples

```asm
section .data
    msg db "Hello", 0

section .text
    global _start

_start:
    ; WRONG: loading from invalid address
    mov rax, 0xDEAD        ; arbitrary invalid address
    mov rbx, [rax]         ; segfault here

    ; WRONG: incorrect indirect call
    xor rax, rax
    call rax               ; jumping to NULL - segfault

    mov rax, 60            ; sys_exit
    xor rdi, rdi
    syscall
```

## Related Errors

- [Stack overflow](/languages/assembly/stack-overflow)
- [Invalid memory access](/languages/assembly/memory-access)
