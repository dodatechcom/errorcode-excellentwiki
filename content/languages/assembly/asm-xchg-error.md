---
title: "[Solution] Assembly XCHG Error -- Incorrect Register Exchange"
description: "Fix assembly XCHG errors when exchanging register values incorrectly."
languages: ["assembly"]
error-types: ["syntax-error"]
severities: ["error"]
---

# Assembly XCHG Error

This error occurs when the `XCHG` instruction is used with incorrect operands or where a MOV would be more appropriate.

## Common Causes

- Using XCHG with immediate values (not allowed)
- XCHG with memory implicitly locked (performance issue)
- Swapping when MOV would suffice
- Incorrect operand sizes

## How to Fix

### Use XCHG correctly

```asm
; WRONG: XCHG cannot use immediate
xchg eax, 42  ; error

; CORRECT: XCHG only register-to-register or register-to-memory
xchg eax, ebx
xchg eax, [memory]
```

### Avoid XCHG with memory (implicit LOCK)

```asm
; XCHG with memory has implicit LOCK prefix (slow)
; PREFERRED: use MOV and XCHG for registers only
mov eax, [mem1]
mov ebx, [mem2]
xchg eax, ebx  ; fast register swap
mov [mem1], eax
mov [mem2], ebx
```

## Examples

```asm
; Swap two values
swap:
    mov rax, [rdi]
    mov rbx, [rsi]
    xchg rax, rbx
    mov [rdi], rax
    mov [rsi], rbx
    ret
```
