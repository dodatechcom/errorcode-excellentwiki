---
title: "Register allocation error"
description: "A register allocation error occurs when code corrupts or misuses register state, leading to incorrect program behavior or crashes."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["register", "allocation", "corruption", "convention"]
weight: 5
---

## What This Error Means

A register allocation error occurs when the programmer incorrectly manages register contents, such as failing to preserve callee-saved registers across function calls, clobbering registers used by calling conventions, or using a register for two conflicting purposes simultaneously. This can lead to subtle data corruption or hard-to-diagnose crashes.

## Common Causes

- Not preserving callee-saved registers (`rbx`, `rbp`, `r12`-`r15`) across calls
- Clobbering register values that are needed after a function call
- Mixing up caller-saved and callee-saved register conventions
- Using the wrong register width (e.g., `eax` vs `rax`) and getting truncated values

## How to Fix

```asm
; WRONG: Clobbering callee-saved register without preserving it
my_func:
    mov rbx, 42           ; rbx is callee-saved - must preserve
    call external_func    ; external_func may expect rbx unchanged
    ; rbx is now corrupted
    ret

; CORRECT: Save and restore callee-saved registers
my_func:
    push rbx              ; save callee-saved register
    mov rbx, 42
    call external_func    ; rbx is safe across this call
    pop rbx               ; restore original value
    ret
```

```asm
; WRONG: Using wrong register width after 64-bit operation
    mov rax, 0x1FFFFFFFF    ; value exceeds 32 bits
    mov ebx, eax            ; truncates to lower 32 bits - value lost

; CORRECT: Use matching register widths
    mov rax, 0x1FFFFFFFF
    mov rbx, rax            ; preserves full 64-bit value
```

## Examples

```asm
section .text
    global _start

_start:
    ; WRONG: Not preserving rdi across printf call
    mov rdi, format_str
    call printf             ; printf clobbers rax, rcx, rdx, rsi, rdi
    ; rdi is now destroyed - cannot use it
    mov rdi, 0              ; would have worked if preserved

    ; CORRECT approach:
    push rdi                ; save before call
    mov rdi, format_str
    call printf
    pop rdi                 ; restore after call

    mov rax, 60
    xor rdi, rdi
    syscall

section .data
    format_str db "Value: %d", 10, 0
```

## Related Errors

- [Segmentation fault](/languages/assembly/segfault-error)
- [Invalid instruction](/languages/assembly/invalid-instruction)
