---
title: "Stack overflow (segmentation fault)"
description: "A stack overflow occurs when the call stack exceeds its allocated size, often resulting in a segmentation fault."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["stack", "overflow", "segmentation-fault"]
weight: 5
---

## What This Error Means

A stack overflow in assembly happens when too many values are pushed onto the stack without being popped off, or when a recursive function never reaches a base case. The stack grows downward on most architectures, and when it collides with the heap or unmapped memory, the result is a segmentation fault.

## Common Causes

- Infinite recursion without a proper base case
- Excessive stack allocation for local variables
- Pushing values in a loop without corresponding pops
- Missing `ret` instructions causing repeated function calls

## How to Fix

```asm
; WRONG: Infinite recursion - no base case
recursive_func:
    push rbp
    mov rbp, rsp
    sub rsp, 16
    call recursive_func     ; calls itself forever
    leave
    ret

; CORRECT: Proper base case
recursive_func:
    push rbp
    mov rbp, rsp
    sub rsp, 16
    cmp rdi, 0              ; base case check
    je .done
    dec rdi
    call recursive_func     ; only recurse when rdi > 0
.done:
    leave
    ret
```

```asm
; WRONG: Excessive stack usage in a loop
push_loop:
    push rax                ; keeps pushing without popping
    inc rax
    cmp rax, 1000000
    jl push_loop

; CORRECT: Use stack properly or use heap
push_loop:
    sub rsp, 8              ; allocate once
    mov [rsp], rax
    ; ... process ...
    add rsp, 8              ; deallocate
    inc rax
    cmp rax, 1000000
    jl push_loop
```

## Examples

```asm
section .text
    global _start

_start:
    ; Stack overflow via recursion
    mov rdi, 100000         ; large recursion depth
    call recursive_factorial

    mov rax, 60
    xor rdi, rdi
    syscall

recursive_factorial:
    push rbp
    mov rbp, rsp
    push rbx
    mov rbx, rdi
    cmp rdi, 1
    jle .base_case
    dec rdi
    call recursive_factorial  ; depth of 100000 = stack overflow
    imul rax, rbx
    jmp .done
.base_case:
    mov rax, 1
.done:
    pop rbx
    pop rbp
    ret
```

## How to Debug

- Compile with a larger stack size if recursion depth is legitimately deep
- Use `ulimit -s unlimited` to increase stack size during testing
- Check for missing `ret` or `pop` instructions
- Use GDB `backtrace` to see the call chain

## Related Errors

- [Segmentation fault (core dumped)](/languages/assembly/segmentation-fault)
