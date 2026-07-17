---
title: "Stack overflow in Assembly"
description: "A stack overflow in Assembly occurs when the call stack exceeds its allocated memory, corrupting return addresses and local variables."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["stack", "overflow", "recursive", "memory", "rsp"]
weight: 5
---

## What This Error Means

A stack overflow in Assembly happens when too many function calls are nested (recursion) or too much data is pushed onto the stack, exceeding the stack's memory limit. The stack grows downward on x86/x64.

## Common Causes

- Unbounded recursion (function calls itself infinitely)
- Excessive local variable allocation
- Not restoring stack pointer after push/pop
- Large stack-allocated buffers

## How to Fix

```asm
; WRONG: Infinite recursion
recursive_func:
    push rbp
    mov rbp, rsp
    call recursive_func   ; stack overflow - never returns
    pop rbp
    ret

; CORRECT: Add base case
recursive_func:
    push rbp
    mov rbp, rsp
    cmp rdi, 0
    jle .done            ; base case: stop recursion
    dec rdi
    call recursive_func
.done:
    pop rbp
    ret
```

```asm
; WRONG: Excessive stack allocation
big_function:
    sub rsp, 1000000     ; 1MB - may overflow

; CORRECT: Use heap or allocate conservatively
big_function:
    sub rsp, 64          ; reasonable stack frame
```

## Examples

```asm
; Stack overflow example
section .text
    global _start
_start:
    mov rsp, stack_top
    call _start           ; recursive call with no base case
    ; stack grows until SIGSEGV

section .bss
    resb 4096
stack_top:
```

## How to Debug

- Use `gdb` to watch RSP value
- Compile with stack protector: `nasm -g -F dwarf file.asm`
- Use `valgrind --tool=memcheck` for stack analysis

## Related Errors

- [Segmentation Fault](/languages/assembly/segmentation-fault) - memory access violations
- [Page Fault](/languages/assembly/asm-page-fault) - invalid memory page access
