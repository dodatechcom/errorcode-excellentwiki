---
title: "[Solution] Segfault: null pointer dereference in assembly"
description: "Fix assembly segmentation faults caused by null pointer dereference, invalid memory access, and memory protection violations."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["segfault", "null-pointer", "memory", "access-violation", "signal", "assembly"]
weight: 5
---

## What This Error Means

A segmentation fault (SIGSEGV) from null pointer dereference occurs when assembly code attempts to read from or write to memory address 0, which is protected by the operating system.

## Common Causes

- Uninitialized pointer register (contains 0)
- Failed memory allocation not checked
- Incorrect base or index register values
- Stack pointer corruption
- Jumping to address 0

## How to Fix

```asm
; WRONG: Dereferencing uninitialized pointer
section .text
    mov rax, 0       ; rax = NULL
    mov rbx, [rax]   ; SIGSEGV: read from address 0

; CORRECT: Check pointer before use
    mov rax, 0
    test rax, rax
    jz .null_error
    mov rbx, [rax]
    jmp .done
.null_error:
    ; Handle NULL pointer error
.done:
```

```asm
; WRONG: malloc result not checked
section .text
    mov rdi, 1024
    call malloc      ; Returns pointer in rax
    mov [rax], 0     ; May be NULL if malloc failed

; CORRECT: Check malloc return value
    mov rdi, 1024
    call malloc
    test rax, rax
    jz .malloc_failed
    mov qword [rax], 0
    jmp .done
.malloc_failed:
    ; Handle allocation failure
.done:
```

```asm
; CORRECT: Safe memory access pattern
section .text
    global _start
_start:
    ; Load base address
    lea rax, [rel data]
    test rax, rax
    jz .error
    
    ; Safe dereference
    mov rbx, [rax]
    jmp .exit
.error:
    mov rdi, 1
    mov rax, 60
    syscall
.exit:
    mov rdi, 0
    mov rax, 60
    syscall

section .data
    data dq 42
```

## Related Errors

- [Stack Overflow](asm-stack-overflow-v2) - stack pointer issues
- [Page Fault](asm-page-fault-v2) - page errors
- [General Protection](asm-general-protection-v2) - protection faults
