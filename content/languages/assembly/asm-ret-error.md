---
title: "[Solution] Assembly RET Error -- Incorrect Return from Function"
description: "Fix assembly RET errors when returning from functions with incorrect stack state."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Assembly RET Error

This error occurs when the `RET` instruction is executed with the stack pointer pointing to a wrong return address.

## Common Causes

- PUSH/POP mismatch causing wrong return address on stack
- RET with extra values on stack
- Missing RET instruction at end of function
- CALL to wrong address

## How to Fix

### Balance PUSH and POP

```asm
; WRONG: unbalanced PUSH
my_func:
    push rbx
    push r12
    ; ... body ...
    pop rbx    ; pops r12 value into rbx
    ret        ; returns to wrong address

; CORRECT: balanced PUSH/POP
my_func:
    push rbx
    push r12
    ; ... body ...
    pop r12
    pop rbx
    ret
```

### Use LEAVE for standard prologue

```asm
my_func:
    push rbp
    mov rbp, rsp
    sub rsp, 32
    ; ... body ...
    leave   ; mov rsp, rbp; pop rbp
    ret
```

## Examples

```asm
; Clean function return
calculate:
    push rbp
    mov rbp, rsp
    mov eax, edi
    add eax, esi
    pop rbp
    ret
```
