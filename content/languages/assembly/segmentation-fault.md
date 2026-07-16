---
title: "Segmentation fault (core dumped)"
description: "A segmentation fault occurs when a program attempts to access memory that it is not allowed to access."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["memory", "segmentation-fault", "core-dumped"]
weight: 5
---

## What This Error Means

A segmentation fault (commonly abbreviated as segfault) occurs when a program tries to read or write to a memory address that the operating system has not allocated for it, or that it does not have permission to access. In assembly, this typically happens due to incorrect pointer manipulation, stack corruption, or accessing uninitialized/invalid memory locations.

## Common Causes

- Dereferencing a null or uninitialized pointer register
- Writing beyond the bounds of an allocated buffer or stack frame
- Incorrect stack alignment (e.g., pushing wrong number of bytes)
- Jumping to an invalid memory address (e.g., corrupted return address)

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
; WRONG: Writing beyond stack bounds
push rax
push rbx
push rcx
push rdx
push r8
push r9
push r10
push r11
push r12
push r13
push r14
push r15
push rsi
push rdi
push rbp
sub rsp, 1024        ; may overflow if stack is small

; CORRECT: Use appropriate stack frames and allocate conservatively
push rbp
mov rbp, rsp
sub rsp, 64          ; reasonable local allocation
; ... function body ...
mov rsp, rbp
pop rbp
ret
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

## How to Debug

- Use `gdb` to get the exact instruction and register values at fault
- Compile with debug symbols: `nasm -g -F dwarf file.asm`
- Use `valgrind` to detect memory issues early
- Check stack alignment before and after function calls

## Related Errors

- [Stack overflow](/languages/assembly/stack-overflow)
