---
title: "[Solution] Assembly Red Zone Error -- Stack Red Zone Misuse"
description: "Fix assembly red zone errors when the 128-byte stack red zone is used incorrectly."
languages: ["assembly"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Assembly Red Zone Error

This error occurs when the 128-byte stack red zone is used incorrectly, such as in interrupt handlers or when RSP is manipulated.

## Common Causes

- Using red zone in functions that call other functions
- Red zone overwritten by signal handlers
- Not adjusting RSP before using red zone space
- Red zone in interrupt handlers (must save all state)

## How to Fix

### Use red zone correctly

```asm
; WRONG: calling function uses red zone
my_func:
    mov [rsp-8], rax  ; red zone
    call other_func   ; may overwrite red zone!
    mov rax, [rsp-8]  ; corrupted!

; CORRECT: only use red zone if no calls
leaf_func:
    sub rsp, 16       ; skip red zone if needed
    mov [rsp+8], rax  ; safe space
    ; ...
    add rsp, 16
    ret
```

### Leaf functions can use red zone

```asm
; Leaf function (no calls) can use red zone
leaf:
    mov [rsp-8], rdi  ; safe: no calls
    ; ... use [rsp-8] ...
    ret
```

## Examples

```asm
; Safe leaf function with red zone
abs_val:
    mov rax, rdi
    test rdi, rdi
    jns .positive
    neg rax
.positive:
    ret
```
