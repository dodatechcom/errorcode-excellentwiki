---
title: "[Solution] Assembly Interrupt Error -- Incorrect INT Usage"
description: "Fix assembly interrupt errors when using INT instruction incorrectly."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Assembly Interrupt Error

This error occurs when the INT instruction is used incorrectly, such as calling undefined interrupt handlers.

## Common Causes

- INT with interrupt vector not set up in IDT
- Not saving/restoring registers in interrupt handler
- INT 0x80 used in 64-bit mode (should use syscall)
- Missing IRET in interrupt handler

## How to Fix

### Use correct interrupt mechanism

```asm
; WRONG: INT 0x80 in 64-bit mode
mov rax, 1
mov rdi, 1
lea rsi, [msg]
mov rdx, 13
int 0x80  ; 32-bit syscall interface

; CORRECT: use syscall in 64-bit mode
mov rax, 1
mov rdi, 1
lea rsi, [msg]
mov rdx, 13
syscall
```

### Handle interrupts properly

```asm
; Simple interrupt handler
my_handler:
    push rax
    push rcx
    push rdx
    ; ... handle interrupt ...
    pop rdx
    pop rcx
    pop rax
    iretq
```

## Examples

```asm
; Software interrupt for debugging
debug_break:
    int 3  ; breakpoint interrupt
    ret
```
