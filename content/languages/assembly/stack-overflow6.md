---
title: "Stack overflow"
description: "A stack overflow occurs when a program exhausts the available stack space, typically due to excessive recursion or large stack allocations."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["stack", "overflow", "recursion", "memory"]
weight: 5
---

## What This Error Means

A stack overflow occurs when the call stack grows beyond its allocated limit. In assembly, this typically happens when functions push too many values onto the stack, allocate excessive local variables, or recurse without a proper base case. The kernel detects the stack guard page being hit and terminates the process.

## Common Causes

- Recursive functions without a base case or with too deep recursion
- Allocating excessively large local buffers on the stack
- Missing stack frame cleanup (e.g., forgetting to `ret` or restore `rsp`)
- Excessive `push` instructions without corresponding `pop`s

## How to Fix

```asm
; WRONG: Unbounded recursion with large stack frame
deep_push:
    push rbx
    push rcx
    push rdx
    push r8
    push r9
    call deep_push       ; infinite recursion - stack overflow

; CORRECT: Add a base case and use minimal stack space
deep_push:
    test rdi, rdi        ; check recursion counter
    jz .done
    dec rdi
    push rdi
    call deep_push
    pop rdi
.done:
    ret
```

```asm
; WRONG: Large local allocation on stack
bad_alloc:
    sub rsp, 65536       ; 64KB on stack - risky

; CORRECT: Use heap allocation for large buffers
good_alloc:
    mov rdi, 65536
    call malloc          ; allocate on heap instead
    test rax, rax
    jz .alloc_failed
```

## Examples

```asm
section .text
    global _start

_start:
    ; WRONG: Recursive call pushes stack frames indefinitely
    xor rdi, rdi
    call recursive_func
    jmp .exit

recursive_func:
    push rbp
    mov rbp, rsp
    sub rsp, 256          ; large local allocation
    inc rdi
    call recursive_func   ; no base case - stack overflow
    mov rsp, rbp
    pop rbp
    ret

.exit:
    mov rax, 60
    xor rdi, rdi
    syscall
```

## Related Errors

- [Segmentation fault](/languages/assembly/segmentation-fault)
- [Invalid memory access](/languages/assembly/memory-access)
