---
title: "[Solution] Stack overflow: stack pointer out of bounds"
description: "Fix assembly stack overflow when the stack pointer exceeds allocated stack memory boundaries."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Stack overflow in assembly occurs when the stack pointer (RSP on x86-64) moves beyond the allocated stack memory, causing a segmentation fault. This is common with deep recursion or large stack allocations.

## Common Causes

- Deep or infinite recursion
- Large local variables on stack
- Stack buffer overflow (writing past array bounds)
- Missing stack frame cleanup
- Incorrect stack alignment

## How to Fix

```asm
; WRONG: Infinite recursion
section .text
    global recursive_func
recursive_func:
    push rbp
    mov rbp, rsp
    call recursive_func  ; Never returns - stack overflow
    pop rbp
    ret

; CORRECT: Proper recursion with base case
section .text
    global recursive_func
recursive_func:
    push rbp
    mov rbp, rsp
    
    ; Base case
    cmp rdi, 0
    jle .base_case
    
    ; Recursive case
    dec rdi
    call recursive_func
    
.base_case:
    mov rax, rdi
    pop rbp
    ret
```

```asm
; WRONG: Writing past stack buffer
section .text
    sub rsp, 16      ; 16 bytes allocated
    mov qword [rsp + 32], 0  ; Overflow: offset 32 > 16

; CORRECT: Stay within bounds
    sub rsp, 32      ; Allocate enough space
    mov qword [rsp + 16], 0  ; Safe: within 32 bytes
```

```asm
; CORRECT: Check stack limits
section .text
    ; Compare stack pointer to guard page
    lea rax, [rel stack_limit]
    cmp rsp, rax
    jbe .stack_overflow
    
    ; Safe to proceed
    sub rsp, 64
    ; ... function body ...
    add rsp, 64
    ret
    
.stack_overflow:
    ; Handle overflow
    mov rdi, 1
    mov rax, 60
    syscall

section .bss
    stack_limit resq 1
```

```asm
; CORRECT: Use callee-saved registers for large data
section .text
    push rbx
    push r12
    
    ; Use registers instead of stack for frequently accessed data
    mov rbx, rdi
    mov r12, rsi
    
    ; Process using registers
    mov rdi, rbx
    call process
    
    pop r12
    pop rbx
    ret
```

## Related Errors

- [Segmentation Fault](asm-segmentation-fault-v2) - memory access
- [Page Fault](asm-page-fault-v2) - page errors
- [General Protection](asm-general-protection-v2) - protection faults
